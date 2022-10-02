from decimal import (
    Decimal as D,
)
import datetime
import decimal
import uuid
import warnings

warnings.warn(
    "This module is deprecated. Use bmb.entity package instead.",
    DeprecationWarning,
)


def isinstanceornone(obj, objtype):
    return any([
            isinstance(obj, objtype),
            obj is None,
            ])


class Invoice:

    header = None
    body = None
    totals = None
    footer = None

    def __init__(
            self,
            header=None,
            body=None,
            totals=None,
            footer=None,
            ):
        assert isinstanceornone(header, Header)
        self.header = header
        assert isinstanceornone(body, Body)
        self.body = body
        assert isinstanceornone(totals, Totals)
        self.totals = totals
        assert isinstanceornone(footer, Footer)
        self.footer = footer

    def __eq__(self, other):
        return all([
            isinstance(other, self.__class__),
            self.header == other.header,
            self.body == other.body,
            self.totals == other.totals,
            self.footer == other.footer,
            ])

    def __repr__(self):
        return (
                "{classname}("
                "header={header}, "
                "body={body}, "
                "totals={totals}, "
                "footer={footer}, "
                ")"
                ).format(
                        classname=self.__class__.__name__,
                        header=self.header,
                        body=self.body,
                        totals=self.totals,
                        footer=self.footer,
                        )


class Header:

    def __init__(
            self,
            date=None,
            seller_id=None,
            seller_name=None,
            buyer_id=None,
            buyer_name=None,
            number=None,
            sacors=None,
            currency_code=None,
            ):
        assert isinstanceornone(date, datetime.date)
        self.date = date
        assert isinstanceornone(seller_id, uuid.UUID)
        self.seller_id = seller_id
        assert isinstanceornone(seller_name, str)
        self.seller_name = seller_name
        assert isinstanceornone(buyer_id, uuid.UUID)
        self.buyer_id = buyer_id
        assert isinstanceornone(buyer_name, str)
        self.buyer_name = buyer_name
        assert isinstanceornone(number, str)
        self.number = number
        assert isinstanceornone(sacors, str)
        self.sacors = sacors
        assert isinstanceornone(currency_code, str)
        self.currency_code = currency_code

    def __eq__(self, other):
        return all([
            isinstance(other, self.__class__),
            self.date == other.date,
            self.seller_id == other.seller_id,
            self.seller_name == other.seller_name,
            self.buyer_id == other.buyer_id,
            self.buyer_name == other.buyer_name,
            self.number == other.number,
            self.sacors == other.sacors,
            self.currency_code == other.currency_code,
            ])

    def __repr__(self):
        return (
                "{classname}("
                "date={date}, "
                "seller_id={seller_id}, "
                "seller_name={seller_name}, "
                "buyer_id={buyer_id}, "
                "buyer_name={buyer_name}, "
                "number={number}, "
                "sacors={sacors}, "
                "currency_code={currency_code}, "
                ")"
                ).format(
                        classname=self.__class__.__name__,
                        date=self.date,
                        seller_id=self.seller_id,
                        seller_name=self.seller_name,
                        buyer_id=self.buyer_id,
                        buyer_name=self.buyer_name,
                        number=self.number,
                        sacors=self.sacors,
                        currency_code=self.currency_code,
                        )


class Body:

    def __init__(
            self,
            lines=None,
            ):
        self.lines = lines

    def __eq__(self, other):
        return all([
            isinstance(other, self.__class__),
            self.lines == other.lines,
            ])

    def __repr__(self):
        return (
                "{classname}("
                "lines={lines}, "
                ")"
                ).format(
                        classname=self.__class__.__name__,
                        lines=self.lines,
                        )


class Line:

    def __init__(
            self,
            quantity=None,
            unit_price=None,
            unit_of_measure=None,
            item_code=None,
            description=None,
            net=None,
            vat=None,
            vatcode=None,
            gross=None,
            ):

        assert isinstanceornone(quantity, decimal.Decimal)
        self.quantity = quantity
        assert isinstanceornone(unit_price, decimal.Decimal)
        self.unit_price = unit_price
        assert isinstanceornone(unit_of_measure, str)
        self.unit_of_measure = unit_of_measure
        assert isinstanceornone(item_code, str)
        self.item_code = item_code
        assert isinstanceornone(description, str)
        self.description = description
        assert isinstanceornone(net, decimal.Decimal)
        self.net = net
        assert isinstanceornone(vat, decimal.Decimal)
        self.vat = vat
        assert isinstanceornone(vatcode, str)
        self.vatcode = vatcode
        assert isinstanceornone(gross, decimal.Decimal)
        self.gross = gross

    def __eq__(self, other):
        return all([
            isinstance(other, self.__class__),
            self.quantity == other.quantity,
            self.unit_price == other.unit_price,
            self.unit_of_measure == other.unit_of_measure,
            self.item_code == other.item_code,
            self.description == other.description,
            self.net == other.net,
            self.vat == other.vat,
            self.vatcode == other.vatcode,
            self.gross == other.gross,
            ])

    def __repr__(self):
        return (
                "{classname}("
                "quantity={quantity}, "
                "unit_price={unit_price}, "
                "unit_of_measure={unit_of_measure}, "
                "item_code={item_code}, "
                "description={description}, "
                "net={net}, "
                "vat={vat}, "
                "vatcode={vatcode}, "
                "gross={gross}, "
                ")"
                ).format(
                        classname=self.__class__.__name__,
                        quantity=self.quantity,
                        unit_price=self.unit_price,
                        unit_of_measure=self.unit_of_measure,
                        item_code=self.item_code,
                        description=self.description,
                        net=self.net,
                        vat=self.vat,
                        vatcode=self.vatcode,
                        gross=self.gross,
                        )


class Totals:

    def __init__(
            self,
            net=None,
            vat=None,
            gross=None,
            ):
        assert isinstanceornone(net, decimal.Decimal)
        self.net = net
        assert isinstanceornone(vat, decimal.Decimal)
        self.vat = vat
        assert isinstanceornone(gross, decimal.Decimal)
        self.gross = gross

    def __eq__(self, other):
        return all([
            isinstance(other, self.__class__),
            self.net == other.net,
            self.vat == other.vat,
            self.gross == other.gross,
            ])

    def __repr__(self):
        return (
                "{classname}("
                "net={net}, "
                "vat={vat}, "
                "gross={gross}, "
                ")"
                ).format(
                        classname=self.__class__.__name__,
                        net=self.net,
                        vat=self.vat,
                        gross=self.gross,
                        )


class Footer:

    pass


class InvoiceV5:
    """Shadows standard_invoice_v5.xsd

    Serializable/Deserializable.
    """

    class Header:

        def __init__(self):
            self._number = None
            self._date = None
            self._seller = None
            self._buyer = None
            self._currencycode = None
            self._net = None
            self._vat = None
            self._gross = None

        @property
        def number(self):
            return self._number

        @number.setter
        def number(self, value):
            assert isinstance(value, str)
            self._number = value

        @property
        def date(self):
            return self._date

        @date.setter
        def date(self, value):
            assert isinstance(value, datetime.date)
            self._date = value

        @property
        def seller(self):
            return self._seller

        @seller.setter
        def seller(self, value):
            assert isinstance(value, str)
            self._seller = value

        @property
        def buyer(self):
            return self._buyer

        @buyer.setter
        def buyer(self, value):
            assert isinstance(value, str)
            self._buyer = value

        @property
        def currencycode(self):
            return self._currencycode

        @currencycode.setter
        def currencycode(self, value):
            assert isinstance(value, str)
            self._currencycode = value

        @property
        def net(self):
            return self._net

        @net.setter
        def net(self, value):
            assert isinstance(value, D)
            self._net = value

        @property
        def vat(self):
            return self._vat

        @vat.setter
        def vat(self, value):
            assert isinstance(value, D)
            self._vat = value

        @property
        def gross(self):
            return self._gross

        @gross.setter
        def gross(self, value):
            assert isinstance(value, D)
            self._gross = value

        def __eq__(self, other):
            return all([
                isinstance(other, self.__class__),
                self.number == other.number,
                self.date == other.date,
                self.seller == other.seller,
                self.buyer == other.buyer,
                self.currencycode == other.currencycode,
                self.net == other.net,
                self.vat == other.vat,
                self.gross == other.gross,
            ])

    class Line:

        def __init__(self):
            self._quantity = None
            self._unitprice = None
            self._unitofmeasure = None
            self._itemcode = None
            self._description = None
            self._net = None
            self._vatcode = None
            self._vat = None
            self._gross = None

        @property
        def quantity(self):
            return self._quantity

        @quantity.setter
        def quantity(self, value):
            assert isinstance(value, D)
            self._quantity = value

        @property
        def unitprice(self):
            return self._unitprice

        @unitprice.setter
        def unitprice(self, value):
            assert isinstance(value, D)
            self._unitprice = value

        @property
        def unitofmeasure(self):
            return self._unitofmeasure

        @unitofmeasure.setter
        def unitofmeasure(self, value):
            assert isinstance(value, str)
            self._unitofmeasure = value

        @property
        def itemcode(self):
            return self._itemcode

        @itemcode.setter
        def itemcode(self, value):
            assert isinstance(value, str)
            self._itemcode = value

        @property
        def description(self):
            return self._description

        @description.setter
        def description(self, value):
            assert isinstance(value, str)
            self._description = value

        @property
        def net(self):
            return self._net

        @net.setter
        def net(self, value):
            assert isinstance(value, D)
            self._net = value

        @property
        def vat(self):
            return self._vat

        @vat.setter
        def vat(self, value):
            assert isinstance(value, D)
            self._vat = value

        @property
        def vatcode(self):
            return self._vatcode

        @vatcode.setter
        def vatcode(self, value):
            assert isinstance(value, str)
            self._vatcode = value

        @property
        def gross(self):
            return self._gross

        @gross.setter
        def gross(self, value):
            assert isinstance(value, D)
            self._gross = value

        def __eq__(self, other):
            return all([
                isinstance(other, self.__class__),
                self.quantity == other.quantity,
                self.unitprice == other.unitprice,
                self.unitofmeasure == other.unitofmeasure,
                self.itemcode == other.itemcode,
                self.description == other.description,
                self.net == other.net,
                self.vat == other.vat,
                self.vatcode == other.vatcode,
                self.gross == other.gross,
            ])

    def __init__(self):
        self._header = None
        self._lines = []

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value

    def __eq__(self, other):
        return all([
            isinstance(other, self.__class__),
            self.header == other.header,
            sorted(self.lines) == sorted(other.lines),
        ])


def create_invoice_v5(
        header=None,
        lines=[],
):
    inv = InvoiceV5()
    inv.header = header
    inv.lines = lines
    return inv


def create_v5_header(
        number,
        date,
        seller,
        buyer,
        currencycode,
        net,
        vat,
        gross,
):
    hdr = InvoiceV5.Header()
    hdr.number = number
    hdr.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    hdr.seller = seller
    hdr.buyer = buyer
    hdr.currencycode = currencycode
    hdr.net = D(net)
    hdr.vat = D(vat)
    hdr.gross = D(gross)
    return hdr


def create_v5_line(
        quantity,
        unitprice,
        unitofmeasure,
        itemcode,
        description,
        net,
        vatcode,
        vat,
        gross,
):
    lin = InvoiceV5.Line()
    lin.quantity = D(quantity)
    lin.unitprice = D(unitprice)
    lin.unitofmeasure = unitofmeasure
    lin.itemcode = itemcode
    lin.description = description
    lin.net = D(net)
    lin.vatcode = vatcode
    lin.vat = D(vat)
    lin.gross = D(gross)
    return lin
