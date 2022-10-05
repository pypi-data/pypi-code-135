#!/usr/bin/env python3

from FlightStream.actions.abstract_action import AbstractAction
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class ActionPropertyChange(AbstractAction):

    def __init__(self):
        self.action_type = self.ACTION_TYPE_PROPERTY
        self.action = None
        self.value = None
        self.source = None

    def set_source(self, source):
        self.source = source

    def execute(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        try:
            new = self.get_new_value(sim_integration)
            print('property change {} to {}'.format(self.action, new))
            sim_integration.set_aircraft_request_value(self.action, new)
        except Exception as e:
            print('Exception: {}'.format(e))
            return None

    def get_new_value(self, sim_integration: SimIntegration):
        cur = int(self.get_source_value(sim_integration))
        new = int(cur + self.value)
        print('cur {} new {}'.format(cur, new))
        return new

    def get_source_value(self, sim_integration: SimIntegration):
        # print('source {}'.format(self.source))
        return sim_integration.get_aircraft_request_value(self.source)
