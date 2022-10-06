#!/usr/bin/env python3

from FlightStream.actions.action_event import ActionEvent
from FlightStream.sources.source import Source
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class ActionEventIncrement(ActionEvent):

    def initialise_subclass(self):
        self.source = None

    def set_source(self, source: Source):
        self.source = source

    def execute(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        try:
            new = int(self.source.get_sim_value() + self.value)
            sim_integration.trigger_event(self.action, new)
        except Exception as e:
            print(e)
            return None
