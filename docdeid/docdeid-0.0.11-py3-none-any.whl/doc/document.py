from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import Any, Optional

from docdeid.annotate.annotation import AnnotationSet
from docdeid.tokenize.token import Token
from docdeid.tokenize.tokenizer import BaseTokenizer


class Document:
    def __init__(
        self,
        text: str,
        tokenizers: Optional[dict[str, BaseTokenizer]] = None,
        metadata: Optional[dict] = None,
    ):

        self._text = text
        self._annotations = AnnotationSet()

        self._tokenizers = tokenizers
        self._metadata = metadata or {}

        self._tokens = {}
        self._deidentified_text = None

    @property
    def text(self) -> str:
        return self._text

    def get_tokens(self, tokenizer_name: str = "default") -> list[Token]:

        if tokenizer_name not in self._tokenizers:
            raise ValueError(f"Cannot get tokens from unknown tokenizer {tokenizer_name}")

        if tokenizer_name not in self._tokens or self._tokens[tokenizer_name] is None:
            self._tokens[tokenizer_name] = self._tokenizers[tokenizer_name].tokenize(self._text)

        return self._tokens[tokenizer_name].copy()

    @property
    def annotations(self) -> AnnotationSet:
        return self._annotations

    @annotations.setter
    def annotations(self, value: AnnotationSet):
        self._annotations = value

    @property
    def deidentified_text(self) -> str:

        return self._deidentified_text

    def set_deidentified_text(self, deidentified_text: str):

        self._deidentified_text = deidentified_text

    def get_metadata(self) -> dict:
        return self._metadata.copy()

    def get_metadata_item(self, key: str) -> Any:
        return self._metadata[key]

    def add_metadata_item(self, key: str, item: Any):

        if key in self._metadata:
            raise ValueError(f"Key {key} already present in Document metadata, cannot overwrite (read only)")

        self._metadata[key] = item


class DocProcessor(ABC):
    @abstractmethod
    def process(self, doc: Document, **kwargs):
        pass


class DocProcessorGroup(OrderedDict):
    def process(self, doc: Document, processors_enabled: Optional[list[str]] = None):

        for name, proc in self.items():
            if (processors_enabled is None) or (name in processors_enabled):
                proc.process(doc, processors_enabled=processors_enabled)
