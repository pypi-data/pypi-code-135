class DWidget(object):
    def __init__(self):
        self.build()

    def build(self):
        from PySide6.QtWidgets import QWidget
        self.Me = QWidget()

    def gethWnd(self):
        return self.Me.winId()

    def getMe(self):
        return self.Me

    def setParent(self, parnet):
        try:
            from Padevel import setParent
        except:
            pass
        else:
            try:
                setParent(self.gethWnd(), parnet.gethWnd())
            except:
                pass

    def embedEx(self, widget):
        self.setParent(widget)

    def upDate(self):
        self.Me.update()

    def destroy(self):
        self.Me.destroy()

    def getSizeWidth(self) -> int:
        return self.Me.width()

    def getSizeHeight(self) -> int:
        return self.Me.height()

    def getPosition(self):
        return self.Me.x(), self.Me.y()

    def getPositionX(self) -> int:
        return self.Me.x()

    def getPositionY(self) -> int:
        return self.Me.y()

    def showToast(self, title: str = "",
                  message: str = "Message",
                  appName: str = "Python",
                  appIcon: str = "",
                  timeOut: int = 0):
        try:
            from plyer.utils import platform
            from plyer import notification

            notification.notify(
                title=title,
                message=message,
                app_name=appName,
                app_icon=appIcon,
                timeout=timeOut,
            )

        except:
            prError("Plyer -> Check -> Not Installed")