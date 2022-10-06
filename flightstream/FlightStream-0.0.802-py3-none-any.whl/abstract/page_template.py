#!/usr/bin/env python3

from types import NoneType


class PageTemplate:
    def __init__(self):
        self.buttons = []

    def initialise(self):
        pass

    def append_button(self, key, button):
        if isinstance(button, NoneType):
            print('Key {} is not a button'.format(key))
            return
        button.set_key(key)
        # print('Add button {} {} (key {})'.format(
        #     key, button.get_title(0), button.get_key()))
        self.buttons.append(button)

    def get_buttons(self):
        return self.buttons
