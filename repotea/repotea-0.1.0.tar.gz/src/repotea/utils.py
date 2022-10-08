# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2022 Michał Góral.

from typing import Optional

import os
import sys


def eprint(*a, **kw):
    kw["file"] = sys.stderr
    print(*a, **kw)


def die(*a, **kw):
    eprint(*a, **kw)
    sys.exit(1)


def getenv(var: str) -> Optional[str]:
    return os.environ.get(var)
