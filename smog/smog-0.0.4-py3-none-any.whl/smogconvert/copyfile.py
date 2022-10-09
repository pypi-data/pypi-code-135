import sys

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

    ArgsTeeAdapter(args).tee(inp, inp)


if __name__ == "__main__":
    # print(sys.argv)
    sys.exit(convert())
