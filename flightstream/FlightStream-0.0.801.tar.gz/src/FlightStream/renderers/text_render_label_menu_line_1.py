#!/usr/bin/env python3

from FlightStream.renderers.text_render import TextRender


class TextRenderLabelMenuLine1(TextRender):

    def initialise_subclass(self):
        self.font_size = 24
        self.offset_y = 30
        self.colour = (230,230,255)
