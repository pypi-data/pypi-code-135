#!/usr/bin/env python3

from FlightStream.renderers.text_render import TextRender


class TextRenderLabelIndicator(TextRender):

    def initialise_subclass(self):
        self.font_size = 30
        self.offset_y = 66
        self.colour = 'yellow'
