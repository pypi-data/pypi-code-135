#!/usr/bin/env python3

from FlightStream.renderers.text_render import TextRender


class TextRenderLabelLargeLine1(TextRender):

    def initialise_subclass(self):
        self.font_size = 22
        self.offset_y = 30
        self.colour = 'white'
