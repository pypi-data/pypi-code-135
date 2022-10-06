from typing import Optional

from docdeid.doc.document import DocProcessorGroup, Document


class DocDeid:
    def __init__(self):

        self.tokenizers = {}
        self.processors = DocProcessorGroup()

    def deidentify(
        self, text: str, processors_enabled: Optional[list[str]] = None, metadata: Optional[dict] = None
    ) -> Document:

        doc = Document(text, tokenizers=self.tokenizers, metadata=metadata)

        self.processors.process(doc, processors_enabled)

        return doc
