#!/usr/bin/env python3

from FlightStream.actions.action_property import ActionProperty
from FlightStream.button_types.button_function import ButtonFunction


class ButtonCameraViewTypeIndex(ButtonFunction):

    def set_camera(self, state: int, type0: int, type1: int):
        camera = ActionProperty()
        camera.set_action('CAMERA_STATE')
        camera.set_value(state)
        self.add_action(camera)

        view1 = ActionProperty()
        view1.set_action('CAMERA_VIEW_TYPE_AND_INDEX:0')
        view1.set_value(type0)
        self.add_action(view1)

        view2 = ActionProperty()
        view2.set_action('CAMERA_VIEW_TYPE_AND_INDEX:1')
        view2.set_value(type1)
        self.add_action(view2)
