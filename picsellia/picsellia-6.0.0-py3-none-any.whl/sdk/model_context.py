import logging
from uuid import UUID

from beartype import beartype

import picsellia.exceptions as exceptions
from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.dataset_version import DatasetVersion
from picsellia.types.schemas import ModelContextSchema

logger = logging.getLogger("picsellia")


class ModelContext(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    @property
    def experiment_id(self) -> UUID:
        return self._experiment_id

    @property
    def datasets(self) -> list:
        return self._datasets

    @property
    def parameters(self) -> dict:
        return self._parameters

    def __str__(self):
        return "A {}model context{} (id: {})".format(
            bcolors.BLUE, bcolors.ENDC, self.id
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/model/context/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> ModelContextSchema:
        object = ModelContextSchema(**data)
        self._experiment_id = object.experiment_id
        self._datasets = object.datas
        self._parameters = object.parameters
        return object

    @exception_handler
    @beartype
    def get_infos(self) -> dict:
        """Retrieve some infos about this context

        Examples:
            ```python
                get_infos()
            ```

        Returns:
            A (dict) with some infos
        """
        return {
            "experiment": self.experiment_id,
            "datasets": self.datasets,
            "parameters": self.parameters,
        }

    @exception_handler
    @beartype
    def retrieve_experiment(self):
        """Retrieve source experiment of this context

        It will raise an exception if this context has no experiment source

        Examples:
            ```python
                exp = model_context.retrieve_experiment()
            ```

        Returns:
            An (Experiment) object
        """
        if self.experiment_id is None:
            raise exceptions.ContextSourceNotDefined(
                "This context has no experiment source"
            )

        from experiment import Experiment

        r = self.connexion.get("/sdk/experiment/{}".format(self.experiment_id)).json()
        return Experiment(self.connexion, r)

    @exception_handler
    @beartype
    def retrieve_datasets(self):
        """Retrieve datasets used to train and evaluate (or else) the model

        It will raise an exception if this context has no data

        Examples:
            ```python
                dataset_versions = model_context.retrieve_datasets()
            ```

        Returns:
            A list of (DatasetVersion) objects
        """
        if self.datasets is None or self.datasets == []:
            raise exceptions.ContextSourceNotDefined("This context has no data")

        datasets = []
        for dataset_version in self.datasets:
            r = self.connexion.get(
                "/sdk/dataset/version/{}".format(dataset_version.version_id)
            ).json()
            datasets.append(DatasetVersion(self.connexion, r))
        return datasets
