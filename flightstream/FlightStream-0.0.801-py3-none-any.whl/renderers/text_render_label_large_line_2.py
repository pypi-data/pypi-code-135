#!/usr/bin/env python3

from FlightStream.renderers.text_render import TextRender


class TextRenderLabelLargeLine2(TextRender):

    def initialise_subclass(self):
        self.font_size = 22
        self.offset_y = 60
        self.colour = 'white'
