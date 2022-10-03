import logging
import os

from beartype import beartype

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.schemas import ModelFileSchema

logger = logging.getLogger("picsellia")


class ModelFile(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    @property
    def name(self) -> str:
        return self._name

    @property
    def object_name(self) -> str:
        return self._object_name

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def large(self) -> bool:
        return self._large

    def __str__(self):
        return "{}Model file named '{}'{} (id: {})".format(
            bcolors.BLUE,
            self.name,
            bcolors.ENDC,
            self.id,
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/model/file/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> ModelFileSchema:
        object = ModelFileSchema(**data)
        self._name = object.name
        self._object_name = object.object_name
        self._filename = object.filename
        self._large = object.large
        return object

    @exception_handler
    @beartype
    def download(self, target_path: str = "./", force_replace: bool = False) -> None:
        """Download file stored.

        Examples:
            ```python
                latest_cp = model.get_file("model-latest")
                latest_cp.download("./files/")
            ```
        Arguments:
            dir_path (str): Directory path where file will be downloaded
        """
        self.sync()
        path = os.path.join(target_path, self.filename)
        if self.connexion.download_file(
            self.object_name, path, self.large, force_replace=force_replace
        ):
            logger.info("{} downloaded successfully".format(self.filename))
        else:  # pragma: no cover
            logger.warning("Did not download file '{}'".format(self.filename))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this file

        Examples:
            ```python
                model_file.delete()
            ```
        """
        self.connexion.delete("/sdk/model/file/{}".format(self.id))
        logger.info("{} deleted from platform.".format(self))
