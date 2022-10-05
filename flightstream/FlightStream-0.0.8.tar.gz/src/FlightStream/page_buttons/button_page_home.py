#!/usr/bin/env python3

from FlightStream.page_buttons.button_page import ButtonPage
import FlightStream.pages.page_main
from FlightStream.renderers.text_render_label_menu import TextRenderLabelMenu


class ButtonHome(ButtonPage):

    def initialise_instance(self):
        self.add_title('HOME', TextRenderLabelMenu())

    def get_new_page(self):
        return FlightStream.pages.page_main.PageMain()
