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
from picsellia.types.schemas import RectangleSchema
from picsellia.utils import filter_payload

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Rectangle(Dao):
    def __init__(self, connexion: Connexion, annotation_id: UUID, data: dict) -> None:
        Dao.__init__(self, connexion, data)
        self._annotation_id = annotation_id

    @property
    def annotation_id(self) -> int:
        return self._annotation_id

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def w(self) -> int:
        return self._w

    @property
    def h(self) -> int:
        return self._h

    @property
    def label(self) -> Label:
        return self._label

    def __str__(self):
        return "{}Rectangle (x:{},y:{},w:{},h:{}) with label {} on annotation {} {} (id: {})".format(
            bcolors.BLUE,
            self.x,
            self.y,
            self.w,
            self.h,
            self.label.name,
            self.annotation_id,
            bcolors.ENDC,
            self.id,
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/rectangle/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> RectangleSchema:
        object = RectangleSchema(**data)
        self._x = object.x
        self._y = object.y
        self._w = object.w
        self._h = object.h
        self._label = Label(self.connexion, object.label.dict())
        return object

    @exception_handler
    @beartype
    def update(
        self,
        x: int = None,
        y: int = None,
        w: int = None,
        h: int = None,
        label: Label = None,
    ) -> None:
        """Update this rectangle with new coordinates or new label.

        Examples:
            ```python
                rect.update(x=10, label=label_car)
            ```
        """
        payload = {"x": x, "y": y, "w": w, "h": h}
        filtered_payload = filter_payload(payload)
        if label is not None:
            filtered_payload["label_id"] = label.id
        r = self.connexion.patch(
            "/sdk/rectangle/{}".format(self.id), data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this rectangle from the platform.

        :warning: **DANGER ZONE**: Be very careful here!

        Examples:
            ```python
                rect.delete()
            ```
        """
        self.connexion.delete("/sdk/rectangle/{}".format(self.id))
        logger.info("{} deleted.".format(self))
