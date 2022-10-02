from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.label import Label
from Paperl.Paperui.Widgets.button import Button


def empty():
    pass


class InfoBar(Frame):
    def __init__(self, parent: Widget, message: str = "", closable: bool = True, closefunc=empty, useSunValley: bool = False):
        """
from Paperl import *


Application = Application()


Window = Window()


Window.useStyleSunValley(STYLE_DARK)


InfoBar = InfoBar(Window, "Hello, This is a InfoBar", useSunValley=True)


InfoBar.open()


Application.run(Window)


        :param parent:
        :param message:
        :param closable:
        :param useSunValley:
        """

        super().__init__(parent)
        self.message = Label(self, message)
        self.message.pack(sideType="left", marginX=10, marginY=10)

        self.closeButton = Button(self, "✕")
        self.closeButton.onCommand(self.close)

        if useSunValley:
            self.closeButton.buttonUseSunValleyTitleBarStyle()
            self.frameUseSunValleyCardStyle()

        if closable:
            self.closeButton.pack(sideType="right", marginX=8, marginY=5, paddingY=2, paddingX=0)

        self.isclose = True

        self.closefunc = closefunc

    def setCloseFunc(self, func):
        self.closefunc = func

    def open(self, paddingX=5, paddingY=5, marginX=8, marginY=5):
        self.isclose = False
        self.pack(fillType="x", sideType="top", marginX=marginX, marginY=marginY, paddingX=paddingX, paddingY=paddingY)

    def close(self):
        self.isclose = True
        self.packForget()
        self.closefunc()