#!/usr/bin/env python3

from FlightStream.actions.action_property import ActionProperty
from FlightStream.button_types.button_function import ButtonFunction


class ButtonCameraState(ButtonFunction):

    def set_camera(self, state: int):
        view = ActionProperty()
        view.set_action('CAMERA_STATE')
        view.set_value(state)
        self.add_action(view)
