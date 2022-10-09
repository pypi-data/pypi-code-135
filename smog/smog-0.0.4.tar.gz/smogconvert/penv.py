import sys
import os

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

    print("--- env")

    for k, v in os.environ.items():
        print(k, v)

    print("--- argv")

    print(opt_argv(args))

    ArgsTeeAdapter(args).tee(inp, inp)


if __name__ == "__main__":
    sys.exit(convert())
