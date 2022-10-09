# https://pypdf2.readthedocs.io/en/latest/user/add-watermark.html

import sys
import os
import datetime
from io import BytesIO

try:
    from core import *
except:
    from .core import *

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfMerger

from reportlab.pdfgen import canvas

# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors


def create_watermark(fnam, text, height=48, font="Courier-Bold"):
    pdf = canvas.Canvas(fnam)

    ptext = pdf.beginText(200, 600)
    ptext.setFont(font, height)
    ptext.setFillColor(colors.red)

    for line in text:
        ptext.textLine(line)

    pdf.drawText(ptext)
    pdf.save()


def convert(args=None, container=None):
    """
    apply watermark with PyPDF2 and reportlab
    """
    args = get_argv(args)
    check_argv(args)

    opts = opt_argv(args)
    opts = ArgsOptsAdapter(opts)

    with ArgsInAdapter(args) as fi:
        inp = fi.read()
        inp = BytesIO(inp)
        pdf = PdfFileReader(inp)

    year = datetime.datetime.now().year
    warning = opts.pop("TOP SECRECT \n - NOT FOR SHARING -")
    warning = warning.format(year=year)

    with CtxTempFile() as tmpf:
        tmpfile = tmpf.mktemp(suffix=".pdf", prefix="PRJ_smog-", guard=True)
        create_watermark(tmpfile, warning.split())
        watermark = PdfFileReader(tmpfile).pages[0]

    doc = PdfFileWriter()

    for p in pdf.pages:
        p.merge_page(watermark)
        doc.add_page(p)

    outp = BytesIO()
    doc.write(outp)
    outp = outp.getbuffer().tobytes()

    ArgsTeeAdapter(args).tee(inp, outp)


if __name__ == "__main__":
    # print(sys.argv)
    rc = convert()
