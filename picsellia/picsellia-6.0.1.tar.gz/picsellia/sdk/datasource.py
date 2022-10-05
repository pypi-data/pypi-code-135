import logging
import warnings

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.schemas import DataSourceSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class DataSource(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    def __str__(self):
        return "{}Data source '{}'{} (id: {})".format(
            bcolors.GREEN, self.name, bcolors.ENDC, self.id
        )

    @property
    def name(self) -> str:
        return self._name

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> DataSourceSchema:
        object = DataSourceSchema(**data)
        self._name = object.name
        return object

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/data/source/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def update(self, name: str) -> None:
        """Update this data source with a new name.

        Examples:
            ```python
                sdk_source.update(name="new name")
            ```
        """
        payload = {"name": name}
        r = self.connexion.patch(
            "/sdk/data/source/{}".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this data source from the platform.
        All data with this source will not have source anymore

        :warning: **DANGER ZONE**: Be very careful here!

        Examples:
            ```python
                sdk_source.delete()
            ```
        """
        self.connexion.delete("/sdk/data/source/{}".format(self.id))
        logger.info("{} deleted.".format(self))
