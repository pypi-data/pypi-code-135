#!/usr/bin/env python3

from FlightStream.page_buttons.button_page_inactive import ButtonPageInactive
from FlightStream.renderers.text_render_label_menu import TextRenderLabelMenu
from FlightStream.renderers.text_render_label_menu_line_1 import TextRenderLabelMenuLine1
from FlightStream.renderers.text_render_label_menu_line_2 import TextRenderLabelMenuLine2


class ButtonTakeOffLandInactive(ButtonPageInactive):

    def initialise_instance(self):
        self.add_title('TO /', TextRenderLabelMenuLine1())
        self.add_title('LAND', TextRenderLabelMenuLine2())
