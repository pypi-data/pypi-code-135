from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.button import Button
from Paperl.Paperui.Widgets.checkButton import CheckButton


def empty():
    pass


class ToolBar(Frame):
    def __init__(self, parent: Widget):
        super().__init__(parent.Me)
        self.actions = []

    def addCommand(self, text: str = "", command=empty, marginX: int = 3, marginY: int = 3):
        action = Button(self, text=text)
        action.onCommand(command)
        action.pack(sideType="left", marginX=marginX, marginY=marginY)
        self.actions.append(action)
        return action

    def addCheck(self, text: str = "", command=empty, marginX: int = 3, marginY: int = 3):
        action = CheckButton(self, text=text)
        action.onCommand(command)
        action.pack(sideType="left", marginX=marginX, marginY=marginY)
        self.actions.append(action)
        return action

    def show(self, marginX: int = 5, marginY: int = 5):
        self.pack(fillType="x", sideType="top", marginX=marginX, marginY=marginY)