from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.button import Button


class NavigationView(Frame):
    def __init__(self, parent: Widget):
        super().__init__(parent)
        self.actions = {}

    def add(self, id: str, text: str = "", command=...):
        action = Button(self, text=text)
        action.onCommand(command)
        action.pack(fillType="both", sideType="top", marginX=3, marginY=3)
        self.actions[id] = action
        return action

    def remove(self, id: str):
        self.actions[id].destroy()

    def show(self):
        self.pack(fillType="y", sideType="left")
