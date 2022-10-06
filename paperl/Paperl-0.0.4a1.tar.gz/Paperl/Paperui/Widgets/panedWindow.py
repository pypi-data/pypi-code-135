from Paperl.Paperui.Widgets.widget import Widget


class PanedWindow(Widget):
    def __init__(self, parent: Widget):
        self.build(parent.Me)

    def build(self, parent: Widget):
        from tkinter.ttk import Panedwindow
        self.Me = Panedwindow(parent)

    def addWidget(self, widget: Widget):
        self.Me.add(widget.Me)