import logging
import warnings
from uuid import UUID

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.label import Label
from picsellia.types.schemas import ClassificationSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Classification(Dao):
    def __init__(self, connexion: Connexion, annotation_id: UUID, data: dict) -> None:
        Dao.__init__(self, connexion, data)
        self._annotation_id = annotation_id

    @property
    def annotation_id(self) -> int:
        return self._annotation_id

    @property
    def label(self) -> Label:
        return self._label

    def __str__(self):
        return "{}Classification with label {} on annotation {} {} (id: {})".format(
            bcolors.BLUE,
            self.label.name,
            self.annotation_id,
            bcolors.ENDC,
            self.id,
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/classification/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> ClassificationSchema:
        object = ClassificationSchema(**data)
        self._label = Label(self.connexion, object.label.dict())
        return object

    @exception_handler
    @beartype
    def update(
        self,
        label: Label,
    ) -> None:
        """Update this classification with another label.

        Examples:
            ```python
                classif.update(label=label_plane)
            ```
        """
        payload = {"label_id": label.id}
        r = self.connexion.patch(
            "/sdk/classification/{}".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this classification from the platform.

        :warning: **DANGER ZONE**: Be very careful here!

        Examples:
            ```python
                classif.delete()
            ```
        """
        self.connexion.delete("/sdk/classification/{}".format(self.id))
        logger.info("{} deleted.".format(self))
