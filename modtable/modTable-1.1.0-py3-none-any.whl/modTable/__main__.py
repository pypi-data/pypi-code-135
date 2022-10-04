#!/usr/bin/env python3

# 3-Clause BSD License
# 
# Copyright (c) 2008-2022, James Philip Rowell,
# Alpha Eleven Incorporated
# www.alpha-eleven.com
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
# 
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
# 
#  3. Neither the name of the copyright holder, "Alpha Eleven, Inc.",
#     nor the names of its contributors may be used to endorse or
#     promote products derived from this software without specific prior
#     written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# modTable - prints the addition and multiplication tables for
# the ring of integers modulo n, denoted Z/nZ. The ring of integers
# modulo n is a field, if and only if n is prime.

import re
import argparse
import os
import sys
import subprocess
import seqLister
import textwrap
import math
import time
from operator import itemgetter

VERSION='1.1.0'

def main():

    # Redefine the exception handling routine so that it does NOT
    # do a trace dump if the user types ^C while the comment is running.
    #
    old_excepthook = sys.excepthook
    def new_hook(exceptionType, value, traceback):
        if exceptionType != KeyboardInterrupt and exceptionType != IOError:
            old_excepthook(exceptionType, value, traceback)
        else:
            pass
    sys.excepthook = new_hook

    p = argparse.ArgumentParser(
            prog="modTable",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description="Prints the addition and multiplication tables for \
            the ring of integers modulo n, denoted " + u"\u2124" + "/n" + u"\u2124" + 
            ". The ring of integers modulo n is a field if and only if n is prime.")

    p.add_argument("--version", action="version", version=VERSION)

    p.add_argument("n", metavar="n", type=int, nargs=1,
        help="the divisor for the modulus of " + u"\u2124" + "/n" + u"\u2124")

    args = p.parse_args()

    modBase = args.n[0]

    if modBase <= 1 :
        print(os.path.basename(sys.argv[0]) + \
            ": error: the divisor 'n' must be greater than or equal to 2", file=sys.stderr)
        sys.exit(1)

    i = 0

    print(u"\u2124" + "/" + str(modBase) + u"\u2124")
    outputLine   = ' + | '
    dividingLine = '-----'
    while i < modBase :
        outputLine   += "%2d " % i
        dividingLine += "---"
        i += 1
    print(outputLine)
    print(dividingLine)

    i = 0
    j = 0
    while i < modBase :
        outputLine = "%2d | " % i
        while j < modBase :
            outputLine += "%2d " % ((i + j) % modBase)
            j += 1
        print(outputLine)
        i += 1
        j = 0

    print("")
    outputLine   = ' * | '
    dividingLine = '-----'
    i = 0
    j = 0
    while i < modBase :
        outputLine   += "%2d " % i
        dividingLine += "---"
        i += 1
    print(outputLine)
    print(dividingLine)
    i = 0
    while i < modBase :
        outputLine = "%2d | " % i
        while j < modBase :
            outputLine += "%2d " % ((i * j) % modBase)
            j += 1
        print(outputLine)
        i += 1
        j = 0

if __name__ == '__main__':
    main()
