from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.widget import Widget


class DragFrameEx(Frame):
    def __init__(self, parent: Widget, style: bool = True):
        self.build(parent.Me, parent, style)

    def build(self, parent: Widget, window: Widget, style: bool = True):
        if style:
            from tkinter.ttk import Frame
            self.Me = Frame(parent)
        else:
            from tkinter import Frame
            self.Me = Frame(parent)
        self.drag(window)