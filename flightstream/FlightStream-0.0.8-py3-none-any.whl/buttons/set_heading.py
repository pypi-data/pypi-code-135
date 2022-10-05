#!/usr/bin/env python3

from FlightStream.actions.action_event_change_degrees import ActionEventChangeDegrees
from FlightStream.actions.action_property_degrees import ActionPropertyDegrees
from FlightStream.button_types.button_function import ButtonFunction
from FlightStream.renderers.text_render_label_large_line_1 import TextRenderLabelLargeLine1
from FlightStream.renderers.text_render_label_large_line_2 import TextRenderLabelLargeLine2
from FlightStream.sim_integration.sim_integration import SimIntegration
from FlightStream.sources.source import Source


class ButtonSetHeading(ButtonFunction):

    def initialise_instance(self):
        self.background = (40, 70, 40)
        self.add_title('HDG', TextRenderLabelLargeLine1())
        source = Source()
        source.set_source('AUTOPILOT_HEADING_LOCK_DIR')
        source.set_frequency(600)
        source.set_renderer(None)
        self.add_source(source)

    def set_change(self, change):
        hdg = ActionEventChangeDegrees()
        hdg.set_action('HEADING_BUG_SET')
        hdg.set_value(change)
        hdg.set_source(self.get_source(0))
        self.add_action(hdg)
        if change > 0:
            label = '+{}'.format(change)
        else:
            label = str(change)
        self.add_title(label, TextRenderLabelLargeLine2())

    def get_button_up_new_value(self, sim_integration: SimIntegration):
        action = self.get_action(0)
        cur = sim_integration.get_aircraft_request_value(self.get_source(0))
        new = (cur + action.get_value()) % 360
        return int(new)
