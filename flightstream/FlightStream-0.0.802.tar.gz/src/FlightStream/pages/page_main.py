#!/usr/bin/env python3

from FlightStream.actions.action_event import ActionEvent
from FlightStream.button_types.button import Button
from FlightStream.button_types.button_event import ButtonEvent
from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.button_types.button_monitor_indicator import ButtonMonitorIndicator
from FlightStream.buttons.airspeed_true import ButtonAirspeedTrue
from FlightStream.buttons.altitude import ButtonAltitude
from FlightStream.buttons.button_exit import ButtonExit
from FlightStream.buttons.button_flight_level import ButtonFlightLevel
from FlightStream.buttons.button_throttle import ButtonThrottle
from FlightStream.buttons.ground_speed import ButtonGroundSpeed
from FlightStream.page_buttons.button_page_home_inactive import ButtonHomeInactive
from FlightStream.page_buttons.button_page_startup import ButtonPageStartup
from FlightStream.page_buttons.button_page_takeoff_land import ButtonTakeOffLand
from FlightStream.page_buttons.button_page_views import ButtonPageViews
from FlightStream.abstract.page_template_xl import PageTemplateXl
from FlightStream.renderers.text_render_label_indicator import TextRenderLabelIndicator
from FlightStream.renderers.text_render_label_large_line_2 import TextRenderLabelLargeLine2
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.renderers.text_render_label_top_line_2 import TextRenderLabelTopLine2
from FlightStream.renderers.text_render_label_xlarge_line_2 import TextRenderLabelXLargeLine2
from FlightStream.sources.bool import SourceBoolean
from FlightStream.sources.feet_per_second_to_minute import SourceFeetPerSecondToMinute
from FlightStream.sources.meterstokm import SourceMetersToKm
from FlightStream.sources.percent import SourcePercent
from FlightStream.sources.seconds_to_minute import SourceSecondsToMinutes
from FlightStream.sources.source import Source
from FlightStream.sources.string import SourceString


class PageMain(PageTemplateXl):

    def get_button_1_1(self):
        return ButtonHomeInactive()

    def get_button_1_4(self):
        return ButtonFlightLevel()

    def get_button_1_5(self):
        return ButtonAltitude()

    def get_button_1_6(self):
        return ButtonThrottle()

    def get_button_1_7(self):
        return ButtonGroundSpeed()

    def get_button_1_8(self):
        return ButtonAirspeedTrue()

    def get_button_2_1(self):
        return ButtonPageStartup()

    def get_button_2_2(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('AP', TextRenderLabelTopLine1())
        source = SourceBoolean()
        source.set_source('AUTOPILOT_MASTER')
        btn.add_source(source)
        return btn

    # def get_button_2_6(self):
    #     btn = ButtonMonitor()
    #     btn.set_background(Button.COLOUR_INDICATOR)
    #     btn.add_title('Airport', TextRenderLabelTopLine1())
    #     source = SourceString()
    #     source.set_source('GPS_APPROACH_AIRPORT_ID')
    #     btn.add_source(source)
    #     return btn

    def get_button_3_1(self):
        return ButtonPageViews()

    def get_button_3_7(self):
        btn = ButtonMonitor()
        btn.set_background(Button.COLOUR_INDICATOR)
        btn.add_title('Fuel %', TextRenderLabelTopLine1())
        source = SourcePercent()
        source.set_source('FUEL_SELECTED_QUANTITY_PERCENT:1')
        source.set_renderer(TextRenderLabelIndicator())
        btn.add_source(source)
        return btn

    def get_button_3_8(self):
        btn = ButtonEvent()
        btn.add_title('Pause', TextRenderLabelTopLine1())
        pause = ActionEvent()
        pause.set_action('PAUSE_TOGGLE')
        btn.add_action(pause)
        return btn

    def get_button_4_1(self):
        return ButtonTakeOffLand()

    def get_button_4_2(self):
        btn = ButtonEvent()
        btn.add_title('Sim Rate', TextRenderLabelTopLine1())
        btn.add_title('-', TextRenderLabelXLargeLine2())
        rate = ActionEvent()
        rate.set_action('SIM_RATE_DECR')
        btn.add_action(rate)
        return btn

    def get_button_4_3(self):
        btn = ButtonEvent()
        btn.add_title('Sim Rate', TextRenderLabelTopLine1())
        btn.add_title('+', TextRenderLabelXLargeLine2())
        rate = ActionEvent()
        rate.set_action('SIM_RATE_INCR')
        btn.add_action(rate)
        return btn

    def get_button_4_4(self):
        btn = ButtonMonitor()
        btn.set_background(Button.COLOUR_INDICATOR)
        btn.add_title('Waypoint', TextRenderLabelTopLine1())
        btn.add_title('(minutes)', TextRenderLabelTopLine2())
        source = SourceSecondsToMinutes()
        source.set_source('GPS_WP_ETE')
        source.set_renderer(TextRenderLabelIndicator())
        btn.add_source(source)
        return btn

    def get_button_4_5(self):
        btn = ButtonMonitor()
        btn.set_background(Button.COLOUR_INDICATOR)
        btn.add_title('Waypoint', TextRenderLabelTopLine1())
        btn.add_title('(KM)', TextRenderLabelTopLine2())
        source = SourceMetersToKm()
        source.set_source('GPS_WP_DISTANCE')
        btn.add_source(source)
        return btn

    def get_button_4_6(self):
        btn = ButtonMonitor()
        btn.set_background(Button.COLOUR_INDICATOR)
        btn.add_title('Dest', TextRenderLabelTopLine1())
        btn.add_title('(minutes)', TextRenderLabelTopLine2())
        source = SourceSecondsToMinutes()
        source.set_source('GPS_ETE')
        source.set_renderer(TextRenderLabelIndicator())
        btn.add_source(source)
        return btn

    def get_button_4_7(self):
        btn = ButtonMonitor()
        btn.set_background(Button.COLOUR_INDICATOR)
        btn.add_title('Touchdown', TextRenderLabelTopLine1())
        btn.add_title('feet / min', TextRenderLabelTopLine2())
        source = SourceFeetPerSecondToMinute()
        source.set_source('PLANE_TOUCHDOWN_NORMAL_VELOCITY')
        btn.add_source(source)
        return btn

    def get_button_4_8(self):
        return ButtonExit()
