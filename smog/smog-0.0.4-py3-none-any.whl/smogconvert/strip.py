import sys

try:
    from core import *
except:
    from .core import *


def convert(args=None, container=None):
    """
    imagemagik -strip
    drops all xmp metadata
    will reduce also size
    """
    args = get_argv(args)
    check_argv(args)

    opts = opt_argv(args)
    opts = ArgsOptsAdapter(opts)

    with ArgsInAdapter(args) as fi:

        inp = fi.read()

        rc = procrun(
            args=["convert", "-", "-strip", "-"],
            input=inp,
        )

        # todo test rc

    ArgsTeeAdapter(args).tee(inp, rc.stdout)

    rc.stdout = None
    return rc


if __name__ == "__main__":
    # print(sys.argv)
    rc = convert()
