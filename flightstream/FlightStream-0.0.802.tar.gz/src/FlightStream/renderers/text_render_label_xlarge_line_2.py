#!/usr/bin/env python3

from FlightStream.renderers.text_render import TextRender


class TextRenderLabelXLargeLine2(TextRender):

    def initialise_subclass(self):
        self.font_size = 26
        self.offset_y = 60
        self.colour = 'white'
