#!/usr/bin/env python3

from FlightStream.renderers.renderer import Renderer


class DrawingRenderer(Renderer):

    SHAPE_ROUNDED_RECTANGLE = 1

    def __init__(self):
        self.shape = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.colour = 'black'
        self.radius = 0
        self.initialise_subclass()
        self.initialise_instance()

    def get_shape(self) -> int:
        return self.shape

    def get_x1(self) -> int:
        return self.x1

    def get_y1(self) -> int:
        return self.y1

    def get_x2(self) -> int:
        return self.x2

    def get_y2(self) -> int:
        return self.y2

    def get_colour(self):
        return self.colour

    def get_radius(self) -> int:
        return self.radius

    def get_dimensions(self) -> tuple:
        return (self.x1, self.y1, self.x2, self.y2)

    def set_shape(self, shape: int):
        self.shape = shape

    def set_x1(self, x1: int):
        self.x1 = x1

    def set_y1(self, y1: int):
        self.y1 = y1

    def set_x2(self, x2: int):
        self.x2 = x2

    def set_y2(self, y2: int):
        self.y2 = y2

    def set_colour(self, colour):
        self.colour = colour

    def set_radius(self, radius: int):
        self.radius = radius

    def render(self, draw, image, text):
        if text != True:
            return
        switcher = {
            self.SHAPE_ROUNDED_RECTANGLE: self.render_rounded_rectangle(draw),
        }
        switcher.get(self.get_shape(), None)

    def render_rounded_rectangle(self, draw):
        draw.rounded_rectangle(self.get_dimensions(
        ), fill=self.get_colour(), radius=self.get_radius())
