#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from FlightStream.renderers.renderer import Renderer


class TextRender(Renderer):

    def __init__(self):
        self.font = "C:\Windows\Fonts\ARIAL.TTF"
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
