import logging
import warnings
from typing import List
from uuid import UUID

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.label import Label
from picsellia.types.schemas import PolygonSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Polygon(Dao):
    def __init__(self, connexion: Connexion, annotation_id: UUID, data: dict) -> None:
        Dao.__init__(self, connexion, data)
        self._annotation_id = annotation_id

    @property
    def annotation_id(self) -> int:
        return self._annotation_id

    @property
    def coords(self) -> List[List[int]]:
        return self._coords

    @property
    def label(self) -> Label:
        return self._label

    def __str__(self):
        return (
            "{}Polygon ({} points) with label {} on annotation {} {} (id: {})".format(
                bcolors.BLUE,
                len(self.coords),
                self.label.name,
                self.annotation_id,
                bcolors.ENDC,
                self.id,
            )
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/polygon/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> PolygonSchema:
        object = PolygonSchema(**data)
        self._coords = object.coords
        self._label = Label(self.connexion, object.label.dict())
        return object

    @exception_handler
    @beartype
    def update(
        self,
        coords: List = None,
        label: Label = None,
    ) -> None:
        """Update this polygon with new coords or new label.

        Examples:
            ```python
                poly.update(coords=[[0, 0], [0, 1], [1, 1], [0, 0]])
            ```
        """
        payload = {}
        if coords is not None:
            payload["polygon"] = coords
        if label is not None:
            payload["label_id"] = label.id
        assert payload != {}, "You can't update this polygon with no data to update"
        r = self.connexion.patch(
            "/sdk/polygon/{}".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this polygon from the platform.

        :warning: **DANGER ZONE**: Be very careful here!

        Examples:
            ```python
                poly.delete()
            ```
        """
        self.connexion.delete("/sdk/polygon/{}".format(self.id))
        logger.info("{} deleted.".format(self))
