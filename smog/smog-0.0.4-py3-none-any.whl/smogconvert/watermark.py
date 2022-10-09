import sys
import os
import datetime

try:
    from core import *
except:
    from .core import *


def watermark(fnam, text, height=64, font="Courier"):

    # must be .png file
    if os.path.splitext(fnam)[1] != ".png":
        raise NotImplementedError("wrong format")

    text_ = f"label:'{text}'"
    offs = 30 * 2
    fact = 2

    args = [
        "convert",
        "-size",
        f"{len(text)*height/2*fact+offs*2}x{height*fact*2+offs}",
        "xc:none",
        "-font",
        font,
        "-pointsize",
        f"{height}",
        "-fill",
        "black",
        "-gravity",
        "NorthWest",
        "-draw",
        f"text 10,10 '{text}'",
        "-gravity",
        "SouthEast",
        "-draw",
        f"text 5,15 '{text}'",
        "-fill",
        "white",
        "-gravity",
        "NorthWest",
        "-draw",
        f"text 12,12 '{text}'",
        "-gravity",
        "SouthEast",
        "-draw",
        f"text 7,17 '{text}'",
        "-fill",
        "transparent",
        "-gravity",
        "NorthWest",
        "-draw",
        f"text 11,11 '{text}'",
        "-gravity",
        "SouthEast",
        "-draw",
        f"text 6,16 '{text}'",
        fnam,
    ]
    rc = procrun(args)
    return rc


def convert(args=None, container=None):
    """
    apply watermark with imagemagik -composite
    """
    args = get_argv(args)
    check_argv(args)

    opts = opt_argv(args)
    opts = ArgsOptsAdapter(opts)

    with ArgsInAdapter(args) as fi:

        inp = fi.read()

        # todo rework opts handling
        year = datetime.datetime.now().year
        tx = opts.pop("(c) {year}")
        tx = tx.format(year=year)

        # todo rework opts handling
        font_ = opts.get("font", "Courier")
        font_size_ = int(opts.get("font-size", 64))

        with CtxTempFile() as tmpf:

            fnam = tmpf.mktemp(suffix=".png", prefix="IMG_smog-", guard=True)

            rc = watermark(fnam, tx, height=font_size_, font=font_)
            if rc.returncode > 0:
                raise Exception(rc)

            rc = procrun(
                args=[
                    "composite",
                    "-tile",
                    fnam,
                    "-",
                    "-",
                ],
                input=inp,
            )

            # todo test rc

    ArgsTeeAdapter(args).tee(inp, rc.stdout)

    rc.stdout = None
    return rc


if __name__ == "__main__":
    # print(sys.argv)
    rc = convert()
