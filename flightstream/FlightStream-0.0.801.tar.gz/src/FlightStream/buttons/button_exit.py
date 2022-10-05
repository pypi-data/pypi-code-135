#!/usr/bin/env python3

import sys
import threading
from FlightStream.button_types.button import Button
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer
from FlightStream.renderers.text_render_label_menu import TextRenderLabelMenu


class ButtonExit(Button):

    def initialise_subclass(self):
        self.background = (200, 0, 0)
        self.add_title('EXIT', TextRenderLabelMenu())

    def button_down(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        return

    def button_up(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        sdbr.sim_monitor_stop()
        deck = sdbr.get_stream_deck()
        with deck:
            deck.reset()
            deck.close()
        sim_integration.wrap_up()
        sys.exit()
