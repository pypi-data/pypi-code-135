import datetime
import decimal
import logging
import uuid

from lxml import (
        etree,
        )


from jinja2 import (
        Environment,
        PackageLoader,
        )

from bmb.entity.invoice import (
        Invoice,
        Header,
        Body,
        Line,
        Totals,
        )
from bmb.entity.invoice_v5 import (
    create_invoice_v5,
    create_v5_header,
    create_v5_line,
)
from bmb.schema.util import (
    maybe_first,
    xpath,
    doc,
    first_or_empty_string,
)


log = logging.getLogger(__name__)

env = Environment(
        loader=PackageLoader("bmb.schema", "resources"),
        )


class Serializer:

    def __call__(self, invoice):
        log.debug("invoice: %s", invoice)
        assert isinstance(invoice, Invoice)
        template = env.get_template("standard_invoice_v4_jinja2.xml")
        bytes_ = template.render(**vars(invoice)).encode("utf-8")
        log.debug("bytes_: %s", bytes_)
        return bytes_


def _mk_date(invoice_doc):
    date_text = invoice_doc.xpath("/invoice/date/text()")[0]
    return datetime.datetime.strptime(date_text, "%Y-%m-%d").date()


def _mk_seller_id(invoice_doc):
    return None


def _mk_seller_name(invoice_doc):
    return invoice_doc.xpath("/invoice/seller/text()")[0]


def _mk_buyer_id(invoice_doc):
    buyer_id_text = invoice_doc.xpath("/invoice/receiver_basic/text()")[0]
    return uuid.UUID(buyer_id_text)


def _mk_buyer_name(invoice_doc):
    return invoice_doc.xpath("/invoice/buyer/text()")[0]


def _mk_number(invoice_doc):
    return invoice_doc.xpath("/invoice/number/text()")[0]


def _mk_sacors(invoice_doc):
    return invoice_doc.xpath("/invoice/sacors/text()")[0]


def _mk_currency_code(invoice_doc):
    return invoice_doc.xpath("/invoice/currencycode/text()")[0]


def _mk_header(invoice_doc):
    return Header(
            date=_mk_date(invoice_doc),
            seller_id=_mk_seller_id(invoice_doc),
            seller_name=_mk_seller_name(invoice_doc),
            buyer_id=_mk_buyer_id(invoice_doc),
            buyer_name=_mk_buyer_name(invoice_doc),
            number=_mk_number(invoice_doc),
            sacors=_mk_sacors(invoice_doc),
            currency_code=_mk_currency_code(invoice_doc),
            )


def _mk_body(invoice_doc):
    line_nodes = invoice_doc.xpath("//line")
    return Body(
            lines=[_mk_line(line_node) for line_node in line_nodes]
            )


def _mk_totals_net(invoice_doc):
    totals_net_text = invoice_doc.xpath("/invoice/net/text()")[0]
    return decimal.Decimal(totals_net_text)


def _mk_totals_vat(invoice_doc):
    totals_vat_text = invoice_doc.xpath("/invoice/vat/text()")[0]
    return decimal.Decimal(totals_vat_text)


def _mk_totals_gross(invoice_doc):
    totals_gross_text = invoice_doc.xpath("/invoice/gross/text()")[0]
    log.debug("gross: %s", decimal.Decimal(totals_gross_text))
    return decimal.Decimal(totals_gross_text)


def _mk_totals(invoice_doc):
    return Totals(
            net=_mk_totals_net(invoice_doc),
            vat=_mk_totals_vat(invoice_doc),
            gross=_mk_totals_gross(invoice_doc),
            )


def _mk_quantity(line_node):
    quantity_text = line_node.xpath("quantity/text()")[0]
    return decimal.Decimal(quantity_text)


def _mk_unit_price(line_node):
    unit_price_text = line_node.xpath("unitprice/text()")[0]
    return decimal.Decimal(unit_price_text)


def _mk_unit_of_measure(line_node):
    return line_node.xpath("unitofmeasure/text()")[0]


def _mk_item_code(line_node):
    return line_node.xpath("itemcode/text()")[0]


def _mk_description(line_node):
    return line_node.xpath("description/text()")[0]


def _mk_net(line_node):
    net_text = line_node.xpath("net/text()")[0]
    return decimal.Decimal(net_text)


def _mk_vatcode(line_node):
    return line_node.xpath("vatcode/text()")[0]


def _mk_vat(line_node):
    vat_text = line_node.xpath("vat/text()")[0]
    return decimal.Decimal(vat_text)


def _mk_gross(line_node):
    gross_text = line_node.xpath("gross/text()")[0]
    return decimal.Decimal(gross_text)


def _mk_line(line_node):
    return Line(
            quantity=_mk_quantity(line_node),
            unit_price=_mk_unit_price(line_node),
            unit_of_measure=_mk_unit_of_measure(line_node),
            item_code=_mk_item_code(line_node),
            description=_mk_description(line_node),
            net=_mk_net(line_node),
            vat=_mk_vat(line_node),
            vatcode=_mk_vatcode(line_node),
            gross=_mk_gross(line_node),
            )


class Deserializer:

    def __call__(self, invoice_bytes):
        assert isinstance(invoice_bytes, bytes)
        invoice_doc = etree.fromstring(invoice_bytes)
        header = _mk_header(invoice_doc)
        body = _mk_body(invoice_doc)
        totals = _mk_totals(invoice_doc)
        return Invoice(
                header=header,
                body=body,
                totals=totals,
                )


def deserialize_v5(v5_bytes):

    def get(path):
        return maybe_first(xpath(doc(v5_bytes), path, {}))

    def mget(path):
        return xpath(doc(v5_bytes), path, {})

    def elget(el, path):
        return maybe_first(xpath(el, path, {}))

    def elget_empty_string(el, path):
        return first_or_empty_string(xpath(el, path, {}))

    return create_invoice_v5(
        header=create_v5_header(
            number=get("number/text()"),
            date=get("date/text()"),
            seller=get("seller/text()"),
            buyer=get("buyer/text()"),
            currencycode=get("currencycode/text()"),
            net=get("net/text()"),
            vat=get("vat/text()"),
            gross=get("gross/text()"),
            seller_name=get("sellername/text()"),
            seller_address1=get("selleraddress1/text()"),
            seller_address2=get("selleraddress2/text()"),
            seller_address3=get("selleraddress3/text()"),
            seller_business_registration_number=get("sellerbusinessregistrationnumber/text()"),
            seller_tax_registration_number=get("sellertaxregistrationnumber/text()"),
            customer_name=get("customername/text()"),
            customer_address1=get("customeraddress1/text()"),
            customer_address2=get("customeraddress2/text()"),
            customer_address3=get("customeraddress3/text()"),
            customer_business_registration_number=get("customerbusinessregistrationnumber/text()"),
            customer_tax_registration_number=get("customertaxregistrationnumber/text()"),
        ),
        lines=[create_v5_line(
            quantity=elget(el, "quantity/text()"),
            unitprice=elget(el, "unitprice/text()"),
            unitofmeasure=elget(el, "unitofmeasure/text()"),
            itemcode=elget_empty_string(el, "itemcode/text()"),
            description=elget(el, "description/text()"),
            net=elget(el, "net/text()"),
            vat=elget(el, "vat/text()"),
            vatcode=elget(el, "vatcode/text()"),
            gross=elget(el, "gross/text()"),
        ) for el in mget("line")]
    )


def serialize_v5(v5_invoice):
    template = env.get_template("standard_invoice_v5.j2.xml")
    rendered_invoice = template.render(inv=v5_invoice)
    return rendered_invoice.encode("utf-8")
