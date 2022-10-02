from abc import abstractmethod
from enum import Flag
from typing import Union


class Button(Flag):
    A = 0
    B = 1
    X = 2
    Y = 4
    DPAD_UP = 8
    DPAD_DOWN = 16
    DPAD_LEFT = 32
    DPAD_RIGHT = 64
    L_STICK_PRESS = 128
    R_STICK_PRESS = 256
    SHOULDER_L = 512
    SHOULDER_R = 1024
    SHOULDER_ZL = 2048
    SHOULDER_ZR = 4096
    HOME = 8192
    CAPTURE = 16384
    MINUS = 32768
    PLUS = 65536
    JCL_SR = 131072
    JCL_SL = 262144
    JCR_SR = 524288
    JCR_SL = 1048576


class NXWrapper:
    support_combo = False

    def combo_supported(self):
        return self.support_combo

    def __init__(self, press_duration_ms: int = 50, delay_ms: int = 120):
        self.press_duration_ms = press_duration_ms
        self.delay_ms = delay_ms

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def button_hold(self, button_name: Button, duration_ms: int):
        """
        Hold a button for a certain duration.

        :param button_name: The name of the button to push.
        :param duration_ms: The duration in milliseconds.
        """
        pass

    def button_press(self, button_name: Button):
        """
        Press a button.

        :param button_name: The name of the button to push.
        """
        return self.button_hold(button_name, self.press_duration_ms)

    def series_press(self, button_names: list[Union[Button, tuple[Button, int]]]):
        """
        Press a series of buttons.
        :param button_names: A list of button names.
        """
        for button_name in button_names:
            if isinstance(button_name, tuple):
                self.button_hold(button_name[0], button_name[1])
            else:
                self.button_press(button_name)

    @abstractmethod
    def disconnect(self):
        pass

    # Context Manager
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()
        return False
