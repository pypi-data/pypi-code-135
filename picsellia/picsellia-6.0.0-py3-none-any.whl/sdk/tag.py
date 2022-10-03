import logging
import warnings
from typing import List, Union

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.multi_object import MultiObject
from picsellia.types.enums import TagTarget
from picsellia.types.schemas import TagSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Tag(Dao):
    def __init__(self, connexion: Connexion, data: dict) -> None:
        Dao.__init__(self, connexion, data)

    @property
    def name(self) -> str:
        return self._name

    @property
    def target_type(self) -> TagTarget:
        return self._target_type

    def __str__(self):
        return "{}Tag '{}'{} (id: {})".format(
            bcolors.BLUE, self.name, bcolors.ENDC, self.id
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/tag/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> TagSchema:
        object = TagSchema(**data)
        self._name = object.name
        self._target_type = object.target_type
        return object

    @exception_handler
    @beartype
    def update(self, name: str) -> None:
        """Update this tag with a new name.

        Examples:
            ```python
                a_tag.update(name="new name")
            ```
        """
        payload = {"name": name}
        r = self.connexion.patch(
            "/sdk/tag/{}".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated".format(self))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this tag from the platform.
        All tagged object will not have this tag anymore.

        :warning: **DANGER ZONE**: Be very careful here!

        Examples:
            ```python
                tag.delete()
            ```
        """
        self.connexion.delete("/sdk/tag/{}".format(self.id))
        logger.info("{} deleted.".format(self))

    @exception_handler
    @beartype
    def attach_on(self, targets: Union[Dao, List[Dao], MultiObject[Dao]]) -> None:
        """Attach this tag on a list of target.

        Tag needs to be the same target type as the taggable object.
        For example, if it's a Data Tag, it can only be attached on Data.

        If this is not a good target type, it will not raised any Error but it will not do anything.

        Examples:
            ```python
                data_tag = datalake.create_data_tag("home")
                some_data = datalake.list_data()
                data_tag.attach_on(some_data)
            ```
        """
        if isinstance(targets, Dao):
            targets = [targets]
        payload = [target.id for target in targets]
        r = self.connexion.post(
            "/sdk/tag/{}/attach".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r["tag"])
        logger.info("{} was attached to {} object(s)".format(self, r["count"]))

    @exception_handler
    @beartype
    def detach_from(self, targets: Union[Dao, List[Dao], MultiObject[Dao]]) -> None:
        """Detach this tag from a list of target.

        Tag needs to be the same target type as the taggable object.
        For example, if it's a Data Tag, it can only be detached from a Data.

        If this is not a good target type, it will not raised any Error but it will not do anything.

        Examples:
            ```python
                data_tag = datalake.create_data_tag("home")
                some_data = datalake.list_data()
                data_tag.attach_on(some_data)

                data_tag.detach_from(some_data)
            ```
        """
        if isinstance(targets, Dao):
            targets = [targets]
        payload = [target.id for target in targets]
        r = self.connexion.post(
            "/sdk/tag/{}/detach".format(self.id), data=orjson.dumps(payload)
        ).json()
        self.refresh(r["tag"])
        logger.info("{} was detached from {} object(s)".format(self, r["count"]))
