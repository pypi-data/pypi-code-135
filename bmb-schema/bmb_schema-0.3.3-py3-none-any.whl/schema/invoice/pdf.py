"""xml to pdf"""

from jinja2 import (
        Environment,
        PackageLoader,
        )

from weasyprint import (
    HTML,
    CSS,
)
from weasyprint.fonts import (
    FontConfiguration,
)

from bmb.schema.invoice.xml_serializer import (
    deserialize_v5,
)
from bmb.schema.util import (
    get_resource,
)

env = Environment(
        loader=PackageLoader("bmb.schema", "resources"),
        )
template = env.get_template("standard_invoice_v5_2.j2.html")
font_config = FontConfiguration()

src = "https://via.placeholder.com/240x180.png?text=Your%20Logo"
invoice_file = "invoice2.css"


def data_uri(logo):
    if logo:
        return "data:{media_type};base64,{data}".format(
            media_type=logo.media_type,
            data=logo.base64_data.decode("utf-8"),
        )
    return src


def v5bytes2pdf(
        v5bytes,
        invoice_id,
        logo=None,
):
    """
    Args:
        v5bytes (bytes): the xml invoice representation
    Returns (bytes): a pdf representation of the invoice
    """
    v5_invoice = deserialize_v5(v5bytes)
    rendered_invoice = template.render(
        inv=v5_invoice,
        logo_uri=data_uri(logo),
        invoice_id=invoice_id,
    )
    bytes_invoice = rendered_invoice
    html = HTML(string=bytes_invoice)
    css_bytes = get_resource(invoice_file)
    css = CSS(string=css_bytes, font_config=font_config)
    return html.write_pdf(
        stylesheets=[css],
        font_config=font_config,
    )
