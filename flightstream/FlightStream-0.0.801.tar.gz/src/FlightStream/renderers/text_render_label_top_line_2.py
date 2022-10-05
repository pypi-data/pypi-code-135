#!/usr/bin/env python3

from FlightStream.renderers.text_render import TextRender


class TextRenderLabelTopLine2(TextRender):

    def initialise_subclass(self):
        self.font_size = 16
        self.text_anchor = 'mt'
        self.offset_x = 0
        self.offset_y = 32
        self.colour = 'white'
