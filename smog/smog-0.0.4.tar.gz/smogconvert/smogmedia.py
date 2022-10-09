import sys

try:
    from core import *
except:
    from .core import *


def convert(args=None, container=None):
    """
    get media from smog repo to stdin for next pipe stage
    this script expects the media-id as cmd-line parameter

    param-1: media-id
    """
    args = get_argv(args)
    check_argv(args)

    opts = opt_argv(args)
    opts = ArgsOptsAdapter(opts)

    # todo check bounds
    media_id = args[1]

    if media_id == "-":
        raise Exception("no media-id found")

    rc = procrun(args=["smog", "cat", "-id", media_id])

    data = rc.stdout

    ArgsTeeAdapter(args).tee(data, data)

    rc.stdout = None
    return rc


if __name__ == "__main__":
    # print(sys.argv)
    rc = convert()
