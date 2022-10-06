#!/usr/bin/env python3

from FlightStream.button_types.button import Button
from FlightStream.abstract.page_template import PageTemplate


class PageTemplateXl(PageTemplate):

    def initialise(self):

        # Row 1
        self.append_button(0, self.get_button_1_1())
        self.append_button(1, self.get_button_1_2())
        self.append_button(2, self.get_button_1_3())
        self.append_button(3, self.get_button_1_4())
        self.append_button(4, self.get_button_1_5())
        self.append_button(5, self.get_button_1_6())
        self.append_button(6, self.get_button_1_7())
        self.append_button(7, self.get_button_1_8())

        # Row 2
        self.append_button(8, self.get_button_2_1())
        self.append_button(9, self.get_button_2_2())
        self.append_button(10, self.get_button_2_3())
        self.append_button(11, self.get_button_2_4())
        self.append_button(12, self.get_button_2_5())
        self.append_button(13, self.get_button_2_6())
        self.append_button(14, self.get_button_2_7())
        self.append_button(15, self.get_button_2_8())

        # Row 3
        self.append_button(16, self.get_button_3_1())
        self.append_button(17, self.get_button_3_2())
        self.append_button(18, self.get_button_3_3())
        self.append_button(19, self.get_button_3_4())
        self.append_button(20, self.get_button_3_5())
        self.append_button(21, self.get_button_3_6())
        self.append_button(22, self.get_button_3_7())
        self.append_button(23, self.get_button_3_8())

        # Row 4
        self.append_button(24, self.get_button_4_1())
        self.append_button(25, self.get_button_4_2())
        self.append_button(26, self.get_button_4_3())
        self.append_button(27, self.get_button_4_4())
        self.append_button(28, self.get_button_4_5())
        self.append_button(29, self.get_button_4_6())
        self.append_button(30, self.get_button_4_7())
        self.append_button(31, self.get_button_4_8())


# Row 1

    def get_button_1_1(self):
        return Button()

    def get_button_1_2(self):
        return Button()

    def get_button_1_3(self):
        return Button()

    def get_button_1_4(self):
        return Button()

    def get_button_1_5(self):
        return Button()

    def get_button_1_6(self):
        return Button()

    def get_button_1_7(self):
        return Button()

    def get_button_1_8(self):
        return Button()

# Row 2
    def get_button_2_1(self):
        return Button()

    def get_button_2_2(self):
        return Button()

    def get_button_2_3(self):
        return Button()

    def get_button_2_4(self):
        return Button()

    def get_button_2_5(self):
        return Button()

    def get_button_2_6(self):
        return Button()

    def get_button_2_7(self):
        return Button()

    def get_button_2_8(self):
        return Button()

# Row 3
    def get_button_3_1(self):
        return Button()

    def get_button_3_2(self):
        return Button()

    def get_button_3_3(self):
        return Button()

    def get_button_3_4(self):
        return Button()

    def get_button_3_5(self):
        return Button()

    def get_button_3_6(self):
        return Button()

    def get_button_3_7(self):
        return Button()

    def get_button_3_8(self):
        return Button()

# Row 4
    def get_button_4_1(self):
        return Button()

    def get_button_4_2(self):
        return Button()

    def get_button_4_3(self):
        return Button()

    def get_button_4_4(self):
        return Button()

    def get_button_4_5(self):
        return Button()

    def get_button_4_6(self):
        return Button()

    def get_button_4_7(self):
        return Button()

    def get_button_4_8(self):
        return Button()
