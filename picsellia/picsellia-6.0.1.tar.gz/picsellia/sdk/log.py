import logging
import warnings

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.bcolors import bcolors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.enums import LogType
from picsellia.types.schemas import LogDataType, LogSchema
from picsellia.utils import filter_payload

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Log(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    @property
    def name(self) -> str:
        return self._name

    @property
    def data(self) -> LogDataType:
        return self._data

    @property
    def type(self) -> LogType:
        return self._type

    def __str__(self):
        return "{}Log {}{} (id: {})".format(
            bcolors.GREEN, self.name, bcolors.ENDC, self.id
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get("/sdk/log/{}".format(self.id)).json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict):
        object = LogSchema(**data)
        self._name = object.name
        self._data = object.data
        self._type = object.type
        return object

    @exception_handler
    @beartype
    def update(self, name: str = None, data: LogDataType = None) -> None:
        """Update this log with a new name or new data

        You cannot change the type of this Log.

        Examples:
            ```python
                my_log.update(name="new_name", data={"key": "value"})
            ```
        Arguments:
            name (str, optional): New name of the log. Defaults to None.
            data (LogDataType, optional): New data of the log. Defaults to None.
        """
        payload = {"name": name, "data": data}
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            "/sdk/log/{}".format(self.id), data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)
        logger.info("{} updated.".format(self))

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this log

        Examples:
            ```python
                my_log.delete()
            ```
        """
        self.connexion.delete("/sdk/log/{}".format(self.id))

    @exception_handler
    @beartype
    def append(self, data: LogDataType) -> None:
        """Appends value to log with given name.

        You can only append log on Line logs.

        Arguments:
            name (str): name of the log is mandatory

        """
        assert self.type == LogType.LINE, "You can only append log on Line logs"
        payload = {"data": data}
        self.connexion.post(
            "/sdk/log/{}/append".format(self.id), data=orjson.dumps(payload)
        ).json()
