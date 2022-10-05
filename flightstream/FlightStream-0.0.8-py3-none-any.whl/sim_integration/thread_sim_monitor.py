#!/usr/bin/env python3

import time
from FlightStream.abstract.thread_abstract import ThreadAbstract


class SimMonitor(ThreadAbstract):

    def get_thread_name(self):
        return 'SimMonitor'

    def set_renderer(self, renderer):
        self.renderer = renderer

    def set_sim_integration(self, sim_integration):
        self.si = sim_integration

    def process(self):
        for index, button in enumerate(self.si.get_monitors()):
            if (self.should_keep_running()):
                self.renderer.render_sim_value(button)
            else:
                break
