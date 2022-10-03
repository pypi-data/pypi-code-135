import logging
import os
import warnings

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.schemas import ScanFileSchema
from picsellia.utils import filter_payload

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class ScanFile(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    def __str__(self):
        return "{}ScanFile {}{} (id: {})".format(
            bcolors.GREEN, self.name, bcolors.ENDC, self.id
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def object_name(self) -> str:
        return self._object_name

    @property
    def large(self) -> bool:
        return self._large

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> ScanFileSchema:
        object = ScanFileSchema(**data)
        self._name = object.name
        self._object_name = object.object_name
        self._large = object.large
        return object

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/scan/file/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def update(
        self,
        name: str = None,
        object_name: str = None,
        large: bool = None,
    ) -> None:
        """Update this scan file.

        Examples:
            ```python
                script.update(object_name="another-path-to-script")
            ```
        """
        payload = {
            "name": name,
            "object_name": object_name,
            "large": large,
        }
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            "/sdk/scan/file/{}".format(self.id), data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this scan file

        Examples:
            ```python
                script.delete()
            ```
        """
        self.connexion.delete("/sdk/scan/file/{}".format(self.id))

    @exception_handler
    @beartype
    def download(self, target_path: str = "./", force_replace: bool = False) -> None:
        """Download an experiment's artifact to a given target_path.

        Examples:
            ```python
                script.download("myDir")
                file_list = os.path.listdir("myDir")
                print(file_list)
                >>> ["saved_model.zip"]
            ```
        Arguments:
            target_path (str, optional): Path to download the file to, default to cwd. Defaults to './'.

        """
        self.sync()
        path = os.path.join(target_path, self.name)
        if self.connexion.download_file(
            self.object_name, path, self.large, force_replace=force_replace
        ):
            logger.info("{} downloaded successfully".format(self.name))
        else:
            logger.error("Did not download file '{}'".format(self.name))
