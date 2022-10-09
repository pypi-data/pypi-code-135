import sys
import json

from libxmp import XMPFiles, XMPMeta

try:
    from core import *
except:
    from .core import *


def convert(args=None, container=None):
    """
    this will stamp xmp data
    make sure to use strip before to ensure all other data is really gone
    """
    args = get_argv(args)
    check_argv(args)

    opts = opt_argv(args)
    opts = ArgsOptsAdapter(opts)

    with ArgsInAdapter(args) as fi:
        inp = fi.read()

    fnam = opts.pop()
    if fnam is None:
        raise Exception("no file for metadata")

    with CtxTempFile() as tmpf:
        # this is a bit compicated since we need
        # to write first before we can set the meta data
        fnamtemp = tmpf.mktemp(suffix=".png", prefix="IMG_smog-", guard=True)
        with open(fnamtemp, "wb") as ft:
            ft.write(inp)

        fmt = opts.get("format", "xml")

        fnam = expand_path(fnam)
        with open(fnam) as f:
            xmpmeta_s = f.read()

        if fmt == "xml":
            xmpmeta = XMPMeta()
            xmpmeta.parse_from_str(xmpmeta_s, xmpmeta_wrap=True)

            xmpfile = XMPFiles()
            xmpfile.open_file(file_path=fnamtemp, open_forupdate=True)
            if not xmpfile.can_put_xmp(xmpmeta):
                raise Exception("can not put xmpmeta")
            xmpfile.put_xmp(xmpmeta)
            xmpfile.close_file()

        else:
            raise Exception("wrong format", fmt)

        with open(fnamtemp, "rb") as f:
            outp = f.read()

    ArgsTeeAdapter(args).tee(inp, outp)


if __name__ == "__main__":
    # print(sys.argv)
    sys.exit(convert())
