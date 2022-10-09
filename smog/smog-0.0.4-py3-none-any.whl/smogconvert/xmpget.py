import sys
import json

try:
    from core import *
except:
    from .core import *


def convert(args=None, container=None):
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
        # to write first before we can read the meta data
        fnamtemp = tmpf.mktemp(suffix=".png", prefix="IMG_smog-", guard=True)
        with open(fnamtemp, "wb") as ft:
            ft.write(inp)

        fmt = opts.get("format", "xml")

        if fmt == "xml":
            # this is the only format for xmpset
            xmpmeta = xmp_meta(fnamtemp)
            xmpmeta = str(xmpmeta)
        # todo others formats
        # very low priority
        elif fmt == "json":
            xmpmeta = xmp_dict(fnamtemp)
            xmpmeta = json.dumps(xmpmeta, indent=4)
        elif fmt == "tags":
            xmpmeta = get_tags(fnamtemp)
            xmpmeta = json.dumps(xmpmeta)
        elif fmt == "keyval":
            xmpmeta = get_tags(fnamtemp)
            xmpmeta = "\n".join([f"{k}={v}" for k, v in xmpmeta])
        elif fmt == "cfg":
            xmpmeta = get_tags(fnamtemp)
            raise NotImplementedError()  # todo
        elif fmt == "csv":
            xmpmeta = get_tags(fnamtemp)
            xmpmeta = "\n".join([f"{k}\t{v}" for k, v in xmpmeta])
        else:
            raise Exception("wrong format", fmt)

    fnam = expand_path(fnam)
    ensure_path(fnam)
    with open(fnam, "w") as f:
        f.write(xmpmeta)

    ArgsTeeAdapter(args).tee(inp, inp)


if __name__ == "__main__":
    # print(sys.argv)
    sys.exit(convert())
