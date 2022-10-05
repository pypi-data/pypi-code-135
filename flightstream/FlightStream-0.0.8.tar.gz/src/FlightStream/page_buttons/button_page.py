#!/usr/bin/env python3

from FlightStream.button_types.button import Button
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer
from FlightStream.renderers.text_render_label_menu import TextRenderLabelMenu


class ButtonPage(Button):

    def initialise_subclass(self):
        self.background = self.COLOUR_MENU

    def button_down(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        return None

    def button_up(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        return None
