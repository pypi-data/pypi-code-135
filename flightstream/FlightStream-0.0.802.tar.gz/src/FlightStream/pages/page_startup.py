#!/usr/bin/env python3

from FlightStream.actions.action_property_change import ActionPropertyChange
from FlightStream.actions.action_property_toggle import ActionPropertyToggle
from FlightStream.renderers.text_render_label_top_line_2 import TextRenderLabelTopLine2
from FlightStream.sources.bool import SourceBoolean
from FlightStream.sources.source import Source
from FlightStream.actions.action_event import ActionEvent
from FlightStream.button_types.button_event import ButtonEvent
from FlightStream.button_types.button_monitor_indicator import ButtonMonitorIndicator
from FlightStream.page_buttons.button_page_home import ButtonHome
from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.page_buttons.button_page_startup_inactive import ButtonPageStartupInactive
from FlightStream.page_buttons.button_page_takeoff_land import ButtonTakeOffLand
from FlightStream.page_buttons.button_page_views import ButtonPageViews
from FlightStream.abstract.page_template_xl import PageTemplateXl
from FlightStream.renderers.text_render_label_indicator import TextRenderLabelIndicator
from FlightStream.renderers.text_render_label_large import TextRenderLabelLarge
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.renderers.text_render_label_large_line_1 import TextRenderLabelLargeLine1
from FlightStream.renderers.text_render_label_large_line_2 import TextRenderLabelLargeLine2
from FlightStream.sources.string import SourceString


class PageStartup(PageTemplateXl):

    def get_button_1_1(self):
        return ButtonHome()

    def get_button_1_2(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('Battery',  TextRenderLabelTopLine1())
        source = SourceBoolean()
        source.set_source('ELECTRICAL_MASTER_BATTERY')
        btn.add_source(source)
        battery = ActionEvent()
        battery.set_action('TOGGLE_MASTER_BATTERY_ALTERNATOR')
        btn.add_action(battery)
        return btn

    def get_button_1_3(self):
        btn = ButtonMonitor()
        btn.add_title('APU Start', TextRenderLabelTopLine1())
        apu = ActionEvent()
        apu.set_action('APU_STARTER')
        btn.add_action(apu)
        return btn

    def get_button_2_1(self):
        return ButtonPageStartupInactive()

    def get_button_3_1(self):
        return ButtonPageViews()

    def get_button_3_2(self):
        btn = ButtonMonitorIndicator()
        btn.add_title('Ribbons', TextRenderLabelLarge())
        source = SourceBoolean()
        source.set_source('FLY_ASSISTANT_RIBBONS_ACTIVE')
        btn.add_source(source)
        ribbon = ActionPropertyToggle()
        ribbon.set_action('FLY_ASSISTANT_RIBBONS_ACTIVE')
        ribbon.set_source(source)
        btn.add_action(ribbon)
        return btn

    def get_button_3_3(self):
        btn = ButtonMonitor()
        btn.add_title('Landing', TextRenderLabelTopLine1())
        source = SourceString()
        source.set_source('FLY_ASSISTANT_LANDING_SPEED')
        source.set_renderer(TextRenderLabelTopLine2())
        btn.add_source(source)
        return btn

    def get_button_4_1(self):
        return ButtonTakeOffLand()

    def get_button_4_2(self):
        btn = ButtonEvent()
        btn.add_title('Power', TextRenderLabelLarge())
        power = ActionEvent()
        power.set_action('REQUEST_POWER_SUPPLY')
        btn.add_action(power)
        return btn

    def get_button_4_3(self):
        btn = ButtonEvent()
        btn.add_title('Fuel', TextRenderLabelLarge())
        fuel = ActionEvent()
        fuel.set_action('REQUEST_FUEL_KEY')
        btn.add_action(fuel)
        return btn

    def get_button_4_4(self):
        btn = ButtonEvent()
        btn.add_title('Catering', TextRenderLabelLarge())
        cater = ActionEvent()
        cater.set_action('REQUEST_CATERING')
        btn.add_action(cater)
        return btn

    def get_button_4_5(self):
        btn = ButtonEvent()
        btn.add_title('Luggage', TextRenderLabelLarge())
        luggage = ActionEvent()
        luggage.set_action('REQUEST_LUGGAGE')
        btn.add_action(luggage)
        return btn

    def get_button_4_6(self):
        btn = ButtonEvent()
        btn.add_title('Stairs', TextRenderLabelLarge())
        jetway = ActionEvent()
        jetway.set_action('TOGGLE_RAMPTRUCK')
        btn.add_action(jetway)
        return btn

    def get_button_4_7(self):
        btn = ButtonEvent()
        btn.add_title('Jetway', TextRenderLabelLarge())
        jetway = ActionEvent()
        jetway.set_action('TOGGLE_JETWAY')
        btn.add_action(jetway)
        return btn

    def get_button_4_8(self):
        btn = ButtonEvent()
        btn.add_title('Push', TextRenderLabelLargeLine1())
        btn.add_title('Back', TextRenderLabelLargeLine2())
        pushback = ActionEvent()
        pushback.set_action('TOGGLE_PUSHBACK')
        btn.add_action(pushback)
        return btn
