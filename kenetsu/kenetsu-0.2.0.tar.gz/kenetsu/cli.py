#!/usr/bin/env python

from __future__ import print_function
import sys
import locale
import argparse

from .tail_loader import TailLoader
from .censor import Censor
from .maileater import MailLogEater

LOGPATH = "/var/log/maillog"

# Reset locale for parsing timestamp in logs
locale.setlocale(locale.LC_ALL, "C")


def main():
    parser = argparse.ArgumentParser(description="kenetsu")
    parser.add_argument(
        "--exclude-pattern",
        metavar="PAT",
        dest="excl_pats",
        type=str,
        help="Exclude pattern of lines",
        default="postfix/local",
    )
    parser.add_argument(
        "duration", metavar="SECOND", type=int, help="Duration seconds to load"
    )
    parser.add_argument(
        "logpath",
        metavar="FILE",
        type=str,
        help="Log file path to load",
        default=LOGPATH,
    )
    args = parser.parse_args()
    duration = args.duration
    logpath = args.logpath
    loader = TailLoader(logpath, duration)
    censor = Censor()
    eater = MailLogEater([args.excl_pats])
    for rawline in loader.readlines():
        line = censor.censor(rawline)
        eater.eat(line)
    print(eater)


def usage(name):
    print("Usage: %s SECOND [LOGPATH]" % name)


if __name__ == "__main__":
    main()
