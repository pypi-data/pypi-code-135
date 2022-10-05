#!/usr/bin/env python3

from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer


class AbstractAction:

    ACTION_TYPE_EVENT = 1
    ACTION_TYPE_PROPERTY = 2

    def __init__(self):
        self.action_type = None
        self.action = None
        self.value = None

    def get_action_type(self):
        return self.action_type

    def get_action(self):
        return self.action

    def get_value(self):
        return self.value

    def set_action(self, action):
        self.action = action

    def set_value(self, value):
        self.value = value

    def execute(self, sdbr: StreamDeckButtonRenderer, sim_integration: SimIntegration):
        print('Not implemented')
