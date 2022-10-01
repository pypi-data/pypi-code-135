from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame


class ChildWindow(Frame):
    def __init__(self, parent: Widget):
        self.build(parent.Me)

    def build(self, parent: Widget):
        import Paperl.Paperui.Extension.childWindow.childwindow

        self.Me = childwindow.Create_Window(parent, 'Console', 500, 400, 50, 50,
                                            args={'title_color': 'black', 'pass_through': False}, tc='#DADADA',
                                            style='_mac', bg='#FFFFFF')
