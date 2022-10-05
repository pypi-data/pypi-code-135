#!/usr/bin/env python3

from FlightStream.actions.action_event_increment import ActionEventIncrement
from FlightStream.button_types.button_function import ButtonFunction
from FlightStream.renderers.text_render_label_large_line_1 import TextRenderLabelLargeLine1
from FlightStream.renderers.text_render_label_large_line_2 import TextRenderLabelLargeLine2
from FlightStream.sources.source import Source


class ButtonFlightLevelChange(ButtonFunction):

    def initialise_instance(self):
        self.background = (50, 50, 75)
        self.add_title('FL', TextRenderLabelLargeLine1())

    def set_change(self, change):
        source1 = Source()
        source1.set_source('AUTOPILOT_ALTITUDE_LOCK_VAR')
        source1.set_frequency(600)
        source1.set_renderer(None)
        self.add_source(source1)
        hdg = ActionEventIncrement()
        hdg.set_action('AP_ALT_VAR_SET_ENGLISH')
        hdg.set_value(change)
        hdg.set_source(source1)
        self.add_action(hdg)        
        if change > 0:
            label = '+{}'.format(change)
        else:
            label = str(change)
        self.add_title(label, TextRenderLabelLargeLine2())
