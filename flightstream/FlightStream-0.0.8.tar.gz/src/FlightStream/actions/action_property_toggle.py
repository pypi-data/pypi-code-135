#!/usr/bin/env python3

from FlightStream.actions.action_property_change import ActionPropertyChange
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class ActionPropertyToggle(ActionPropertyChange):

    def execute(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        try:
            sim_integration.set_aircraft_request_value(
                self.action, self.get_new_value(sim_integration))
        except Exception as e:
            print(e)
            return None

    def get_new_value(self, sim_integration: SimIntegration):
        cur = int(self.get_source_value(sim_integration))
        if cur == 0:
            return 1
        else:
            return 0
