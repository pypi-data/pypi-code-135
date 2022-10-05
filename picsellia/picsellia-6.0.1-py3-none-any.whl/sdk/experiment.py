import logging
import os
from functools import partial
from typing import Any, Dict, List, Optional, Tuple, Union

import orjson
from beartype import beartype

from picsellia import exceptions, utils
from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.artifact import Artifact
from picsellia.sdk.asset import Asset
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.dataset_version import DatasetVersion
from picsellia.sdk.label import Label
from picsellia.sdk.log import Log, LogType
from picsellia.sdk.model_version import ModelVersion
from picsellia.types.enums import ExperimentStatus, JobStatus, ObjectDataType
from picsellia.types.schemas import ExperimentSchema, LogDataType

logger = logging.getLogger("picsellia")


class Experiment(Dao):
    def __init__(self, connexion: Connexion, data: dict) -> None:
        Dao.__init__(self, connexion, data)

    @property
    def name(self) -> str:
        return self._name

    @property
    def status(self) -> ExperimentStatus:
        return self._status

    def __str__(self):
        return "{}Experiment '{}' {} (id: {})".format(
            bcolors.BLUE, self.name, bcolors.ENDC, self.id
        )

    @property
    def base_dir(self):
        return self.name

    @property
    def metrics_dir(self):
        return os.path.join(self.base_dir, "metrics")

    @property
    def png_dir(self):
        return os.path.join(self.base_dir, "images")

    @property
    def checkpoint_dir(self):
        return os.path.join(self.base_dir, "checkpoint")

    @property
    def record_dir(self):
        return os.path.join(self.base_dir, "records")

    @property
    def config_dir(self):
        return os.path.join(self.base_dir, "config")

    @property
    def results_dir(self):
        return os.path.join(self.base_dir, "results")

    @property
    def exported_model_dir(self):
        return os.path.join(self.base_dir, "exported_model")

    @exception_handler
    @beartype
    def get_resource_url_on_platform(self) -> str:
        """Get platform url of this resource.

        Examples:
            ```python
                print(foo_dataset.get_resource_url_on_platform())
                >>> https://app.picsellia.com/experiment/62cffb84-b92c-450c-bc37-8c4dd4d0f590
            ```

        Returns:
            Url on Platform for this resource
        """

        return "{}/experiment/{}".format(self.connexion.host, self.id)

    @exception_handler
    @beartype
    def refresh(self, data: dict):
        object = ExperimentSchema(**data)
        self._name = object.name
        self._status = object.status
        return object

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/experiment/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def update(
        self,
        name: str = None,
        description: str = None,
        base_experiment: "Experiment" = None,
        base_model_version: "ModelVersion" = None,
        status: ExperimentStatus = None,
    ) -> None:
        """Update this experiment with a given name, description or a base experiment or a base model version.

        Examples:
            ```python
                my_experiment.update(description="First try Yolov5")
            ```
        """
        payload = {"name": name, "description": description, "status": status}

        if base_experiment is not None:
            payload["base_experiment_id"] = base_experiment.id

        if base_model_version is not None:
            payload["base_model_id"] = base_model_version.id

        filtered_payload = utils.filter_payload(payload)
        r = self.connexion.patch(
            "/sdk/experiment/{}".format(self.id), data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this experiment.

        Examples:
            ```python
                my_experiment.delete()
            ```
        """
        self.connexion.delete("/sdk/experiment/{}".format(self.id))

    @exception_handler
    @beartype
    def list_artifacts(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
    ) -> List[Artifact]:
        """List artifacts stored in the experiment.

        Examples:
            ```python
                artifacts = my_experiment.list_artifacts()
            ```

        Returns:
            A list of artifact objects that you can manipulate
        """
        params = {"limit": limit, "offset": offset, "order_by": order_by}
        params = utils.filter_payload(params)
        r = self.connexion.get(
            "/sdk/experiment/{}/artifacts".format(self.id), params=params
        ).json()
        return list(map(partial(Artifact, self.connexion), r["items"]))

    @exception_handler
    @beartype
    def delete_all_artifacts(self) -> None:
        """Delete all stored artifacts for experiment

        :warning: **DANGER ZONE**: This will definitely remove the artifacts from our servers

        Examples:
            ```python
                experiment.delete_all_artifacts()
            ```
        """
        payload = ["__all__"]
        self.connexion.delete(
            "/sdk/experiment/{}/artifacts".format(self.id), data=orjson.dumps(payload)
        )

    @exception_handler
    @beartype
    def create_artifact(
        self, name: str, filename: str, object_name: str, large: bool = False
    ) -> Artifact:
        """Create an artifact for this experiment.

        Examples:
            ```python
                self.create_artifact(name="a_file", filename="file.png", object_name="some_file_in_s3.png", large=False)
            ```
        Arguments:
            name (str): name of the artifact.
            filename (str): filename.
            object_name (str): s3 object name.
            large (bool, optional): >5Mb or not. Defaults to False.

        Returns:
            An artifact object
        """
        payload = {
            "name": name,
            "filename": filename,
            "object_name": object_name,
            "large": large,
        }
        r = self.connexion.post(
            "/sdk/experiment/{}/artifacts".format(self.id), data=orjson.dumps(payload)
        ).json()
        return Artifact(self.connexion, r)

    @exception_handler
    @beartype
    def _create_or_update_file(
        self, name: str, filename: str, object_name: str, large: bool
    ) -> Artifact:
        try:
            stored = self.get_artifact(name)
            stored.update(
                name=name, filename=filename, object_name=object_name, large=large
            )
            return stored
        except exceptions.ResourceNotFoundError:
            return self.create_artifact(
                name=name, filename=filename, object_name=object_name, large=large
            )

    @exception_handler
    @beartype
    def store(self, name: str, path: str = None, zip: bool = False) -> Artifact:
        """Store an artifact and attach it to the experiment.

        Examples:
            ```python
                # Zip and store a folder as an artifact for the experiment
                # you can choose an arbitrary name or refer to our 'namespace'
                # for certain artifacts to have a custom behavior

                trained_model_path = "my_experiment/saved_model"
                experiment.store("model-latest", trained_model_path, zip=True)
            ```
        Arguments:
            name (str): name for the artifact. Defaults to "".
            path (str): path to the file or folder. Defaults to None.
            zip (bool, optional): Whether or not to compress the file to a zip file. Defaults to False.

        Raises:
            FileNotFoundException: No file found at the given path
        """
        if path is None:  # pragma: no cover
            return self.store_local_artifact(name)

        if zip:
            path = utils.zipdir(path)

        filename = os.path.split(path)[-1]
        object_name = self.connexion.generate_experiment_object_name(
            filename, ObjectDataType.ARTIFACT, self.id
        )
        _, is_large, _ = self.connexion.upload_file(object_name, path)

        return self._create_or_update_file(
            name=name, filename=filename, object_name=object_name, large=is_large
        )

    @exception_handler
    @beartype
    def store_local_artifact(self, name: str) -> Artifact:  # pragma: no cover
        """Store an artifact in platform that is locally stored

        This artifact shall have the name: config, checkpoint-data-latest, checkpoint-index-latest or model-latest

        It will look for special file into current directory.

        Examples:
            ```python
                my_experiment.store_local_artifact("model-latest")
            ```
        Arguments:
            name (str): Name of the artifact to store

        Returns:
            An (Artifact) object
        """
        assert (
            name == "config"
            or name == "checkpoint-data-latest"
            or name == "checkpoint-index-latest"
            or name == "model-latest"
        ), "This name cannot be used to store an artifact"

        if name == "config":
            filename = "pipeline.config"
            path = os.path.join(self.config_dir, filename)
            if not os.path.isfile(path):
                raise exceptions.FileNotFoundException("No config file found")

        elif name == "checkpoint-data-latest":
            file_list = os.listdir(self.checkpoint_dir)
            ckpt_id = max(
                [int(p.split("-")[1].split(".")[0]) for p in file_list if "index" in p]
            )
            filename = None
            for f in file_list:
                if "{}.data".format(ckpt_id) in f:
                    filename = f
                    break
            if filename is None:
                raise exceptions.ResourceNotFoundError(
                    "Could not find matching data file with index"
                )
            path = os.path.join(self.checkpoint_dir, filename)

        elif name == "checkpoint-index-latest":
            file_list = os.listdir(self.checkpoint_dir)
            ckpt_id = max(
                [int(p.split("-")[1].split(".")[0]) for p in file_list if "index" in p]
            )
            filename = "ckpt-{}.index".format(ckpt_id)
            path = os.path.join(self.checkpoint_dir, filename)

        elif name == "model-latest":  # pragma: no cover
            file_path = os.path.join(self.exported_model_dir, "saved_model")
            path = utils.zipdir(file_path)
            filename = "saved_model.zip"

        else:
            raise RuntimeError("unreachable code")

        object_name = self.connexion.generate_experiment_object_name(
            filename, ObjectDataType.ARTIFACT, self.id
        )
        _, is_large, _ = self.connexion.upload_file(object_name, path)

        return self._create_or_update_file(
            name=name, filename=filename, object_name=object_name, large=is_large
        )

    @exception_handler
    @beartype
    def get_base_model_version(self) -> ModelVersion:
        """Retrieve the base model of this experiment.

        Examples:
            ```python
                model_version = experiment.get_base_model_version()
            ```

        Returns:
            A (ModelVersion) object representing the base model.
        """
        r = self.sync()
        if r["base_model_version_id"] is None:
            raise exceptions.NoBaseModelVersionError(
                "There is no base model for this experiment."
            )
        r = self.connexion.get(
            "/sdk/model/version/{}".format(r["base_model_version_id"])
        ).json()
        return ModelVersion(self.connexion, r)

    @exception_handler
    @beartype
    def get_base_experiment(self) -> "Experiment":
        """Retrieve the base experiment of this experiment.

        Examples:
            ```python
                previous = experiment.get_base_experiment()
            ```

        Returns:
            An (Experiment) object representing the base experiment.
        """
        r = self.sync()
        if r["base_experiment_id"] is None:
            raise exceptions.NoBaseExperimentError(
                "There is no base experiment for this experiment"
            )
        r = self.connexion.get(
            "/sdk/experiment/{}".format(r["base_experiment_id"])
        ).json()
        return Experiment(self.connexion, r)

    @exception_handler
    @beartype
    def get_artifact(self, name: str) -> Artifact:
        """Retrieve an artifact information.

        Examples:
            ```python
                model_artifact = experiment.get_artifact("model-latest")
                assert model_artifact.name == "model-latest"
                assert model_artifact.object_name == "d67924a0-7757-48ed-bf7a-322b745e917e/saved_model.zip"
            ```
        Arguments:
            name (str): Name of the artifact to retrieve

        Returns:
            An (Artifact) object
        """
        params = {"name": name}
        r = self.connexion.get(
            "/sdk/experiment/{}/artifacts/find".format(self.id), params=params
        ).json()
        return Artifact(self.connexion, r)

    @exception_handler
    @beartype
    def list_logs(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
    ) -> list:
        """List everything that has been logged.

        List everything that has been logged to an experiment using the .log() method.

        Examples:
            ```python
                logs = experiment.list_logs()
                assert logs[0].type == LogType.Table
                assert logs[0].data == {"batch_size":4, "epochs":1000 }
            ```

        Returns:
            A list of (Log) objects
        """
        params = {"limit": limit, "offset": offset, "order_by": order_by}
        params = utils.filter_payload(params)
        r = self.connexion.get(
            "/sdk/experiment/{}/logs/extended".format(self.id), params=params
        ).json()
        return list(map(partial(Log, self.connexion), r["items"]))

    @exception_handler
    @beartype
    def delete_all_logs(self) -> None:
        """Delete everything that has been logged.

        Delete everything that has been logged (using .log()) into this experiment  method.

        Examples:
            ```python
                experiment.delete_all_logs()
            ```
        """
        payload = ["__all__"]
        self.connexion.delete(
            "/sdk/experiment/{}/logs".format(self.id), data=orjson.dumps(payload)
        )

    @exception_handler
    @beartype
    def create_log(
        self, name: str, data: LogDataType, type: Union[LogType, str]
    ) -> Log:
        """Create a (Log) object in a experiment.

        Arguments:
            name (str): Name of data.
            data (dict, int, str, float): Data content.
            type (LogType): Type of data.
        """
        payload = {"name": name, "data": data, "type": type}
        r = self.connexion.post(
            "/sdk/experiment/{}/logs".format(self.id), data=orjson.dumps(payload)
        ).json()
        return Log(self.connexion, r)

    @exception_handler
    @beartype
    def get_log(self, name: str) -> Log:
        """Get data for a given log in this experiment

        Examples:
            ```python
                parameters = experiment.get_log("parameters")
                assert log.parameters == { "batch_size":4, "epochs":1000 }
            ```
        Arguments:
            name (str): name of the log to retrieve

        Returns:
            A (Log) object
        """
        params = {"name": name}
        r = self.connexion.get(
            "/sdk/experiment/{}/logs/find".format(self.id), params=params
        ).json()
        return Log(self.connexion, r)

    @exception_handler
    @beartype
    def log(
        self,
        name: str,
        data: LogDataType,
        type: Union[LogType, str] = None,
        replace: bool = False,
    ) -> Log:
        """Record some data in an experiment.

        Record something to an experiment.
        It will then be saved and displayed.

        Examples:
            ```python
                parameters = {
                    "batch_size":4,
                    "epochs":1000
                }
                exp.log("parameters", parameters, type=LogType.TABLE)
            ```
        Arguments:
            name (str): Name of the log.
            data (Any): Data to be saved.
            type (LogType, optional): Type of the data to log.
                                  This will condition how it is displayed in the experiment dashboard. Defaults to None.
            replace (bool, optional): Whether to replace the current value of the log. Defaults to False.

        Raises:
            Exception: Impossible to upload the file when logging an image.
        """
        if isinstance(type, str):
            try:
                type = LogType[type.upper()]
            except Exception:
                raise exceptions.PicselliaError(
                    "The Log Type you provided is not included in our supported types."
                )
        try:
            log: Log = self.get_log(name)
        except exceptions.ResourceNotFoundError:
            assert (
                type is not None
            ), "Please specify a type for your data vizualization, check the docs to see all available types"
            log = None

        if type == LogType.IMAGE:
            object_name = self.connexion.generate_experiment_object_name(
                data, ObjectDataType.LOG_IMAGE, self.id
            )
            _, large, _ = self.connexion.upload_file(object_name, data)
            data = {
                "object_name": object_name,
                "large": large,
                "filename": data,
                "name": data,
            }

        if log is None:
            log = self.create_log(name, data=data, type=type)
        elif replace or (type != LogType.LINE and type != "LINE"):
            log.update(data=data)
        else:  # Case: LogType == Line
            log.append(data=data)
        return log

    @exception_handler
    @beartype
    def send_logging(
        self,
        log: Union[str, list],
        part: str,
        final: bool = False,
        special: Union[str, bool, list] = False,
    ) -> None:
        """Send a logging experiment to the experiment .

        Arguments:
            log (str): Log content
            part (str): Logging Part
            final (bool, optional): True if Final line. Defaults to False.
            special (bool, optional): True if special log. Defaults to False.
        """
        if not hasattr(self, "line_nb"):
            self.line_nb = 0

        to_send = {
            "line_nb": self.line_nb,
            "log": log,
            "final": final,
            "part": part,
            "special": special,
        }
        self.line_nb += 1
        self.connexion.post(
            "/sdk/experiment/{}/logging".format(self.id),
            data=orjson.dumps(to_send),
        )

    @exception_handler
    @beartype
    def start_logging_chapter(self, name: str) -> None:
        """Print a log entry to the log .

        Arguments:
            name (str): Chapter name
        """
        utils.print_start_chapter_name(name)

    @exception_handler
    @beartype
    def start_logging_buffer(self, length: int = 1) -> None:
        """Start logging buffer .

        Arguments:
            length (int, optional): Buffer length. Defaults to 1.
        """
        utils.print_logging_buffer(length)
        self.buffer_length = length

    @exception_handler
    @beartype
    def end_logging_buffer(self) -> None:
        """End the logging buffer ."""
        utils.print_logging_buffer(self.buffer_length)

    @exception_handler
    @beartype
    def update_job_status(self, status: JobStatus) -> None:
        """Update the job status.

        Arguments:
            status (JobStatus): Status to send
        """
        to_send = {
            "status": status,
        }
        self.connexion.patch(
            "/sdk/experiment/{}/job/status".format(self.id),
            data=orjson.dumps(to_send),
        )

    @exception_handler
    @beartype
    def publish(self, name: str) -> ModelVersion:
        """Publish an Experiment as a Model to your registry.

        Examples:
            ```python
                model = experiment.publish("awesome-model")
                model.update(framework="tensorflow")
            ```
        Arguments:
            name (str): Target Name for the model in the registry.

        Returns:
            A (Model) just created from the experiment
        """
        payload = {"name": name}
        r = self.connexion.post(
            "/sdk/experiment/{}/publish".format(self.id), data=orjson.dumps(payload)
        ).json()
        model = ModelVersion(self.connexion, r)
        logger.info("Experiment published as {}".format(model))
        return model

    @exception_handler
    @beartype
    def launch(self, gpus: int = 1) -> None:
        """Launch a job on a remote environment with this experiment.

        :information-source: The remote environment has to be setup prior launching the experiment.
        It defaults to our remote training engine.

        Examples:
            ```python
                experiment.launch()
            ```
        Arguments:
            gpus (int, optional): Number of GPU to use for the training. Defaults to 1.
        """
        payload = {
            "gpus": gpus,
        }

        self.connexion.post(
            "/sdk/experiment/{}/launch".format(self.id), data=orjson.dumps(payload)
        )
        logger.info("Job launched successfully")

    def _setup_dirs(self):
        """Create the directories for the project."""
        if not os.path.isdir(self.name):
            logger.debug(
                "No directory for this project has been found, creating directory and sub-directories..."
            )
            os.mkdir(self.name)

        self._create_dir(self.base_dir)
        self._create_dir(self.png_dir)
        self._create_dir(self.checkpoint_dir)
        self._create_dir(self.metrics_dir)
        self._create_dir(self.record_dir)
        self._create_dir(self.config_dir)
        self._create_dir(self.results_dir)
        self._create_dir(self.exported_model_dir)

    @exception_handler
    @beartype
    def _create_dir(self, dir_name: str) -> None:
        """Create a directory if it doesn t exist.

        Arguments:
            dir_name (str): [directory name]
        """
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

    @exception_handler
    @beartype
    def download_artifacts(self, with_tree: bool):
        if with_tree:
            self._setup_dirs()
            self._download_artifacts_with_tree_for_experiment()
        else:
            self._download_artifacts_without_tree_for_experiment()

    @exception_handler
    @beartype
    def _download_artifacts_with_tree_for_experiment(self):
        for artifact in self.list_artifacts():
            if artifact.name == "checkpoint-data-latest":  # pragma: no cover
                target_path = self.checkpoint_dir
            elif artifact.name == "checkpoint-index-latest":  # pragma: no cover
                target_path = self.checkpoint_dir
            elif artifact.name == "model-latest":  # pragma: no cover
                target_path = self.exported_model_dir
            elif artifact.name == "config":  # pragma: no cover
                target_path = self.config_dir
            else:
                target_path = self.base_dir

            artifact.download(target_path=target_path, force_replace=True)

    @exception_handler
    @beartype
    def _download_artifacts_without_tree_for_experiment(self):
        self._create_dir(self.base_dir)
        for artifact in self.list_artifacts():
            artifact.download(target_path=self.base_dir, force_replace=True)

    @exception_handler
    @beartype
    def attach_model_version(self, model_version: ModelVersion) -> None:
        """Attach model version to this experiment.
        There is only one model version attached to an experiment

        Examples:
            ```python
                foo_model = client.get_model("foo").get_version(3)
                my_experiment.attach_model_version(foo_model)
            ```
        Arguments:
            model_version (ModelVersion): A model version to attach to the experiment.
        """
        payload = {"model_version_id": model_version.id}
        self.connexion.post(
            "/sdk/experiment/{}/model".format(self.id), data=orjson.dumps(payload)
        )
        logger.info("{} successfully attached to {}".format(model_version, self))

    @exception_handler
    @beartype
    def attach_dataset(self, name: str, dataset_version: DatasetVersion) -> None:
        """Attach a dataset version to this experiment.

        Retrieve or create a dataset version and attach it to this experiment.

        Examples:
            ```python
                foo_dataset = client.get_dataset("foo").get_version("first")
                my_experiment.attach_dataset(foo_dataset)
            ```
        Arguments:
            dataset_version (DatasetVersion): A dataset version to attach to the experiment.
        """
        payload = {"name": name, "dataset_version_id": dataset_version.id}
        self.connexion.post(
            "/sdk/experiment/{}/datasets".format(self.id), data=orjson.dumps(payload)
        )
        logger.info("{} successfully attached to {}".format(dataset_version, self))

    @exception_handler
    @beartype
    def detach_dataset(self, dataset_version: DatasetVersion) -> None:
        """Detach a dataset version from this experiment.

        Examples:
            ```python
                foo_dataset = client.get_dataset("foo").get_version("first")
                my_experiment.attach_dataset(foo_dataset)
                my_experiment.detach_dataset(foo_dataset)
            ```
        Arguments:
            dataset_version (DatasetVersion): A dataset version to attach to the experiment.
        """
        payload = [dataset_version.id]
        self.connexion.delete(
            "/sdk/experiment/{}/datasets".format(self.id), data=orjson.dumps(payload)
        )
        logger.info(
            "{} was successfully detached from {}".format(dataset_version, self)
        )

    @exception_handler
    @beartype
    def list_attached_dataset_versions(self) -> List[DatasetVersion]:
        """Retrieve all dataset versions attached to this experiment

        Examples:
            ```python
            datasets = my_experiment.list_attached_dataset_versions()
            ```

        Returns:
            A list of (DatasetVersion) object attached to this experiment
        """
        r = self.connexion.get("/sdk/experiment/{}/datasets".format(self.id)).json()
        return list(
            map(
                lambda item: DatasetVersion(self.connexion, item["dataset_version"]),
                r["items"],
            )
        )

    @exception_handler
    @beartype
    def get_dataset(self, name: str) -> DatasetVersion:
        """Retrieve the dataset version attached to this experiment with given name

        Examples:
            ```python
            dataset: DatasetVersion = my_experiment.get_dataset('train')
            pics = dataset.list_assets()
            annotations = dataset.list_annotations()
            ```

        Returns:
            A (DatasetVersion) object attached to this experiment
        """
        params = {"name": name}
        r = self.connexion.get(
            "/sdk/experiment/{}/datasets/find".format(self.id), params=params
        ).json()
        return DatasetVersion(self.connexion, r["dataset_version"])

    @exception_handler
    @beartype
    def run_train_test_split_on_dataset(
        self, name: str, prop: float = 0.8, random_seed: Any = None
    ) -> Tuple[
        List[Asset], List[Asset], Dict[Label, int], Dict[Label, int], List[Label]
    ]:
        """Retrieve the dataset version attached to this experiment with given name

        Examples:
            ```python
            dataset: DatasetVersion = my_experiment.get_dataset('train')
            pics = dataset.list_assets()
            annotations = dataset.list_annotations()
            ```

        Returns:
            A (DatasetVersion) object attached to this experiment
        """
        dataset = self.get_dataset(name)
        (
            train_assets,
            eval_assets,
            train_label_count,
            eval_label_count,
            labels,
        ) = dataset.train_test_split(prop, random_seed)
        # TODO: Log those values
        return train_assets, eval_assets, train_label_count, eval_label_count, labels
