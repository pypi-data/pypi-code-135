import base64
import logging
import mimetypes
import warnings
from functools import partial
from typing import List, Optional

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from picsellia_connexion_services import JwtServiceConnexion

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.exceptions import ImpossibleAction, NoShadowModel, PicselliaError
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.datalake import Datalake
from picsellia.sdk.dataset import DatasetVersion
from picsellia.sdk.model_version import ModelVersion
from picsellia.sdk.project import Project
from picsellia.sdk.tag import Tag
from picsellia.sdk.taggable import Taggable
from picsellia.types.enums import (
    ContinuousDeploymentPolicy,
    ContinuousTrainingTrigger,
    ContinuousTrainingType,
    ServiceMetrics,
    TagTarget,
)
from picsellia.types.schemas import DeploymentSchema
from picsellia.types.schemas_prediction import PredictionFormat

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Deployment(Dao, Taggable):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)
        Taggable.__init__(self, TagTarget.DEPLOYMENT)

        # Refresh done a second time
        object = self.refresh(data)
        if object.oracle_host is not None:
            try:
                self._oracle_connexion = JwtServiceConnexion(
                    object.oracle_host,
                    {
                        "api_token": self.connexion.api_token,
                        "deployment_id": str(self.id),
                    },
                    login_path="/api/auth/login",
                )
                if self._oracle_connexion.jwt is None:
                    raise PicselliaError("Cannot authenticate to oracle")

                logging.info(
                    "Connected with monitoring service at {}".format(object.oracle_host)
                )
            except Exception as e:
                logger.error(
                    "Could not bind {} with our monitoring service at {} because : {}".format(
                        self, object.oracle_host, e
                    )
                )
                self._oracle_connexion.session.close()
                self._oracle_connexion = None
        else:
            self._oracle_connexion = None

        if object.serving_host is not None:
            try:
                self._serving_connexion = JwtServiceConnexion(
                    object.serving_host,
                    {
                        "api_token": self.connexion.api_token,
                        "deployment_id": str(self.id),
                    },
                    login_path="/api/login",
                )
                if self._serving_connexion.jwt is None:
                    raise PicselliaError("Cannot authenticate to serving")
                logging.info(
                    "Connected with serving service at {}".format(object.serving_host)
                )
            except Exception as e:
                logger.error(
                    "Could not bind {} with our serving service because : {}".format(
                        self, e
                    )
                )
                self._serving_connexion.session.close()
                self._serving_connexion = None
        else:
            self._serving_connexion = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def oracle_connexion(self) -> JwtServiceConnexion:
        assert (
            self._oracle_connexion is not None
        ), "You can't use this function with this deployment. Please contact the support."
        return self._oracle_connexion

    @property
    def serving_connexion(self) -> JwtServiceConnexion:
        assert (
            self._serving_connexion is not None
        ), "You can't use this function with this deployment. Please contact the support."
        return self._serving_connexion

    def __str__(self):
        return "{}Deployment '{}' {} (id: {})".format(
            bcolors.CYAN, self.name, bcolors.ENDC, self.id
        )

    @exception_handler
    @beartype
    def refresh(self, data: dict):
        object = DeploymentSchema(**data)
        self._name = object.name
        return object

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/deployment/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def get_tags(self) -> List[Tag]:
        """Retrieve the tags of your deployment.

        Examples:
            ```python
                tags = deployment.get_tags()
                assert tags[0].name == "cool"
            ```

        Returns:
            List of tags as (Tag)
        """
        r = self.sync()
        return list(map(partial(Tag, self.connexion), r["tags"]))

    @exception_handler
    @beartype
    def retrieve_information(self) -> dict:
        """Retrieve some information about this deployment from service.

        Examples:
            ```python
                print(my_deployment.retrieve_information())
                >>> {

                }
            ```
        """
        return self.oracle_connexion.get(
            path="/api/deployment/{}".format(self.id)
        ).json()

    @exception_handler
    @beartype
    def update(
        self,
        name: str = None,
        active: bool = None,
        target_datalake: Datalake = None,
        min_threshold: float = None,
    ) -> None:
        """Update this deployment with a new name.

        Examples:
            ```python
                a_tag.update(name="new name")
            ```
        """
        payload = {}
        if name is not None:
            payload["name"] = name

        if active is not None:
            payload["active"] = active

        if min_threshold is not None:
            payload["min_threshold"] = min_threshold

        if target_datalake is not None:
            payload["target_datalake_id"] = target_datalake.id

        r = self.connexion.patch(
            "/sdk/deployment/{}".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def delete(self, force_delete: bool = False) -> None:
        self.connexion.delete(
            "/sdk/deployment/{}".format(self.id), params={"force_delete": force_delete}
        )
        logger.info("{} deleted.".format(self))

    @exception_handler
    @beartype
    def set_model(self, model_version: ModelVersion) -> None:
        """Update this deployment with a new name.

        Examples:
            ```python
                a_tag.update(name="new name")
            ```
        """
        payload = {"model_version_id": model_version.id}

        self.connexion.post(
            "/sdk/deployment/{}/model".format(self.id), data=orjson.dumps(payload)
        ).json()
        logger.info("{} model is now {}".format(self, model_version))

    @exception_handler
    @beartype
    def get_model_version(self) -> ModelVersion:
        """Retrieve currently used model version

        Examples:
            ```python
                model_version = deployment.get_model()
            ```

        Returns:
            A (Model) object
        """
        r = self.sync()

        r = self.connexion.get(
            "/sdk/model/version/{}".format(r["model_version_id"])
        ).json()
        return ModelVersion(self.connexion, r)

    @exception_handler
    @beartype
    def set_shadow_model(self, shadow_model_version: ModelVersion) -> None:
        """Update this deployment with a new name.

        Examples:
            ```python
                a_tag.update(name="new name")
            ```
        """
        payload = {"model_version_id": shadow_model_version.id}

        self.connexion.post(
            "/sdk/deployment/{}/shadow".format(self.id), data=orjson.dumps(payload)
        ).json()
        logger.info("{} shadow model is now {}".format(self, shadow_model_version))

    @exception_handler
    @beartype
    def get_shadow_model(self) -> ModelVersion:
        """Retrieve currently used shadow model

        Examples:
            ```python
                shadow_model = deployment.get_shadow_model()
            ```

        Returns:
            A (Model) object
        """
        r = self.sync()
        if "shadow_model_version_id" not in r or r["shadow_model_version_id"] is None:
            raise NoShadowModel("This deployment has no shadow model")

        r = self.connexion.get(
            "/sdk/model/version/{}".format(r["shadow_model_version_id"])
        ).json()
        return ModelVersion(self.connexion, r)

    @exception_handler
    @beartype
    def predict(self, file_path: str) -> dict:
        """Run a prediction on our Serving platform

        Examples:
            ```python
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.predict('my-image.png')
            ```
        Arguments:
            file_path (str): path to the image to predict

        Returns:
            A (dict) with information of the prediction
        """
        with open(file_path, "rb") as file:
            files = {"media": file}
            resp = self.serving_connexion.post(
                path="/api/deployment/{}/predict".format(self.id), files=files
            )

            if resp.status_code != 200:
                raise PicselliaError("Could not predict because {}".format(resp.text))

            return resp.json()

    @exception_handler
    @beartype
    def setup_feedback_loop(self, dataset_version: DatasetVersion) -> None:
        """Setup the Feedback Loop for a Deployment.
        This way, you will be able to attached reviewed predictions to the Dataset.
        This is a great option to increase your training set with quality data.

        Examples:
            ```python
                dataset = client.get_dataset(
                    name="my-dataset",
                    version="latest"
                )
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.setup_feedback_loop(
                    dataset
                )
            ```
        Arguments:
            dataset (Dataset): a connected (Dataset)
        """
        payload = {
            "dataset_version_id": dataset_version.id,
        }
        self.connexion.post(
            "/sdk/deployment/{}/pipeline/fl".format(self.id),
            data=orjson.dumps(payload),
        )
        logger.info(
            "Feedback loop setup for {}\nNow you will be able to add predictions\nto {}".format(
                self, dataset_version
            )
        )

    @exception_handler
    @beartype
    def toggle_feedback_loop(self, active: bool) -> None:
        """Toggle the Feedback Loop for a Deployment.
        This way, you will be able to attached reviewed predictions to the updated Dataset.
        This is a great option to increase your training set with quality data.

        Examples:
            ```python
                dataset = client.get_dataset(
                    name="my-dataset",
                    version="new-version"
                )
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.toggle_feedback_loop(
                    dataset
                )
            ```
        Arguments:
            dataset (Dataset): a connected (Dataset)
        """
        payload = {"active": active}
        self.connexion.put(
            "/sdk/deployment/{}/pipeline/fl".format(self.id),
            data=orjson.dumps(payload),
        )
        logger.info(
            "Feedback loop for {} is now {}".format(
                self, "active" if active else "deactivated"
            )
        )

    @exception_handler
    @beartype
    def setup_continuous_training(
        self,
        project: Project,
        dataset_version: DatasetVersion,
        model_version: ModelVersion,
        trigger: Optional[ContinuousTrainingTrigger] = None,
        threshold: Optional[int] = None,
        experiment_parameters: Optional[dict] = None,
        scan_config: Optional[dict] = None,
    ) -> None:
        """Initilize and activate the continuous training features of picsellia. 🥑
           A Training will be triggered using the configured Dataset
           and Model as base whenever your Deployment pipeline hit the trigger.

            There is 2 types of continuous training different. You can launch a continuous training via Scan configuration or via Experiment
            You need to give wether `experiment_parameters` or `scan_config` but not both

        Examples:
            Let's setup a continuous training pipeline that will be trigger
            every 150 new predictions reviewed by your team.
            We will use the same training parameters as those used when building the first model.

            ```python
                deployment = client.get_deployment("awesome-deploy")
                project = client.get_project(name="my-project")
                dataset_version = project.get_dataset(name="my-dataset").get_version("latest")
                model_version = client.get_model(name="my-model").get_version(0)
                experiment = model_version.get_source_experiment()
                parameters = experiment.get_log('parameters')
                feedback_loop_trigger = 150
                deployment.setup_continuous_training(
                    project, dataset_version, model_version,
                    threshold=150, experiment_parameters=experiment_parameters
                )
            ```
        Arguments:
            project (Project): The project that will host your pipeline.
            dataset_version (DatasetVersion): The Dataset that will be used as training data for your training.
            model_version (ModelVersion):  The exported Model to perform transfert learning from.
            threshold (int): Number of images that need to be review to trigger the training.
            experiment_parameters (Optional[dict], optional):  Training parameters. Defaults to None.
            scan_config (Optional[dict], optional): Scan configuration dict. [more info](https://doc.picsellia.com/docs/initialize-a-scan). Defaults to None.
        """
        payload = {
            "project_id": project.id,
            "dataset_version_id": dataset_version.id,
            "model_version_id": model_version.id,
        }

        if trigger is not None and threshold is not None:
            payload["trigger"] = trigger
            payload["threshold"] = threshold

        if experiment_parameters is not None:
            if scan_config is not None:
                raise PicselliaError(
                    "You cannot give both experiment_parameters and scan_config"
                )
            else:
                payload["training_type"] = ContinuousTrainingType.EXPERIMENT
                payload["experiment_parameters"] = experiment_parameters
        else:
            if scan_config is not None:
                payload["training_type"] = ContinuousTrainingType.SCAN
                payload["scan_config"] = scan_config
            else:
                raise PicselliaError(
                    "You need to give experiment_parameters or scan_config"
                )

        self.connexion.post(
            "/sdk/deployment/{}/pipeline/ct".format(self.id),
            data=orjson.dumps(payload),
        )
        logger.info("Continuous training setup for {}\n".format(self))

    @exception_handler
    @beartype
    def toggle_continuous_training(self, active: bool) -> None:
        """Update your continuous training pipeline.

        Examples:
            ```python
                deployment = client.get_deployment("awesome-deploy")
                deployment.update_continuous_training(active=False)
            ```
        """
        payload = {"active": active}
        self.connexion.put(
            "/sdk/deployment/{}/pipeline/ct".format(self.id),
            data=orjson.dumps(payload),
        )
        logger.info(
            "Continuous training for {} is now {}".format(
                self, "active" if active else "deactivated"
            )
        )

    @exception_handler
    @beartype
    def setup_continuous_deployment(self, policy: ContinuousDeploymentPolicy) -> None:
        """Setup the continuous deployment for this pipeline

        Examples:
            ```python
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.setup_continuous_deployment(ContinuousDeploymentPolicy.DEPLOY_MANUAL)
            ```
        Arguments:
            policy (ContinuousDeploymentPolicy): policy to use
        """
        payload = {"policy": policy}
        self.connexion.post(
            "/sdk/deployment/{}/pipeline/cd".format(self.id),
            data=orjson.dumps(payload),
        )
        logger.info(
            "Continuous deployment setup for {} with policy {}\n".format(self, policy)
        )

    @exception_handler
    @beartype
    def toggle_continuous_deployment(self, active: bool) -> None:
        """Toggle continuous deployment for this deployment

        Examples:
            ```python
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.toggle_continuous_deployment(
                    dataset
                )
            ```
        Arguments:
            dataset (Dataset): a connected (Dataset)
        """
        payload = {"active": active}
        self.connexion.put(
            "/sdk/deployment/{}/pipeline/cd".format(self.id),
            data=orjson.dumps(payload),
        )
        logger.info(
            "Continuous deployment for {} is now {}".format(
                self, "active" if active else "deactivated"
            )
        )

    @exception_handler
    @beartype
    def get_stats(
        self,
        service: ServiceMetrics,
        model_version: ModelVersion = None,
        from_timestamp: float = None,
        to_timestamp: float = None,
        since: int = None,
        includes: List[str] = None,
        excludes: List[str] = None,
        tags: List[str] = None,
    ) -> dict:
        """Retrieve stats of this deployment stored in Picsellia environment.

        Mandatory param is "service" an enum of type ServiceMetrics. Values possibles are :
            PREDICTIONS_OUTLYING_SCORE
            PREDICTIONS_DATA
            REVIEWS_OBJECT_DETECTION_STATS
            REVIEWS_CLASSIFICATION_STATS
            REVIEWS_LABEL_DISTRIBUTION_STATS

            AGGREGATED_LABEL_DISTRIBUTION
            AGGREGATED_OBJECT_DETECTION_STATS
            AGGREGATED_PREDICTIONS_DATA
            AGGREGATED_DRIFTING_PREDICTIONS

        For aggregation, computation may not have been done by the past.
        You will need to force computation of these aggregations and retrieve them again.


        Examples:
            ```python
                my_deployment.get_stats(ServiceMetrics.PREDICTIONS_DATA)
                my_deployment.get_stats(ServiceMetrics.AGGREGATED_DRIFTING_PREDICTIONS, since=3600)
                my_deployment.get_stats(ServiceMetrics.AGGREGATED_LABEL_DISTRIBUTION, model_id=1239012)

            ```
        Arguments:
            service (str): service queried
            model (Model, optional): Model that shall be used when retrieving data. Defaults to None.
            from_timestamp (float, optional): System will only retrieve prediction data after this timestamp. Defaults to None.
            to_timestamp (float, optional): System will only retrieve prediction data before this timestamp. Defaults to None.
            since (int, optional): System will only retrieve prediction data that are in the last seconds given by this value. Defaults to None.
            includes (List[str], optional): Research will includes these ids and excludes others. Defaults to None.
            excludes (List[str], optional): Research will excludes these ids. Defaults to None.
            tags (str, optional): Research will be done filtering by tags. Defaults to None.
                                  tags need to be parsable like "tag1:value,tag2:value2"

        Returns:
            A dict with queried statistics about the service you asked
        """
        filter = self._build_filter(
            service=service.service,
            model_version=model_version,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            since=since,
            includes=includes,
            excludes=excludes,
            tags=tags,
        )

        if service.is_aggregation:
            resp = self.oracle_connexion.get(
                path="/api/deployment/{}/stats".format(self.id), params=filter
            ).json()
            if "infos" in resp and "info" in resp["infos"]:
                logger.info("This computation is outdated or has never been done.")
                logger.info(
                    "You can compute it again by calling launch_computation with exactly the same params."
                )
            return resp
        else:
            return self.oracle_connexion.get(
                path="/api/deployment/{}/predictions/stats".format(self.id),
                params=filter,
            ).json()

    def _build_filter(
        self,
        service: str,
        model_version: ModelVersion = None,
        from_timestamp: float = None,
        to_timestamp: float = None,
        since: int = None,
        includes: List[str] = None,
        excludes: List[str] = None,
        tags: List[str] = None,
    ) -> dict:

        filter = {"service": service}

        if model_version is not None:
            filter["model_id"] = model_version.id

        if from_timestamp is not None:
            filter["from_timestamp"] = from_timestamp

        if to_timestamp is not None:
            filter["to_timestamp"] = to_timestamp

        if since is not None:
            filter["since"] = since

        if includes is not None:
            filter["includes"] = includes

        if excludes is not None:
            filter["excludes"] = excludes

        if tags is not None:
            filter["tags"] = tags

        return filter

    @exception_handler
    @beartype
    def monitor(
        self,
        image_path: str,
        latency: float,
        height: int,
        width: int,
        prediction: PredictionFormat,
        source: str = None,
        tags: List[str] = None,
        timestamp: float = None,
        model_version: ModelVersion = None,
        shadow_model_version: ModelVersion = None,
        shadow_latency: float = None,
        shadow_raw_predictions: PredictionFormat = None,
    ) -> dict:
        with open(image_path, "rb") as img_file:
            content_type = mimetypes.guess_type(image_path, strict=False)[0]
            if content_type is None:  # pragma: no cover
                content_type = "image/jpeg"
            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            filename = image_path.split("/")[-1]

        if model_version is None:
            model_version = self.get_model_version()

        if prediction.model_type != model_version.type:
            raise PicselliaError(
                "Prediction shape of this type {} cannot be used with this model {}".format(
                    prediction.model_type, model_version.type
                )
            )

        payload = {
            "filename": filename,
            "content_type": content_type,
            "height": height,
            "width": width,
            "image": encoded_image,
            "raw_predictions": prediction.dict(),
            "latency": latency,
            "model_type": model_version.type,
            "model": model_version.id,
        }

        if source is not None:
            payload["source"] = source

        if tags is not None:
            payload["tags"] = tags

        if timestamp is not None:
            payload["timestamp"] = timestamp

        if shadow_raw_predictions is not None:
            if shadow_model_version is None:
                shadow_model_version = self.get_shadow_model()

            if shadow_latency is None:
                raise ImpossibleAction(
                    "Shadow latency and shadow raw predictions shall be defined if you want to push a shadow model result"
                )
            payload["shadow_model"] = shadow_model_version.id
            payload["shadow_latency"] = shadow_latency
            payload["shadow_raw_predictions"] = shadow_raw_predictions.dict()

        resp = self.oracle_connexion.post(
            path="/api/deployment/{}/predictions".format(self.id),
            data=orjson.dumps(payload),
        )

        if resp.status_code != 201:
            raise PicselliaError("Something went wrong: {}".format(resp.status_code))

        return resp.json()
