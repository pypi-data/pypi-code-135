#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from FlightStream.renderers.renderer import Renderer
from importlib.resources import files

class TextRender(Renderer):

    def __init__(self):
        # 07558_CenturyGothic  AovelSansRounded-rdDL   34460_SHAL____          
        self.font_arial = 'C:\Windows\Fonts\ARIAL.TTF'
        self.font_century_gothic = '07558_CenturyGothic.ttf'
        self.font_aovel = 'AovelSansRounded-rdDL.ttf'
        self.font = str(files('FlightStream.fonts').joinpath(self.font_century_gothic))
        self.font_size = 16
        self.text_anchor = 'mm'
        self.offset_x = 0
        self.offset_y = 14
        self.colour = 'white'
        self.initialise_subclass()
        self.initialise_instance()

    def render(self, draw, image, text):
        font = ImageFont.truetype(self.font, self.font_size)
        draw.text((image.width / 2, self.offset_y), text=str(text),
                  font=font, anchor=self.text_anchor, fill=self.colour)
