#!/usr/bin/env python3

import FlightStream.page_buttons.button_page_startup
from FlightStream.actions.action_property_change import ActionPropertyChange
from FlightStream.button_types.button import Button
from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.sources.bool import SourceBoolean
from FlightStream.sources.percent import SourcePercent
from FlightStream.sources.source import Source
from FlightStream.actions.action_event import ActionEvent
from FlightStream.buttons.airspeed_true import ButtonAirspeedTrue
from FlightStream.buttons.altitude import ButtonAltitude
from FlightStream.buttons.button_flight_level import ButtonFlightLevel
from FlightStream.button_types.button_event import ButtonEvent
from FlightStream.buttons.button_throttle import ButtonThrottle
from FlightStream.buttons.ground_speed import ButtonGroundSpeed
from FlightStream.buttons.set_heading import ButtonSetHeading
from FlightStream.page_buttons.button_page_home import ButtonHome
from FlightStream.button_types.button_monitor_indicator import ButtonMonitorIndicator
from FlightStream.buttons.button_flight_level_change import ButtonFlightLevelChange
from FlightStream.page_buttons.button_page_takeoff_land_inactive import ButtonTakeOffLandInactive
from FlightStream.page_buttons.button_page_views import ButtonPageViews
from FlightStream.abstract.page_template_xl import PageTemplateXl
from FlightStream.renderers.text_render_label_indicator import TextRenderLabelIndicator
from FlightStream.renderers.text_render_label_indicator_1 import TextRenderLabelIndicator1
from FlightStream.renderers.text_render_label_indicator_2 import TextRenderLabelIndicator2
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.renderers.text_render_label_top_line_2 import TextRenderLabelTopLine2
from FlightStream.renderers.text_render_label_large_line_1 import TextRenderLabelLargeLine1
from FlightStream.renderers.text_render_label_large_line_2 import TextRenderLabelLargeLine2


class PageTakeOffLand(PageTemplateXl):

    def get_button_1_1(self):
        return ButtonHome()

    def get_button_1_2(self):
        btn = Button()
        btn.add_title('Flaps', TextRenderLabelTopLine1())
        source1 = SourcePercent()
        source1.set_source('LEADING_EDGE_FLAPS_LEFT_PERCENT')
        source1.set_frequency(1000)
        source1.set_renderer(TextRenderLabelIndicator1())
        btn.add_source(source1)
        source2 = SourcePercent()
        source2.set_source('TRAILING_EDGE_FLAPS_LEFT_PERCENT')
        source2.set_frequency(1000)
        source2.set_renderer(TextRenderLabelIndicator2())
        btn.add_source(source2)
        flapsup = ActionEvent()
        flapsup.set_action('FLAPS_UP')
        btn.add_action(flapsup)
        return btn

    def get_button_1_3(self):
        btn = ButtonMonitor()
        btn.add_title('Spoilers', TextRenderLabelTopLine1())
        source1 = SourcePercent()
        source1.set_source('SPOILERS_LEFT_POSITION')
        source1.set_frequency(1000)
        btn.add_source(source1)
        spoilers = ActionEvent()
        spoilers.set_action('SPOILERS_TOGGLE')
        btn.add_action(spoilers)
        return btn

    def get_button_1_4(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('Spoilers', TextRenderLabelTopLine1())
        btn.add_title('ARM', TextRenderLabelTopLine2())
        source1 = SourceBoolean()
        source1.set_source('SPOILERS_ARMED')
        source1.set_frequency(2000)
        btn.add_source(source1)
        spoilers = ActionEvent()
        spoilers.set_action('SPOILERS_ARM_TOGGLE')
        btn.add_action(spoilers)
        return btn

    def get_button_1_5(self):
        return ButtonAltitude()

    def get_button_1_6(self):
        return ButtonThrottle()

    def get_button_1_7(self):
        return ButtonGroundSpeed()

    def get_button_1_8(self):
        return ButtonAirspeedTrue()

    def get_button_2_1(self):
        return FlightStream.page_buttons.button_page_startup.ButtonPageStartup()

    def get_button_2_2(self):
        btn = ButtonEvent()
        btn.add_title('Flaps', TextRenderLabelLargeLine1())
        btn.add_title('DECR', TextRenderLabelLargeLine2())
        flapsup = ActionEvent()
        flapsup.set_action('FLAPS_DECR')
        btn.add_action(flapsup)
        return btn

    def get_button_2_3(self):
        btn = ButtonFlightLevelChange()
        btn.set_change(-5000)
        return btn

    def get_button_2_4(self):
        btn = ButtonFlightLevelChange()
        btn.set_change(-1000)
        return btn

    def get_button_2_5(self):
        btn = ButtonFlightLevelChange()
        btn.set_change(-100)
        return btn

    def get_button_2_6(self):
        btn = ButtonFlightLevelChange()
        btn.set_change(100)
        return btn

    def get_button_2_7(self):
        btn = ButtonFlightLevelChange()
        btn.set_change(1000)
        return btn

    def get_button_2_8(self):
        btn = ButtonFlightLevelChange()
        btn.set_change(5000)
        return btn

    def get_button_3_1(self):
        return ButtonPageViews()

    def get_button_3_2(self):
        btn = ButtonEvent()
        btn.add_title('Flaps', TextRenderLabelLargeLine1())
        btn.add_title('INCR', TextRenderLabelLargeLine2())
        flapsdown = ActionEvent()
        flapsdown.set_action('FLAPS_INCR')
        btn.add_action(flapsdown)
        return btn

    def get_button_3_3(self):
        btn = ButtonSetHeading()
        btn.set_change(-90)
        return btn

    def get_button_3_4(self):
        btn = ButtonSetHeading()
        btn.set_change(-10)
        return btn

    def get_button_3_5(self):
        btn = ButtonSetHeading()
        btn.set_change(-1)
        return btn

    def get_button_3_6(self):
        btn = ButtonSetHeading()
        btn.set_change(1)
        return btn

    def get_button_3_7(self):
        btn = ButtonSetHeading()
        btn.set_change(10)
        return btn

    def get_button_3_8(self):
        btn = ButtonSetHeading()
        btn.set_change(90)
        return btn

    def get_button_4_1(self):
        return ButtonTakeOffLandInactive()

    def get_button_4_2(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('LOC', TextRenderLabelLargeLine1())
        source1 = SourceBoolean()
        source1.set_source('AUTOPILOT_APPROACH_IS_LOCALIZER')
        btn.add_source(source1)
        loc = ActionEvent()
        loc.set_action('AP_LOC_HOLD_ON')
        btn.add_action(loc)
        return btn

    def get_button_4_3(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('APPR', TextRenderLabelLargeLine1())
        source1 = SourceBoolean()
        source1.set_source('AUTOPILOT_APPROACH_HOLD')
        btn.add_source(source1)
        appr = ActionEvent()
        appr.set_action('AP_APR_HOLD_ON')
        btn.add_action(appr)
        return btn

    def get_button_4_4(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('Landing', TextRenderLabelTopLine1())
        btn.add_title('Gear', TextRenderLabelTopLine2())
        source1 = SourceBoolean()
        source1.set_source('GEAR_POSITION:1')
        btn.add_source(source1)
        gear = ActionEvent()
        gear.set_action('GEAR_TOGGLE')
        btn.add_action(gear)
        return btn

    def get_button_4_5(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('FLCH', TextRenderLabelLargeLine1())
        source1 = SourceBoolean()
        source1.set_source('AUTOPILOT_FLIGHT_LEVEL_CHANGE')
        btn.add_source(source1)
        fl = ActionEvent()
        fl.set_action('AP_FLIGHT_LEVEL_CHANGE_ON')
        btn.add_action(fl)
        return btn

    def get_button_4_6(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('HDG', TextRenderLabelLargeLine1())
        source1 = SourceBoolean()
        source1.set_source('AUTOPILOT_HEADING_LOCK')
        btn.add_source(source1)
        hdg = ActionEvent()
        hdg.set_action('AP_HDG_HOLD')
        btn.add_action(hdg)
        return btn

    def get_button_4_7(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('Taxi', TextRenderLabelTopLine1())
        btn.add_title('Lights', TextRenderLabelTopLine2())
        source1 = SourceBoolean()
        source1.set_source('LIGHT_TAXI')
        btn.add_source(source1)
        light = ActionEvent()
        light.set_action('TOGGLE_TAXI_LIGHTS')
        btn.add_action(light)
        return btn

    def get_button_4_8(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('Landing', TextRenderLabelTopLine1())
        btn.add_title('Lights', TextRenderLabelTopLine2())
        source1 = SourceBoolean()
        source1.set_source('LIGHT_LANDING')
        btn.add_source(source1)
        light = ActionEvent()
        light.set_action('LANDING_LIGHTS_TOGGLE')
        btn.add_action(light)
        return btn
