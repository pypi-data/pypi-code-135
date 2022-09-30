# -*- coding: utf-8 -*-
######################################################
#     _____                  _____      _     _      #
#    (____ \       _        |  ___)    (_)   | |     #
#     _   \ \ ____| |_  ____| | ___ ___ _  _ | |     #
#    | |  | )/ _  |  _)/ _  | |(_  / __) |/ || |     #
#    | |__/ ( ( | | | ( ( | | |__| | | | ( (_| |     #
#    |_____/ \_||_|___)\_||_|_____/|_| |_|\____|     #
#                                                    #
#    Copyright (c) 2022 DataGrid Development Team    #
#    All rights reserved                             #
######################################################

from .audio import Audio
from .base import Asset
from .curve import Curve
from .datagrid import DataGrid  # noqa
from .image import Image
from .serialize import register_asset_type
from .text import Text
from .video import Video

for name, cls, asset_type in [
    (None, Asset, "asset"),
    ("AUDIO-ASSET", Audio, "audio"),
    ("CURVE-ASSET", Curve, "curve"),
    ("IMAGE-ASSET", Image, "image"),
    ("TEXT-ASSET", Text, "text"),
    ("VIDEO-ASSET", Video, "video"),
]:
    register_asset_type(name, cls, asset_type)
