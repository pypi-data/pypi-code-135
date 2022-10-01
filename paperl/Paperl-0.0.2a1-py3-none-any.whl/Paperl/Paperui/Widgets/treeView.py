from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperc import prDebugging, prError, prSuccess


class TreeView(Widget):
    __name__ = "Toplevel"

    def __init__(self, parent: Widget):
        self.build(parent.Me)

    def build(self, parent) -> None:
        from tkinter.ttk import Treeview
        self.Me = Treeview(parent)
