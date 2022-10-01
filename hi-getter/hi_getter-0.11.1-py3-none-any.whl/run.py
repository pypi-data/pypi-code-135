###################################################################################################
#                              MIT Licence (C) 2022 Cubicpath@Github                              #
###################################################################################################
"""Initialize values and runs the application. :py:func:`main` acts as an entry-point."""
from __future__ import annotations

__all__ = (
    'main',
)

import sys
from typing import Final

from ._version import __version__
from .exceptions import ExceptionHook
from .gui import GetterApp
from .utils.system import patch_windows_taskbar_icon


def main(*args, **kwargs) -> int:
    """Run the program. GUI script entrypoint.

    Args are passed to a QApplication instance.
    """
    patch_windows_taskbar_icon(f'cubicpath.{__package__}.app.{__version__}')

    # ExceptionHook is required for subscribing to ExceptionEvents
    with ExceptionHook():
        APP: Final[GetterApp] = GetterApp(*args, **kwargs)
        APP.windows['app'].show()
        return APP.exec()


if __name__ == '__main__':
    main(*sys.argv)
