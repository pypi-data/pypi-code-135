#!/usr/bin/env python3

from FlightStream.sources.source import Source


class SourceSecondsToMinutes(Source):

    def get_value_formatted(self):
        value = self.get_sim_hook_value_as_int()
        if value == None:
            return ''
        mins = round(value / 60)
        hours = int(mins / 60)
        mins_remain = mins - (hours * 60)
        result = '{}:{}'.format(hours, mins_remain)
        return result
