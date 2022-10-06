#!/usr/bin/env python3

from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class ButtonFunction(ButtonMonitor):

    def button_up(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        self.execute_actions(sdbr, sim_integration)
