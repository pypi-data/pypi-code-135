from Paperl.Paperui.Widgets.widget import Widget


class ScrollBar(Widget):
    def __init__(self, parent: Widget):
        self.build(parent.Me)

    def build(self, parent):
        from tkinter.ttk import Scrollbar
        self.Me = Scrollbar(parent)

    def onCommand(self, eventFunc: None = ...):
        self.Me.configure(command=eventFunc)

    def setWidget(self, widget: Widget, orient="y"):
        if orient == "y":
            self.onCommand(widget.Me.yview)
        elif orient == "x":
            self.onCommand(widget.Me.xview)

    def setValue(self, Start, End):
        self.Me.set(Start, End)