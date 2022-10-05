#!/usr/bin/env python3

from FlightStream.actions.abstract_action import AbstractAction
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class ActionEvent(AbstractAction):

    def __init__(self):
        self.action_type = self.ACTION_TYPE_EVENT
        self.action = None
        self.value = None
        self.initialise_subclass()
        self.initialise_instance()

    def initialise_subclass(self):
        pass

    def initialise_instance(self):
        pass

    def execute(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        try:
            sim_integration.trigger_event(self.action, self.value)
        except Exception as e:
            print(e)
            return None
