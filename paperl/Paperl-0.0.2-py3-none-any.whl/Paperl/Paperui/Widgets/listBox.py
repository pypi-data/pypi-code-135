from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.treeView import TreeView
from Paperl.Paperui.Widgets.constant import TREEVIEW_SHOW_MODE_TREE


def empty():
    pass


class ListBox(TreeView):
    __name__ = "Toplevel"

    def __init__(self, parent: Widget):
        super().__init__(parent)
        self.setShowMode(TREEVIEW_SHOW_MODE_TREE)
        self.Me.configure()

    def addItem(self, index="end", text: str = "", tagName: str = ""):
        self.insertColumn("", index, text=text, tags=tagName)

    def bindItem(self, tagName=..., eventName=..., eventFunc=empty):
        self.bindTag(tagName, eventName, eventFunc)