#!/usr/bin/env python3

from FlightStream.actions.action_property import ActionProperty
from FlightStream.button_types.button import Button
from FlightStream.button_types.button_function import ButtonFunction
from FlightStream.buttons.camera_state import ButtonCameraState
from FlightStream.buttons.camera_view_type_index import ButtonCameraViewTypeIndex
from FlightStream.page_buttons.button_page_home import ButtonHome
import FlightStream.page_buttons.button_page_startup
import FlightStream.page_buttons.button_page_takeoff_land
from FlightStream.page_buttons.button_page_views_inactive import ButtonPageViewsInactive
from FlightStream.abstract.page_template_xl import PageTemplateXl
from FlightStream.renderers.text_render_label_large import TextRenderLabelLarge
from FlightStream.renderers.text_render_label_large_line_1 import TextRenderLabelLargeLine1
from FlightStream.renderers.text_render_label_large_line_2 import TextRenderLabelLargeLine2
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1


class PageViews(PageTemplateXl):

    def get_button_1_1(self):
        return ButtonHome()

    def get_button_1_2(self):
        btn = ButtonCameraState()
        btn.add_title('Pilot', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_RED)
        btn.set_camera(2)
        return btn

    def get_button_1_3(self):
        btn = ButtonCameraState()
        btn.add_title('External', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_RED)
        btn.set_camera(3)
        return btn

    def get_button_1_4(self):
        btn = ButtonCameraState()
        btn.add_title('Drone', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_RED)
        btn.set_camera(4)
        return btn

    def get_button_1_7(self):
        btn = ButtonFunction()
        btn.add_title('Upper', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_RED)
        view1 = ActionProperty()
        view1.set_action('COCKPIT_CAMERA_UPPER_POSITION')
        view1.set_value(1)
        btn.add_action(view1)
        return btn

    def get_button_1_8(self):
        btn = ButtonFunction()
        btn.add_title('Reset', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_RED)
        view = ActionProperty()
        view.set_action('CAMERA_REQUEST_ACTION')
        view.set_value(1)
        btn.add_action(view)
        return btn

    def get_button_2_1(self):
        return FlightStream.page_buttons.button_page_startup.ButtonPageStartup()

    def get_button_2_2(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Forward', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_BLUE)
        btn.set_camera(2, 1, 2)
        return btn

    def get_button_2_3(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Instr1', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_BLUE)
        btn.set_camera(2, 2, 1)
        return btn

    def get_button_2_4(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('PFD', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_BLUE)
        btn.set_camera(2, 2, 3)
        return btn

    def get_button_2_5(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Throttles', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_BLUE)
        btn.set_camera(2, 2, 4)
        return btn

    def get_button_2_6(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Radio', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_BLUE)
        btn.set_camera(2, 2, 6)
        return btn

    def get_button_2_7(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Over1', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_BLUE)
        btn.set_camera(2, 2, 8)
        return btn

    def get_button_2_8(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Over2', TextRenderLabelLarge())
        btn.set_background(Button.COLOUR_BLUE)
        btn.set_camera(2, 2, 9)
        return btn

    def get_button_3_1(self):
        return ButtonPageViewsInactive()

    def get_button_3_2(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Cockpit', TextRenderLabelTopLine1())
        btn.add_title('L 120', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_GREEN)
        btn.set_camera(2, 3, 4)
        return btn

    def get_button_3_3(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Cockpit', TextRenderLabelTopLine1())
        btn.add_title('Left', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_GREEN)
        btn.set_camera(2, 3, 0)
        return btn

    def get_button_3_4(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Cockpit', TextRenderLabelTopLine1())
        btn.add_title('L 45', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_GREEN)
        btn.set_camera(2, 3, 5)
        return btn

    def get_button_3_5(self):
        btn = ButtonFunction()
        btn.add_title('Reset', TextRenderLabelLargeLine1())
        btn.set_background(Button.COLOUR_GREEN)
        view1 = ActionProperty()
        view1.set_action('CAMERA_REQUEST_ACTION')
        view1.set_value(1)
        btn.add_action(view1)
        return btn

    def get_button_3_6(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Cockpit', TextRenderLabelTopLine1())
        btn.add_title('R 45', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_GREEN)
        btn.set_camera(2, 3, 6)
        return btn

    def get_button_3_7(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Cockpit', TextRenderLabelTopLine1())
        btn.add_title('Right', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_GREEN)
        btn.set_camera(2, 3, 2)
        return btn

    def get_button_3_8(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('Cockpit', TextRenderLabelTopLine1())
        btn.add_title('R 120', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_GREEN)
        btn.set_camera(2, 3, 7)
        return btn

    def get_button_4_1(self):
        return FlightStream.page_buttons.button_page_takeoff_land.ButtonTakeOffLand()

    def get_button_4_2(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('External', TextRenderLabelTopLine1())
        btn.add_title('RHS', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_YELLOW)
        btn.set_camera(3, 4, 2)
        return btn

    def get_button_4_3(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('External', TextRenderLabelTopLine1())
        btn.add_title('R Back', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_YELLOW)
        btn.set_camera(3, 4, 4)
        return btn

    def get_button_4_4(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('External', TextRenderLabelTopLine1())
        btn.add_title('Nose', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_YELLOW)
        btn.set_camera(3, 4, 1)
        return btn

    def get_button_4_5(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('External', TextRenderLabelTopLine1())
        btn.add_title('R Fwd', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_YELLOW)
        btn.set_camera(3, 4, 6)
        return btn

    def get_button_4_6(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('External', TextRenderLabelTopLine1())
        btn.add_title('LHS', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_YELLOW)
        btn.set_camera(3, 4, 0)
        return btn

    def get_button_4_7(self):
        btn = ButtonCameraViewTypeIndex()
        btn.add_title('External', TextRenderLabelTopLine1())
        btn.add_title('L Fwd', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_YELLOW)
        btn.set_camera(3, 4, 7)
        return btn

    def get_button_4_8(self):
        btn = ButtonFunction()
        btn.add_title('External', TextRenderLabelTopLine1())
        btn.add_title('Tail', TextRenderLabelLargeLine2())
        btn.set_background(Button.COLOUR_YELLOW)
        camera = ActionProperty()
        camera.set_action('CAMERA_REQUEST_ACTION')
        camera.set_value(1)
        btn.add_action(camera)
        return btn
