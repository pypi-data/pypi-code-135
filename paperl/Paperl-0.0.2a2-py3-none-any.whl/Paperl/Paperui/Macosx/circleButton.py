from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Macosx.button import MacButton


class MacCircleButton(MacButton):
    def __init__(self, parent: Widget, text: str = ""):
        self.build(parent.Me, parent, text)

    def build(self, parent, parentWindow: Widget, text: str = ""):
        try:
            from tkmacosx.widgets.circlebutton import CircleButton
        except:
            pass
        else:
            self.Me = CircleButton(parent, text=text)

            if parentWindow.getStyle() == "SunValley.Light":
                self.setBackground("#fafafa")
            if parentWindow.getStyle() == "SunValley.Dark":
                self.setBackground("#1c1c1c")

