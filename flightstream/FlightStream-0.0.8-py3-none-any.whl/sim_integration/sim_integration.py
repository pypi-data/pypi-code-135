#!/usr/bin/env python3

#         Python Stream Deck Library
#      Released under the MIT license
#
#   dean [at] fourwalledcubicle [dot] com
#         www.fourwalledcubicle.com
#

from array import *
import string
import datetime
from time import time
from types import NoneType
from SimConnect import *
from FlightStream.button_types.button import Button
from FlightStream.sim_integration.sim_integration_events import NewEventFeatures
from FlightStream.sim_integration.sim_integration_requests import NewRequestFeatures


class SimIntegration:

    def __init__(self):
        self.monitors = []
        self.sm = None
        self.aq = None
        self.ae = None
        self.last_connection_check = datetime.datetime.now(
        ) - datetime.timedelta(hours=0, minutes=1)
        self.connect_sim()

    def is_sim_connected(self):
        return self.sm != None

    def connect_sim(self):
        if self.is_sim_connected() == True:
            return True
        difference = datetime.datetime.now() - self.last_connection_check
        if difference.total_seconds() < 30:
            return False
        try:
            print('Trying to connect to the Sim')
            self.sm = SimConnect()
            self.aq = AircraftRequests(self.sm)
            self.ae = AircraftEvents(self.sm)
            self.prepare_extended_features()
            print('..connected')
            return True
        except ConnectionError:
            print('...not running')
            self.last_connection_check = datetime.datetime.now()
            return False
        except:
            print('...failed')
            self.last_connection_check = datetime.datetime.now()
            return False

    def prepare_extended_features(self):
        new_request_features = NewRequestFeatures()
        new_request_features.add_features(self)
        new_event_features = NewEventFeatures()
        new_event_features.add_features(self)

    def add_var_read(self, button: Button):
        if self.connect_sim() == False:
            return
        if button.has_sources() == False:
            return
        for index in range(button.get_source_count()):
            source = button.get_source(index)
            source_name = source.get_source_name()
            sim_source = self.aq.find(source_name)
            if isinstance(sim_source, NoneType):
                print('Sim Integration button source {} {} does not exist'.format(index, source_name))
                return
            sim_source.time = source.get_frequency()
            source.set_sim_hook(sim_source)
            self.monitors.append(button)

    def get_monitors(self):
        return self.monitors

    def get_aircraft_requests(self):
        return self.aq

    def get_aircraft_events(self):
        return self.ae

    def get_aircraft_request(self, request_name):
        if self.connect_sim():
            return self.aq.find(request_name)

    def get_aircraft_request_value(self, request_name):
        if request_name == None:
            return 0
        if self.connect_sim() == False:
            return 0
        data = self.aq.get(request_name)
        if data is None:
            print('{} is not a valid request', format(request_name))
            return 0
        return data

    def set_aircraft_request_value(self, request_name, value):
        if self.connect_sim() == False:
            return False
        result = self.aq.set(request_name, value)
        print('{} change to {} success:{}'.format(request_name, value, result))
        return result

    def set_monitors_empty(self):
        self.monitors = []

    def trigger_event(self, event_name: string, value=None):
        print(' Trigger {}'.format(event_name))
        if self.connect_sim() == False:
            return False
        event_to_trigger = self.ae.find(event_name)
        if isinstance(event_to_trigger, NoneType):
            print(' Event {} does not exist'.format(event_name))
            return
        if value != None:
            event_to_trigger(value)
            print(' Trigger {} done'.format(event_name))
        else:
            event_to_trigger()
            print(' Trigger {} done'.format(event_name))
        return True

    def wrap_up(self):
        if self.is_sim_connected():
            self.sm.exit()
