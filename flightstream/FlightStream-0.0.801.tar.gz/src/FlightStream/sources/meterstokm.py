#!/usr/bin/env python3

from FlightStream.sources.source import Source


class SourceMetersToKm(Source):

    def get_value_formatted(self):
        value = self.get_sim_hook_value_as_int()
        if value == None:
            return ''
        return round(value/1000)
