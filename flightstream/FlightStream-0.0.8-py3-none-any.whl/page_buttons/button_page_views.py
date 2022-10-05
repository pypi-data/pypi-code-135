#!/usr/bin/env python3

import FlightStream.page_buttons.button_page
import FlightStream.pages.page_views
from FlightStream.renderers.text_render_label_menu import TextRenderLabelMenu


class ButtonPageViews(FlightStream.page_buttons.button_page.ButtonPage):

    def initialise_instance(self):
        self.add_title('VIEWS', TextRenderLabelMenu())

    def get_new_page(self):
        return FlightStream.pages.page_views.PageViews()
