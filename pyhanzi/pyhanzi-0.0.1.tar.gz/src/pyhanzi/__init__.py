#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""汉字处理工具"""

from __future__ import unicode_literals

from pyhanzi.compat import PY2

from pyhanzi.core import (     # noqa
    hanzi
)

__title__ = 'pyhanzi'
__version__ = '0.0.1'
__author__ = 'xiabo'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2022 xiabo'
__all__ = [
    
]
if PY2:
    # fix "TypeError: Item in ``from list'' not a string" on Python 2
    __all__ = [x.encode('utf-8') for x in __all__]