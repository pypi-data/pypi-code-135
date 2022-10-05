#!/usr/bin/env python3

import math
from FlightStream.button_types.button_function import ButtonFunction
from FlightStream.sim_integration.sim_integration import SimIntegration


class ButtonFunctionPushback(ButtonFunction):

    def get_button_up_new_value(self, sim_integration: SimIntegration):
        cur = sim_integration.get_aircraft_request_value(
            self.get_source(0))
        cur_dgr = int(math.degrees(cur))
        new = cur_dgr + self.get_increment()
        print('{} current value: {} {} {} {}, new value: {}'.format(
            self.action, self.get_source(0), cur, "{:.2f}".format(cur), cur_dgr, new))
        return int((new / 360) * 4294967295)
