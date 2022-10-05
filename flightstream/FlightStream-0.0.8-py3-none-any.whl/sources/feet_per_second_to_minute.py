#!/usr/bin/env python3

from FlightStream.sources.source import Source


class SourceFeetPerSecondToMinute(Source):

    def get_value_formatted(self):
        value = self.get_sim_hook_value_as_percent()
        if value == None:
            return ''
        return value

    def get_sim_hook_value_as_percent(self):
        value = self.get_sim_hook_value()
        if value is None:
            return None
        return round(value * 60)
