from Paperl.Papert.Widgets.widget import DWidget


class DTitleBar(DWidget):
    def __init__(self, parent: DWidget):
        self.build(parent.Me)

    def build(self, parent):
        from qframelesswindow import TitleBar
        TitleBar(parent)