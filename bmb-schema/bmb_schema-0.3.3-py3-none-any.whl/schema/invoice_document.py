from datetime import datetime
from abc import (
        ABC,
        abstractmethod,
        )
import warnings

from lxml import etree

from bmb.schema.util import (
        assertValid,
        )


warnings.warn(
    "This module is deprecated. Use bmb.entity package instead.",
    DeprecationWarning,
)


class Document(ABC):

    @property
    @abstractmethod
    def content(self):
        pass

    @property
    @abstractmethod
    def date(self):
        pass

    @property
    @abstractmethod
    def sender_name(self):
        pass


class InvoiceDocument(Document, ABC):

    @property
    @abstractmethod
    def number(self):
        pass

    @property
    @abstractmethod
    def amount(self):
        pass

    @property
    @abstractmethod
    def currencycode(self):
        pass


class InvoiceV4(InvoiceDocument):

    def __init__(self, document_bytes):
        self.document_bytes = document_bytes
        assertValid(document_bytes, "standard_invoice_v4.xsd")
        self.document = etree.fromstring(document_bytes)

    @property
    def content(self):
        return self.document_bytes

    @property
    def date(self):
        xpath = "//date/text()"
        document_dates = self.document.xpath(xpath)
        return datetime.strptime(
            document_dates[0],
            "%Y-%m-%d",
            ).date()

    @property
    def receiver_name(self):
        xpath = "//buyer/text()"
        document_receiver_names = self.document.xpath(xpath)
        return document_receiver_names[0]

    @property
    def receiver_basic(self):
        xpath = "//receiver_basic/text()"
        receiver_basics = self.document.xpath(xpath)
        return receiver_basics[0]

    @property
    def sacors(self):
        xpath = "//sacors/text()"
        sacorss = self.document.xpath(xpath)
        return sacorss[0]

    @property
    def sender_name(self):
        xpath = "//seller/text()"
        document_sender_names = self.document.xpath(xpath)
        return document_sender_names[0]

    @property
    def number(self):
        xpath = "//number/text()"
        document_numbers = self.document.xpath(xpath)
        return document_numbers[0]

    @property
    def amount(self):
        xpath = "//invoice/gross/text()"
        document_grosses = self.document.xpath(xpath)
        return document_grosses[0]

    @property
    def currencycode(self):
        xpath = "//currencycode/text()"
        document_currencycodes = self.document.xpath(xpath)
        return document_currencycodes[0]


class InvoiceV5(InvoiceDocument):

    def __init__(self, document_bytes):
        self.document_bytes = document_bytes
        assertValid(document_bytes, "standard_invoice_v5.xsd")
        self.document = etree.fromstring(document_bytes)

    @property
    def content(self):
        return self.document_bytes

    @property
    def date(self):
        xpath = "//date/text()"
        document_dates = self.document.xpath(xpath)
        return datetime.strptime(
            document_dates[0],
            "%Y-%m-%d",
            ).date()

    @property
    def racoss(self):
        xpath = "//buyer/text()"
        document_receiver_names = self.document.xpath(xpath)
        return document_receiver_names[0]

    @property
    def sender_name(self):
        xpath = "//seller/text()"
        document_sender_names = self.document.xpath(xpath)
        return document_sender_names[0]

    @property
    def number(self):
        xpath = "//number/text()"
        document_numbers = self.document.xpath(xpath)
        return document_numbers[0]

    @property
    def amount(self):
        xpath = "//invoice/gross/text()"
        document_grosses = self.document.xpath(xpath)
        return document_grosses[0]

    @property
    def currencycode(self):
        xpath = "//currencycode/text()"
        document_currencycodes = self.document.xpath(xpath)
        return document_currencycodes[0]
