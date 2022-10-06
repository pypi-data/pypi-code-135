#!/usr/bin/env python3

from FlightStream.button_types.button import Button
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class ButtonEvent(Button):

    def initialise_subclass(self):
        self.background = self.COLOUR_BROWN
