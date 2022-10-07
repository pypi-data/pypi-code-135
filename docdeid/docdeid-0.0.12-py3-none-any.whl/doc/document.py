from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import Any, Optional

from docdeid.annotate.annotation import AnnotationSet
from docdeid.tokenize.token import Token, TokenList
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

        self._token_lists = {}
        self._deidentified_text = None

    @property
    def text(self) -> str:
        return self._text

    def get_tokens(self, tokenizer_name: str = "default") -> TokenList:

        if tokenizer_name not in self._tokenizers:
            raise ValueError(f"Cannot get tokens from unknown tokenizer {tokenizer_name}")

        if tokenizer_name not in self._token_lists or self._token_lists[tokenizer_name] is None:
            self._token_lists[tokenizer_name] = self._tokenizers[tokenizer_name].tokenize(self._text)

        return self._token_lists[tokenizer_name]

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

    def get_metadata_item(self, key: str) -> Optional[Any]:

        if key not in self._metadata:
            return None

        return self._metadata[key]

    def add_metadata_item(self, key: str, item: Any):

        if key in self._metadata:
            raise RuntimeError(f"Key {key} already present in Document metadata, cannot overwrite (read only)")

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
