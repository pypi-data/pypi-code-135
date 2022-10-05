from __future__ import annotations
from typing import Union
from src.inspector.models import Performance
from src.inspector.models.partials import HOST, User
import random
import string
from src.inspector.models.enums import TransactionType, ModelType
import resource


class Transaction(Performance):
    TYPE_REQUEST = TransactionType.REQUEST
    TYPE_PROCESS = TransactionType.PROCESS

    _name: Union[str, None] = None
    _model: Union[str, None] = None
    _type: Union[str, None] = None
    _hash: Union[str, None] = None
    _host: Union[str, None] = None
    _result: Union[str, None] = None
    _user: Union[User, None] = None
    _memory_peak: Union[str, None] = None

    def __init__(self, name: str, type_str: Union[str, None] = None) -> None:
        # if type_str is not None and type_str not in TransactionType._value2member_map_:
        #    raise ValueError('Transaction Type value not valid')
        self._model = ModelType.TRANSACTION
        self._name = name
        self._type = type_str
        self.hash = self.__generate_unique_hash()
        self.host = HOST()

    def with_user(self, id: str, name: Union[str, None] = None, email: Union[str, None] = None) -> Transaction:
        self._user = User(id=id, name=name, email=email)
        return self

    def end(self, duration: Union[float, None] = None):
        self._memory_peak = self.get_memory_peak()
        return Performance.end(self, duration)

    def get_memory_peak(self):
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    def sample_server_status(self, ratio: float):
        pass

    def set_result(self, result: str) -> Transaction:
        self._result = result
        return self

    def is_ended(self) -> bool:
        return self._duration is not None and self._duration > 0

    def __generate_unique_hash(self, length: int = 32) -> str:
        """
        Generate a unique transaction hash.
        :param length: length hash, default 32
        :type length: int
        :return: str
        """
        if length is None or length < 32:
            length = 32
        hash_str = ''.join(random.sample(string.ascii_letters + string.digits, length))
        return hash_str
