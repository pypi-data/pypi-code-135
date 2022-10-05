#!/usr/bin/env python3

from FlightStream.sources.source import Source


class SourceString(Source):

    def get_value_formatted(self):
        value = self.get_sim_hook_value()
        if value == None:
            return ''
        return str(value)[2:-1]
