###################################################################################################
#                              MIT Licence (C) 2022 Cubicpath@Github                              #
###################################################################################################
"""Neutral namespace for constants. Meant to be star imported."""
from __future__ import annotations

__all__ = (
    'BYTE_UNITS',
    'HI_CACHE_PATH',
    'HI_CONFIG_PATH',
    'HI_PACKAGE_NAME',
    'HI_PATH_PATTERN',
    'HI_RESOURCE_PATH',
    'HI_SAMPLE_RESOURCE',
    'HI_URL_PATTERN',
    'SUPPORTED_IMAGE_EXTENSIONS',
    'SUPPORTED_IMAGE_MIME_TYPES',
)

import re
from pathlib import Path
from typing import Final

# Mappings

BYTE_UNITS = {'Bytes': 1024**0, 'KiB': 1024**1, 'MiB': 1024**2, 'GiB': 1024**3, 'TiB': 1024**4}
"""Mapping of byte units to their respective powers of 1024."""

# Tuples

SUPPORTED_IMAGE_EXTENSIONS: Final[tuple[str, ...]] = (
    'bmp', 'cur', 'gif', 'icns', 'ico', 'jpeg', 'jpg', 'pbm', 'pgm', 'png',
    'ppm', 'svg', 'svgz', 'tga', 'tif', 'tiff', 'wbmp', 'webp', 'xbm', 'xpm'
)
"""Tuple containing all image file extensions supported by application."""

SUPPORTED_IMAGE_MIME_TYPES: Final[tuple[str, ...]] = (
    'image/bmp', 'image/gif', 'image/jpeg', 'image/png', 'image/svg+xml', 'image/svg+xml-compressed',
    'image/tiff', 'image/vnd.microsoft.icon', 'image/vnd.wap.wbmp', 'image/webp', 'image/x-icns', 'image/x-portable-bitmap',
    'image/x-portable-graymap', 'image/x-portable-pixmap', 'image/x-tga', 'image/x-xbitmap', 'image/x-xpixmap'
)
"""Tuple containing all image mime types supported by application."""

# Strings

HI_PACKAGE_NAME:    Final[str] = __package__.split('.', maxsplit=1)[0]
"""The base package name for this application, for use in sub-packages."""

HI_SAMPLE_RESOURCE: Final[str] = 'Progression/file/Calendars/Seasons/SeasonCalendar.json'
"""Example resource. Is pre-filled in the search bar."""

# Paths

HI_CACHE_PATH:    Final[Path] = Path.home() / '.cache/hi_getter'
"""Directory containing cached API results."""

HI_CONFIG_PATH:   Final[Path] = Path.home() / '.config/hi_getter'
"""Directory containing user configuration data."""

HI_RESOURCE_PATH: Final[Path] = Path(__file__).parent / 'resources'
"""Directory containing application resources."""

# Patterns

HI_PATH_PATTERN: Final[re.Pattern] = re.compile(r'([A-Z]:\\)*([\w\-_.]+[/\\])+[\w\-_]*\.\w+|[/\\]\.\w+')
"""Regex pattern for finding a resource path. Finds quoted substrings with at least one folder name and file name (with a file extension)."""

HI_URL_PATTERN:  Final[re.Pattern] = re.compile(
    r'(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|'
    r'[a-z0-9.\-]+[.][a-z]{2,}/)(?:[^\s()<>{}\[\]]+|'
    r'\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|'
    r'\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|'
    r'\([^\s]+?\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’])|'
    r'(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.][a-z]{2,}\b/?(?!@))')
"""Regex pattern for finding URLs. Derived from https://gist.github.com/gruber/8891611."""
