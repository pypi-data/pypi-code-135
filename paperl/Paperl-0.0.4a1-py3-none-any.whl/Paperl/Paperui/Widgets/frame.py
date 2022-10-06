from Paperl.Paperui.Widgets.widget import Widget


class Frame(Widget):
    def __init__(self, parent: Widget, style: bool = True):
        self.build(parent.Me, style)

    def build(self, parent: Widget, style: bool = True):
        if style:
            from tkinter.ttk import Frame
            self.Me = Frame(parent)
        else:
            from tkinter import Frame
            self.Me = Frame(parent)