from abc import ABC, abstractmethod
from collections import defaultdict

from docdeid.annotate.annotation import Annotation
from docdeid.doc.document import DocProcessor, Document


class BaseRedactor(DocProcessor, ABC):
    def process(self, doc: Document, **kwargs):
        redacted_text = self.redact(doc.text, doc.annotations)
        doc.set_deidentified_text(redacted_text)

    @abstractmethod
    def redact(self, text: str, annotations: list[Annotation]) -> str:
        """Redact the text."""


class RedactAllText(BaseRedactor):
    def __init__(self, open_char: str = "[", close_char: str = "]"):
        self.open_char = open_char
        self.close_char = close_char

    def redact(self, text: str, annotations: list[Annotation]):

        return f"{self.open_char}REDACTED{self.close_char}"


class SimpleRedactor(BaseRedactor):
    def __init__(self, open_char: str = "[", close_char: str = "]"):
        self.open_char = open_char
        self.close_char = close_char

    @staticmethod
    def _group_annotations_by_tag(annotations: list[Annotation]) -> list[list[Annotation]]:

        groups = defaultdict(list)

        for annotation in annotations:
            groups[annotation.tag].append(annotation)

        return list(groups.values())

    def redact(self, text: str, annotations: list[Annotation]):

        annotation_text_to_counter = {}

        for annotation_group in self._group_annotations_by_tag(annotations):

            annotation_text_to_counter_group = {}

            annotation_group = sorted(annotation_group, key=lambda a: a.get_sort_key(by=["end_char"]))

            for annotation in annotation_group:

                if annotation.text not in annotation_text_to_counter_group:
                    annotation_text_to_counter_group[annotation.text] = len(annotation_text_to_counter_group) + 1

            annotation_text_to_counter |= annotation_text_to_counter_group

        for annotation in annotations[::-1]:  # back to front

            assert annotation.text == text[annotation.start_char : annotation.end_char]

            text = (
                text[: annotation.start_char] + f"{self.open_char}"
                f"{annotation.tag.upper()}"
                f"-"
                f"{annotation_text_to_counter[annotation.text]}"
                f"{self.close_char}" + text[annotation.end_char :]
            )

        return text
