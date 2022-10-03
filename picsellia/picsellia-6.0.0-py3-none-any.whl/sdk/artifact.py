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
from picsellia.types.schemas import ArtifactSchema
from picsellia.utils import filter_payload

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Artifact(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    def __str__(self):
        return "{}Artifact {}{} (id: {})".format(
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

    @property
    def filename(self) -> str:
        return self._filename

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> ArtifactSchema:
        object = ArtifactSchema(**data)
        self._name = object.name
        self._object_name = object.object_name
        self._large = object.large
        self._filename = object.filename
        return object

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/artifact/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def update(
        self,
        name: str = None,
        filename: str = None,
        object_name: str = None,
        large: bool = None,
    ) -> None:
        """Update this artifact.

        Examples:
            ```python
                this_artifact.update(object_name="another-path-to-artifact")
            ```
        """
        payload = {
            "name": name,
            "filename": filename,
            "object_name": object_name,
            "large": large,
        }
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            "/sdk/artifact/{}".format(self.id), data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this artifact

        Examples:
            ```python
                this_artifact.delete()
            ```
        """
        self.connexion.delete("/sdk/artifact/{}".format(self.id))

    @exception_handler
    @beartype
    def download(self, target_path: str = "./", force_replace: bool = False) -> None:
        """Download an experiment's artifact to a given target_path.

        Examples:
            ```python
                this_artifact.download("myDir")
                file_list = os.path.listdir("myDir")
                print(file_list)
                >>> ["saved_model.zip"]
            ```
        Arguments:
            target_path (str, optional): Path to download the file to, default to cwd. Defaults to './'.

        """
        self.sync()
        path = os.path.join(target_path, self.filename)
        if self.connexion.download_file(
            self.object_name, path, self.large, force_replace=force_replace
        ):
            logger.info("{} downloaded successfully".format(self.filename))
        else:  # pragma: no cover
            logger.error(
                "Did not download file '{}' ({})".format(self.name, self.filename)
            )
