from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.button import Button


class MacButton(Button):
    def __init__(self, parent: Widget, text: str = ""):
        self.build(parent.Me, parent, text)

    def build(self, parent: Widget, parentWindow: Widget, text: str = ""):
        try:
            from tkmacosx.widgets.button import Button
        except:
            pass
        else:
            self.Me = Button(parent, text=text)
            if parentWindow.getStyle() == "SunValley.Light":
                self.setBackground("#fafafa")
                self.setForeground("#1c1c1c")
            if parentWindow.getStyle() == "SunValley.Dark":
                self.setBackground("#1c1c1c")
                self.setForeground("#fafafa")

    def setOverBackground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(overbackground=color)
        except TclError:
            prError("Widget -> OverBackground -> This property is not supported or this value is not supported")

    def getOverBackground(self):
        from tkinter import TclError
        try:
            self.getAttribute("overbackground")
        except TclError:
            prError("Widget -> OverBackground -> This property is not supported or this value is not supported")

    def setOverForeground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(overforeground=color)
        except TclError:
            prError("Widget -> OverForeground -> This property is not supported or this value is not supported")

    def getOverForeground(self):
        from tkinter import TclError
        try:
            self.getAttribute("overforeground")
        except TclError:
            prError("Widget -> OverForeground -> This property is not supported or this value is not supported")
