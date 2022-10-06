class DApplication(object):
    def __init__(self):
        self.build()

    def build(self):
        from PySide6.QtWidgets import QApplication
        self.Me = QApplication()

    def run(self, window):
        from sys import exit
        window.show()
        exit(self.Me.exec())