#!/usr/bin/env python3

from FlightStream.actions.abstract_action import AbstractAction
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class ActionProperty(AbstractAction):

    def __init__(self):
        self.action_type = self.ACTION_TYPE_PROPERTY
        self.action = None
        self.value = None

    def execute(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        try:
            sim_integration.set_aircraft_request_value(self.action, self.value)
        except Exception as e:
            print(e)
            return None
