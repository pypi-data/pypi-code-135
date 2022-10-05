#!/usr/bin/env python3

from FlightStream.sources.source import Source


class SourceFlightLevel(Source):

    def get_value_formatted(self):
        value = self.get_sim_hook_value_as_bool()
        if value == None:
            return ''
        return value

    def get_sim_hook_value_as_bool(self):
        value = self.get_sim_hook_value_as_int()
        if value == None:
            return None
        return round(value / 100)
