from Paperl.Papert.Widgets.widget import DWidget


class DWindow(DWidget):
    def __init__(self):
        super().__init__()
        self.setTitle("Paperl")
        self.setSize(250, 250)

    def show(self):
        self.Me.show()

    def hide(self):
        self.Me.hide()

    def setText(self, text: str):
        self.setTitle(text)

    def getText(self):
        return self.Me.windowTitle()

    def setGeometry(self, width: int, height: int, x: int, y: int) -> None:
        self.Me.setGeometry(x, y, width, height)

    def getGeometry(self):
        return self.getSize(), self.getPosition()

    def setSize(self, width: int, height: int) -> None:
        self.Me.resize(width, height)

    def setTitle(self, title: str):
        self.Me.setWindowTitle(title)

    def getTitle(self):
        return self.Me.windowTitle()
