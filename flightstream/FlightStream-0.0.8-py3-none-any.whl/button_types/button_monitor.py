#!/usr/bin/env python3

from FlightStream.button_types.button_event import ButtonEvent
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.renderers.text_render_label_top_line_2 import TextRenderLabelTopLine2


class ButtonMonitor(ButtonEvent):

    def initialise_subclass(self):
        self.text_render = []
        self.text_render.append(TextRenderLabelTopLine1())
        self.text_render.append(TextRenderLabelTopLine2())
        self.background = self.COLOUR_BROWN
