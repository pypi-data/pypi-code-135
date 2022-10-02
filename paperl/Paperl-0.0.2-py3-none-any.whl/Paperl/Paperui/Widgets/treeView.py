from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperc import prDebugging, prError, prSuccess


def empty():
    pass


class TreeView(Widget):
    __name__ = "Toplevel"

    def __init__(self, parent: Widget, columns: str | list[str] | tuple[str, ...] = None):
        self.build(parent.Me, columns)

    def build(self, parent, columns: str | list[str] | tuple[str, ...]) -> None:
        from tkinter.ttk import Treeview
        self.Me = Treeview(parent, columns=columns)

    def createHeading(self, column: int | str, text: str = "", command=empty):
        self.Me.heading(column, text=text, command=command)

    def createColumn(self, column: int | str):
        self.Me.column(column)

    def insertColumn(self, parent: str, index="end", text: str = ..., list: list = ..., tags=...):
        self.Me.insert(parent=parent, index=index, text=text, values=list, tags=tags)

    def bindTag(self, tagName=..., eventName=..., eventFunc=empty):
        self.Me.tag_bind(tagName, eventName, eventFunc)

    def setShowMode(self, mode):
        self.Me.configure(show=mode)

    def getSelection(self):
        return self.Me.selection()

    def onCommand(self, eventFunc: None = ...):
        self.Me.configure(command=eventFunc)