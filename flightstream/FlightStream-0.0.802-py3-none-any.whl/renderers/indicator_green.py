#!/usr/bin/env python3

from FlightStream.renderers.drawing_renderer import DrawingRenderer


class RendererIndicatorGreen(DrawingRenderer):

    def initialise_subclass(self):
        self.set_shape(self.SHAPE_ROUNDED_RECTANGLE)
        self.set_x1(10)
        self.set_y1(75)
        self.set_x2(80)
        self.set_y2(85)
        self.set_colour('green')
        self.set_radius(8)
