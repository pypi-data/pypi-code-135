#!/usr/bin/env python3

from FlightStream.page_buttons.button_page_inactive import ButtonPageInactive
from FlightStream.renderers.text_render_label_menu import TextRenderLabelMenu


class ButtonHomeInactive(ButtonPageInactive):

    def initialise_instance(self):
        self.add_title('HOME', TextRenderLabelMenu())

