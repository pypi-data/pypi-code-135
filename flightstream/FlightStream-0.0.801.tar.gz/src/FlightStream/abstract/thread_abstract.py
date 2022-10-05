#!/usr/bin/env python3

import time


class ThreadAbstract:

    def __init__(self):
        self._running = None
        self._sleep = 1
        self.initialise_instance()

    def initialise_instance(self):
        pass

    def should_keep_running(self):
        return self._running

    def get_thread_name(self):
        return 'Thread has no name'

    def get_sleep(self):
        return self._sleep

    def terminate(self):
        print('Please stop {}'.format(self.get_thread_name()))
        self._running = False

    def run(self):
        self._running = True
        print('Please start {}'.format(self.get_thread_name()))
        while self.should_keep_running():
            time.sleep(self.get_sleep())
            if (self.should_keep_running() == True):
                self.process()
            else:
                print('Stopping '.format(self.get_thread_name()))

    def process(self):
        pass
