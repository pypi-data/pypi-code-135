import sys

try:
    from core import *
except:
    from .core import *


def convert(args=None, container=None):
    """
    imagemagik -thumbnail
    resizes to 64x64> by default
    """
    args = get_argv(args)
    check_argv(args)

    opts = opt_argv(args)
    opts = ArgsOptsAdapter(opts)

    with ArgsInAdapter(args) as fi:

        inp = fi.read()

        size_ = opts.pop("64x64>")

        outf = opts.get("out", None)
        pipeio = opts.get("pipeio", False)

        rc = procrun(
            args=["convert", "-", "-thumbnail", size_, "-"],
            input=inp,
        )

        # todo test rc

    ArgsTeeAdapter(args).tee(inp, rc.stdout)

    rc.stdout = None
    return rc


if __name__ == "__main__":
    # print(sys.argv)
    rc = convert()
