import sys

try:
    from core import *
except:
    from .core import *

from PIL import Image
from io import BytesIO


def convert(args=None, container=None):
    """
    converts to jpeg format
    drops all xmp metadata
    will reduce also size
    """
    args = get_argv(args)
    check_argv(args)

    opts = opt_argv(args)
    opts = ArgsOptsAdapter(opts)

    with ArgsInAdapter(args) as fi:

        inp = fi.read()

        im = Image.open(BytesIO(inp))

        outformat = opts.get("format", "jpeg")

        outp = BytesIO()
        im.convert("RGB").save(outp, outformat)

        byts = outp.getbuffer().tobytes()

    ArgsTeeAdapter(args).tee(inp, byts)


if __name__ == "__main__":
    # print(sys.argv)
    sys.exit(convert())
