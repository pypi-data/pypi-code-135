from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperc import prDebugging, prError, prSuccess


class TreeView(Widget):
    __name__ = "Toplevel"

    def __init__(self, parent: Widget, columns: str | list[str] | tuple[str, ...]):
        self.build(parent.Me, columns)

    def build(self, parent, columns: str | list[str] | tuple[str, ...]) -> None:
        from tkinter.ttk import Treeview
        self.Me = Treeview(parent, columns=columns)

    def createHeading(self, column: int | str, text: str, command=None):
        self.Me.heading(column, text=text, command=command)

    def createColumn(self, column: int | str):
        self.Me.column(column)

    def setShowMode(self, mode):
        self.Me.configure(show=mode)

    def onCommand(self, eventFunc: None = ...):
        self.Me.configure(command=eventFunc)