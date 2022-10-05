#!/usr/bin/env python3

#         Python Stream Deck Library
#      Released under the MIT license
#
#   dean [at] fourwalledcubicle [dot] com
#         www.fourwalledcubicle.com
#

import os
import threading
from tkinter import Button
from PIL import Image
from StreamDeck.ImageHelpers import PILHelper
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.stream_deck_integration.stream_deck_button_renderer import StreamDeckButtonRenderer
from FlightStream.sim_integration.thread_sim_monitor import SimMonitor


class StreamDeckPageRenderer:

    def __init__(self):
        self.si = SimIntegration()
        self.image_path = os.path.join(os.path.dirname(__file__), "Assets")
        self.current_page = None
        self.sim_monitor = SimMonitor()
        self.sim_monitor.set_sim_integration(self.si)
        self.sim_monitor.set_renderer(self)
        self.thread_monitor_sim = None
        self.button_renderer = StreamDeckButtonRenderer()

    def get_sim_integration(self):
        return self.si

    def get_stream_deck(self):
        return self.stream_deck

    def set_current_page(self, current_page):
        self.current_page = current_page
        self.current_page.initialise()

    def set_stream_deck(self, stream_deck):
        self.stream_deck = stream_deck
        self.button_renderer.set_stream_deck(self.stream_deck)

    def sim_monitor_start(self):
        self.thread_monitor_sim = threading.Thread(
            target=self.sim_monitor.run, args=())
        self.thread_monitor_sim.start()

    def sim_monitor_stop(self):
        if (self.thread_monitor_sim == None):
            return
        self.sim_monitor.terminate()
        self.thread_monitor_sim.join()
        self.thread_monitor_sim = None

    def render_page(self):
        self.sim_monitor_stop()
        self.si.set_monitors_empty()
        for index, button in enumerate(self.current_page.get_buttons()):
            self.si.add_var_read(button)
            self.button_renderer.render_button(button)
        self.sim_monitor_start()

    def render_buttons_empty(self):
        image = Image.new('RGB', (self.stream_deck.KEY_PIXEL_WIDTH,
                          self.stream_deck.KEY_PIXEL_HEIGHT), color=(0, 0, 0))
        btn = PILHelper.to_native_format(self.stream_deck, image)
        for index in range(self.stream_deck.key_count()):
            self.stream_deck.set_key_image(index, btn)

    def render_sim_value(self, button: Button):
        if button.has_sources():
            if button.has_changed():
                # print('Render {}'.format(button.get_title(0)))
                # Generate the custom key with the requested image and label.
                image = self.button_renderer.render_sim_image(button)
                with self.stream_deck:
                    self.stream_deck.set_key_image(button.get_key(), image)

    def key_change_callback(self, deck, key, state):
        buttons = self.current_page.get_buttons()
        button = buttons[key]
        # print("Key {} {}, button {}".format(
        #     key, state, button.get_action()), flush=True)
        if(state):
            button.button_down(self, self.si)
        else:
            button.button_up(self, self.si)

        new_page = button.get_new_page()
        if (new_page == None):
            self.button_renderer.render_button(button)
        else:
            self.set_current_page(new_page)
            self.render_page()
