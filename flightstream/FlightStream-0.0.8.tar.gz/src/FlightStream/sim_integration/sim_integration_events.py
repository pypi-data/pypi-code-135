#!/usr/bin/env python3

from SimConnect.EventList import EventHelper


class NewEventFeatures:
    def add_features(self, sim_integration):
        EventList = Events(sim_integration.sm)
        sim_integration.get_aircraft_events().list.append(EventList)


class Events(EventHelper):
    list = {
        (b'REQUEST_LUGGAGE', "Requests luggage.", "Shared Cockpit"),
        (b'REQUEST_CATERING', "Requests catering.", "Shared Cockpit"),
        (b'REQUEST_POWER_SUPPLY', "Requests a power supply.", "Shared Cockpit"),
        (b'AP_FLIGHT_LEVEL_CHANGE_ON', "FL.", "Shared Cockpit"),
    }
