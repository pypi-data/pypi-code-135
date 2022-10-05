
import logging
import requests

from datetime import datetime
from typing import Generator, List, Optional
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

from intelinair_utils.api import Api

logger = logging.getLogger(__name__)

KNOWN_ENVS = ['prod', 'release', 'bellflower', 'local']


class MLApi(Api):
    """
    Wrapper class for authenticated queries against the ML Service

    After initialization, authentication has been completed and requests
    through this object will be automatically authenticated.
    """

    def __init__(self, environment):
        # version_string == '' corresponds to the first version of API
        assert environment in KNOWN_ENVS, 'Unknown environment for the ML Service'
        self.environment = environment
        if environment == 'local':
            self.api_url = 'http://localhost:8080'
        else:
            self.api_url = f'https://ml.{environment}.int.intelinair.dev'
        # all calls (other than login) should use the version string
        self.session = requests.Session()
        retries = Retry(total=10, read=5, connect=5, backoff_factor=1, allowed_methods=False,
                        status_forcelist=[104, 500, 502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def get(self, path, params=None, json=None, ignore_json=False):
        res = self.session.get(self.api_url + path, params=params, json=json)
        res.raise_for_status()
        if ignore_json is True:
            return res
        else:
            return res.json()

    def post(self, path, json=None, params=None):
        res = self.session.post(self.api_url + path, json=json, params=params)
        res.raise_for_status()
        return res.json()

    def patch(self, path, json=None, params=None):
        res = self.session.patch(self.api_url + path, json=json, params=params)
        res.raise_for_status()
        return res.json()

    def create_dataset(self, name: str, version: int, data: dict, tags: dict = None) -> dict:
        """Creates a dataset with the given parameters"""
        return self.post('/datasets/', json={
            'name': name,
            'version': version,
            'data': data,
            'tags': tags
        })

    def update_dataset(self, dataset: dict) -> dict:
        """Updates a dataset object in the service with new data"""
        return self.patch(f'/datasets/{dataset["id"]}', json=dataset)

    def get_dataset_by_id(self, dataset_id: int) -> dict:
        """Gets a dataset by its id"""
        return self.get(f'/datasets/{dataset_id}')

    def get_datasets(self, dataset_name: str = None, dataset_version: int = None, api_limit_size: int = 100) -> Generator[dict, None, None]:
        """Gets a generator of datasets optionally filtering by name and/or version"""
        skip = 0
        while True:
            datasets = self.get(
                '/datasets/',
                params={
                    'skip': skip,
                    'limit': api_limit_size,
                    'name': dataset_name,
                    'version': dataset_version
                }
            )
            for dataset in datasets:
                yield dataset
            if len(datasets) == api_limit_size:
                skip += api_limit_size
            else:
                break

    def get_dataset(self, dataset_name: str, dataset_version: int = None) -> dict:
        """Gets a dataset by name and optionally a specific version of the dataset"""
        datasets = sorted(list(self.get_datasets(dataset_name, dataset_version)), key=lambda x: x['version'])
        if len(datasets) == 0:
            raise Exception(f'Could not find dataset with  '
                            f'dataset_name={dataset_name} and version={dataset_version}')
        return datasets[-1]

    def create_model(self, model_name: str, model_version: int, model_hash: str, s3_location: str,
                     tags: dict = None, data: dict = None) -> dict:
        """Creates a model with the ML Service with the given parameters"""
        return self.post(
            '/models/',
            json={
                "model_name": model_name,
                "model_version": model_version,
                "model_hash": model_hash,
                "s3_location": s3_location,
                "tags": tags,
                "data": data
            }
        )

    def update_model(self, model: dict) -> dict:
        """Updates a model"""
        return self.patch(f'/models/{model["id"]}', json=model)

    def get_or_create_model_from_script(self, git_repo_name: str, script_name: str, git_description: str) -> dict:
        """Gets a model by script name and git description or creates one if it doesn't exist"""
        return self.post('/models/script', params={
            'git_repo_name': git_repo_name,
            'script_name': script_name,
            'git_description': git_description
        })

    def get_model_by_id(self, model_id: int) -> dict:
        """Gets a model by id"""
        return self.get(f'/models/{model_id}')

    def get_latest_model(self, model_name: str) -> dict:
        """Gets a model by id"""
        return self.get(f'/models/latest', params={'model_name': model_name})

    def get_models(self, model_name: str = None, model_version: int = None, api_limit_size: int = 100) -> Generator[dict, None, None]:
        """Gets models from the api with optional filters"""
        skip = 0
        while True:
            models = self.get(f'/models/?skip={skip}&limit={api_limit_size}',
                              json={'model_name': model_name, 'model_version': model_version})
            for model in models:
                yield model
            if len(models) == api_limit_size:
                skip += api_limit_size
            else:
                break

    def get_model(self, model_name: str, model_version: int = None) -> dict:
        """Gets the model with the give name and version, if no version is specified the latest version is returned"""
        models = sorted(list(self.get_models(model_name, model_version)), key=lambda x: x['model_version'])
        if len(models) == 0:
            raise Exception(f'Could not find registered models with '
                            f'model_name={model_name} and version={model_version}')
        return models[-1]

    def create_inference(self, flight_code: str, inference_type: str, model_id: int, docker_image: str,
                         hparams: dict, result: dict) -> dict:
        """Creates an inference with the given parameters"""
        return self.post('/inferences/flight/', json={
            'flight_code': flight_code,
            'inference_type': inference_type,
            'model_id': model_id,
            'docker_image': docker_image,
            'hparams': hparams,
            'result': result
        })

    def create_inference_from_script(self, flight_code: str, inference_type: str, result: dict, git_repo_name: str,
                                     script_name: str, git_description: str, hparams: dict,
                                     docker_image: Optional[str] = None):
        """Creates an inference from a script"""
        return self.post('/inferences/flight/script', json={
            'flight_code': flight_code,
            'inference_type': inference_type,
            'git_repo_name': git_repo_name,
            'script_name': script_name,
            'git_description': git_description,
            'docker_image': docker_image,
            'hparams': hparams,
            'result': result
        })

    def update_inference(self, inference: dict) -> dict:
        return self.patch(f'/inferences/flight/{inference["id"]}', json=inference)

    def get_inference_by_id(self, inference_id: int) -> dict:
        """Gets an inference by id"""
        return self.get(f'/inferences/flight/{inference_id}')

    def get_inferences(self, flight_code: List[str] = None, inference_type: str = None, model_id: int = None,
                       model_name: str = None, model_version: int = None, git_repo_name: str = None,
                       script_name: str = None, git_description: str = None, docker_image: str = None,
                       hparams: dict = None, start_ts: datetime = None, end_ts: datetime = None,
                       api_limit_size: int = 100) -> Generator[dict, None, None]:
        """Returns inferences that match the provided filters"""
        request = {
            'flight_code': flight_code,
            'inference_type': inference_type,
            'start_ts': str(start_ts) if start_ts else None,
            'end_ts': str(end_ts) if end_ts else None,
            'model_id': model_id,
            'model_name': model_name,
            'model_version': model_version,
            'git_repo_name': git_repo_name,
            'script_name': script_name,
            'git_description': git_description,
            'docker_image': docker_image,
            'hparams': hparams
        }

        skip = 0
        while True:
            inferences = self.get(f'/inferences/flight/?skip={skip}&limit={api_limit_size}', json=request)
            for inference in inferences:
                yield inference
            if len(inferences) == api_limit_size:
                skip += api_limit_size
            else:
                break

    def get_inference_types(self, flight_code: str) -> List[str]:
        """Returns the inference types available for this flight"""
        return self.get(f'/inferences/flight/types/{flight_code}')

    def get_flight_codes_with_inference_type(self, inference_type: str,
                                             api_limit_size: int = 10000) -> Generator[str, None, None]:
        """Returns a list of flight codes with an inference with the given inference type"""
        skip = 0
        while True:
            flight_codes = self.get(f'/inferences/flight/codes/{inference_type}?skip={skip}&limit={api_limit_size}')
            for flight_code in flight_codes:
                yield flight_code
            if len(flight_codes) == api_limit_size:
                skip += api_limit_size
            else:
                break

    def create_flight_evaluation(self, flight_code: str, inference_id: int, scores: dict) -> dict:
        """Creates an evaluation for a flight with the given parameters"""
        return self.post('/evaluations/flight/', json={
            'flight_code': flight_code,
            'inference_id': inference_id,
            'scores': scores,
        })

    def get_flight_evaluation_by_id(self, flight_evaluation_id: int) -> dict:
        """Returns an evaluation by id"""
        return self.get(f'/evaluations/flight/{flight_evaluation_id}')

    def get_flight_evaluations(self, flight_code: List[str] = None, inference_type: str = None,
                               model_id: int = None, model_name: str = None, model_version: int = None,
                               git_repo_name: str = None, script_name: str = None, git_description: str = None,
                               docker_image: str = None, hparams: dict = None,
                               inference_id: int = None, api_limit_size: int = 100) -> Generator[dict, None, None]:
        """Generates a set of evaluations that match the provided filters"""
        skip = 0
        while True:
            evaluations = self.get(
                '/evaluations/flight/',
                json={
                    'flight_code': flight_code,
                    'inference_type': inference_type,
                    'model_id': model_id,
                    'model_name': model_name,
                    'model_version': model_version,
                    'git_repo_name': git_repo_name,
                    'script_name': script_name,
                    'git_description': git_description,
                    'docker_image': docker_image,
                    'hparams': hparams,
                    'inference_id': inference_id,
                },
                params={
                    'skip': skip,
                    'limit': api_limit_size,
                }
            )
            for evaluation in evaluations:
                yield evaluation
            if len(evaluations) == api_limit_size:
                skip += api_limit_size
            else:
                break

    def create_dataset_evaluation(self, dataset_id: int, model_id: int, scores: dict, hparams: dict, tags: dict = None,
                                  docker_image: str = None) -> dict:
        """Creates an evaluation for the given dataset and model"""
        return self.post('/evaluations/dataset/', json={
            'dataset_id': dataset_id,
            'model_id': model_id,
            'scores': scores,
            'hparams': hparams,
            'tags': tags,
            'docker_image': docker_image
        })

    def get_dataset_evaluation_by_id(self, dataset_evaluation_id: int) -> dict:
        """Returns a dataset evaluation by id"""
        return self.get(f'/evaluations/dataset/{dataset_evaluation_id}')

    def get_dataset_evaluations(self, model_id: id = None, docker_image: str = None, hparams: dict = None,
                                dataset_id: int = None, api_limit_size: int = 100) -> Generator[dict, None, None]:
        """Generates a set of dataset evaluations that match the given parameters"""
        skip = 0
        while True:
            evaluations = self.get(
                '/evaluations/dataset/',
                json={
                    'model_id': model_id,
                    'docker_image': docker_image,
                    'hparams': hparams,
                    'dataset_id': dataset_id,
                },
                params={
                    'skip': skip,
                    'limit': api_limit_size,
                }
            )
            for evaluation in evaluations:
                yield evaluation
            if len(evaluations) == api_limit_size:
                skip += api_limit_size
            else:
                break

