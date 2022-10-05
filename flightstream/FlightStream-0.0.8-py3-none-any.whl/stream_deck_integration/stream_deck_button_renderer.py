#!/usr/bin/env python3

import os
from PIL import Image, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper
import FlightStream.button_types.button


class StreamDeckButtonRenderer:

    def __init__(self):
        self.image_path = os.path.join(os.path.dirname(__file__), "Assets")

    def get_stream_deck(self):
        return self.stream_deck

    def set_stream_deck(self, stream_deck):
        self.stream_deck = stream_deck

    def render_button(self, button):
        image = self.render_sim_image(button)
        with self.stream_deck:
            self.stream_deck.set_key_image(button.get_key(), image)

    def render_sim_image(self, button):
        if button.has_icon():
            icon_filename = os.path.join(self.image_path, button.get_icon())
            print(icon_filename)
            icon = Image.open(icon_filename)
            image = PILHelper.create_scaled_image(
                self.stream_deck, icon, margins=[0, 0, 0, 0])
        else:
            image = Image.new('RGB', (self.stream_deck.KEY_PIXEL_WIDTH,
                                      self.stream_deck.KEY_PIXEL_HEIGHT),
                              color=button.get_background())

        draw = ImageDraw.Draw(image)

        for index in range(button.get_title_count()):
            self.render(draw, image, button.get_title_renderer(
                index), button.get_title(index))
#        self.render(draw, button)

        if (button.has_sources()):
            for index in range(button.get_source_count()):
                source = button.get_source(index)
                self.render(
                    draw, image, source.get_renderer(), source.get_sim_value())

        return PILHelper.to_native_format(self.stream_deck, image)

    def render(self, draw, image, renderer, text):
        if renderer == None:
            return
        renderer.render(draw, image, text)
