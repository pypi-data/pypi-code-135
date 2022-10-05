#!/usr/bin/env python3

import FlightStream.page_buttons.button_page
import FlightStream.pages.page_to_land
from FlightStream.renderers.text_render_label_menu_line_1 import TextRenderLabelMenuLine1
from FlightStream.renderers.text_render_label_menu_line_2 import TextRenderLabelMenuLine2


class ButtonTakeOffLand(FlightStream.page_buttons.button_page.ButtonPage):

    def initialise_instance(self):
        self.add_title('TO /', TextRenderLabelMenuLine1())
        self.add_title('LAND', TextRenderLabelMenuLine2())

    def get_new_page(self):
        return FlightStream.pages.page_to_land.PageTakeOffLand()
