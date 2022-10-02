from datetime import datetime
from decimal import (
    Decimal,
)

from bmb.schema.util import (
    assertValid,
    doc,
)

from bmb.entity.invoice_metadata import (
    InvoiceMetadataV5,
)


def parse_invoice_v5_bytes(std_invoice_v5_bytes):
    assert isinstance(std_invoice_v5_bytes, bytes)
    assertValid(std_invoice_v5_bytes, "standard_invoice_v5.xsd")
    document = doc(std_invoice_v5_bytes)
    im = InvoiceMetadataV5()
    im.type = "invoice"

    def date():
        xpath = "//date/text()"
        document_dates = document.xpath(xpath)
        return datetime.strptime(
            document_dates[0],
            "%Y-%m-%d",
            ).date()

    im.date = date()

    def racoss():
        xpath = "//buyer/text()"
        document_receiver_names = document.xpath(xpath)
        return document_receiver_names[0]

    im.racoss = racoss()

    def number():
        xpath = "//number/text()"
        document_numbers = document.xpath(xpath)
        return document_numbers[0]

    im.reference = number()

    def amount():
        xpath = "//invoice/gross/text()"
        document_grosses = document.xpath(xpath)
        return document_grosses[0]

    im.total = Decimal(amount())

    def currencycode():
        xpath = "//currencycode/text()"
        document_currencycodes = document.xpath(xpath)
        return document_currencycodes[0]

    im.currency_code = currencycode()

    return im
