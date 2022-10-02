from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.widget import Widget


class DragFrameEx(Frame):
    def __init__(self, parent: Widget):
        self.build(parent.Me, parent)

    def build(self, parent: Widget, window: Widget):
        from tkinter.ttk import Frame
        self.Me = Frame(parent)
        self.drag(window)