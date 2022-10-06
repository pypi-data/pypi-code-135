from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame


class ScrollText(Frame):
    def __init__(self, parent: Widget, VScroll: bool = True, HScroll: bool = False):
        self.build(parent.Me)

        from Paperl.Paperui.Widgets.text import Text
        from Paperl.Paperui.Widgets.scrollBar import ScrollBar

        self.Text = Text(self)

        if VScroll:
            self.VScroll = ScrollBar(self)
            self.VScroll.setOrient("vertical")
            self.VScroll.setWidget(self.Text, "y")
            self.VScroll.pack(fillType="y", sideType="right", marginX=10, marginY=10)

            self.Text.setVerticalScrollBar(self.VScroll)

        if HScroll:
            self.HScroll = ScrollBar(self)
            self.HScroll.setOrient("horizontal")
            self.HScroll.setWidget(self.Text, "x")
            self.HScroll.pack(fillType="x", sideType="bottom")

            self.Text.setHorizontalScrollBar(self.HScroll)

        self.Text.pack(fillType="both", expandType="yes", marginX=10, marginY=10)

    def build(self, parent: Widget):
        from tkinter.ttk import Frame
        self.Me = Frame(parent)