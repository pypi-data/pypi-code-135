import json
from json import JSONEncoder
import numpy as np
from trojsdk.client import TrojClient

"""
The troj job handler class wraps the client and stores all details relevant to a given job or session
"""
class TrojJobHandler():
    def __init__(self) -> None:
        self.client = None

    def post_job_to_endpoint(self, config:dict, docker_metadata:dict=None) -> dict:
        """

        This function posts any given config to the endpoint supplied, can be used via command line or programmatically

        *Params*
        config: dict
            The main configuration for the project.
        docker_metadata: dict
            A dictionary with the following two values;
            "docker_image_url": A Docker Hub image id for any engine type.
                Ex. value: "trojai/troj-engine-base-tabular:tabluar-shawn-latest"
            "docker_secret_name": The name of the environment secret containing the credentials for Docker Hub access. This is defined in the TrojAI helm repo in the _setup.sh_ script.

        *Return*
        dict
            Contains job_name under key "data", under key "job_name". (Dict within dict)

        *Raises*
        Exception
            If docker_metadata is not defined, and the config does not contain a valid task type. (tabular, nlp, vision, ...)

        """

        self._set_config(config)
        if not docker_metadata:
            docker_metadata = {
                "docker_secret_name": "trojaicreds"
            }
            try:
                docker_choices_dict = {
                    "tabular": "trojai/troj-engine-base-tabular:tabluar-shawn-latest",
                    "nlp": "trojai/troj-engine-base-nlp:nlp-shawn-latest",
                    "vision": "trojai/troj-engine-base-cv:cv-shawn-latest",
                }
                docker_metadata["docker_image_url"] = docker_choices_dict[str(config.get("task_type")).lower()]
            except Exception as e:
                raise Exception("Model type " + str(config.get("task_type", "none")) + " not found. Please select one of " + str(list(docker_choices_dict))) from e

        res = self.client.post_job(config, docker_metadata)

        return res


    def _set_config(self, config):
        """
        Instantiates the client class using the passed config file
        param config dict:
        """
        self.client = TrojClient(api_endpoint=config.get("auth_config").get("api_endpoint"), api_key="api")
        self.client.set_credentials(
            id_token=config["auth_config"]["auth_keys"]["id_token"],
            refresh_token=config["auth_config"]["auth_keys"]["refresh_token"],
            api_key=config["auth_config"]["auth_keys"]["api_key"],
        )

    def check_job_status(self, response:dict, format_pretty:bool=True):
        """
        return only the current status of the pod in cluster based on the job id
        """
        job_name = response.get("data").get("job_name")
        if self.client is None:
            print("No jobs have been submitted yet! Call the post_job_to_endpoint and pass the required config first.")
        else:

            res = self.client.get_job_status(job_name)
            if format_pretty:
                mess = res['data']['Message']
                mess = str(mess).replace("\\n", "\n").replace("\'", "").replace("\"", "")
            else:
                mess = str(mess).replace("\n", "")
            return res


    def stream_job_logs(self, job_id):
        """
        this function will stream all the prints/logs from the evaluation pod as its running
        I believe it will use prometheus to some effect
        """
        pass

class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)