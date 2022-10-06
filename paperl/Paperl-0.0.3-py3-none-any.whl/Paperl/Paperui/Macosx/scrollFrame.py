from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame


class MacScrollFrame(Frame):
    def __init__(self, parent: Widget, text: str = ""):
        self.build(parent.Me, text)

    def build(self, parent, text: str = ""):
        try:
            from tkmacosx.widgets.sframe import SFrame
        except:
            pass
        else:
            self.Me = SFrame(parent)

