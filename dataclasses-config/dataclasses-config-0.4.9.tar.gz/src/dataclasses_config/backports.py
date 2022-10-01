import sys

if (sys.version_info >= (3, 8)):
    from functools import cached_property
else:
    # noinspection PyUnresolvedReferences
    from cached_property import cached_property


__all__ = \
[
    'cached_property',
]
