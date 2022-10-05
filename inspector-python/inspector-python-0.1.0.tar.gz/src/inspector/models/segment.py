from src.inspector.models import Performance
from src.inspector.models.enums import ModelType


class Segment(Performance):
    MODEL_NAME = ModelType.SEGMENT
    _model = None
    _type = None
    _label = None
    _host = None
    _transaction = None

    def __init__(self, transaction, type, label):
        self._model = self.MODEL_NAME
        self._type = type
        self._label = label
        self._transaction = transaction
