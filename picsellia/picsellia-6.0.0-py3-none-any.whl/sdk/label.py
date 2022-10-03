import logging
import warnings

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.schemas import LabelSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Label(Dao):
    def __init__(self, connexion: Connexion, data: dict) -> None:
        Dao.__init__(self, connexion, data)

    @property
    def name(self) -> str:
        return self._name

    def __str__(self):
        return "{}Label '{}'{} (id: {})".format(
            bcolors.GREEN, self.name, bcolors.ENDC, self.id
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/label/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> LabelSchema:
        object = LabelSchema(**data)
        self._name = object.name
        return object

    @exception_handler
    @beartype
    def update(self, name: str) -> None:
        """Update this label with a new name.

        Examples:
            ```python
                a_label.update(name="new name")
            ```
        """
        payload = {"name": name}
        r = self.connexion.patch(
            "/sdk/label/{}".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this label from the platform.
        All annotations shapes with this label will be deleted!
        This is a very dangerous move.

        :warning: **DANGER ZONE**: Be very careful here!

        Examples:
            ```python
                this_label.delete()
            ```
        """
        self.connexion.delete("/sdk/label/{}".format(self.id))
        logger.info("{} deleted.".format(self))
