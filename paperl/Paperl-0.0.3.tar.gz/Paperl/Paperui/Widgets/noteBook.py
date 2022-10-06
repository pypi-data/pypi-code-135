from Paperl.Paperui.Widgets.widget import Widget


class NoteBook(Widget):
    def __init__(self, parent: Widget):
        self.build(parent.Me)

    def build(self, parent):
        from tkinter.ttk import Notebook
        self.Me = Notebook(parent)

    def add(self, widget: Widget, text: str = ""):
        self.Me.add(widget.Me, text=text)