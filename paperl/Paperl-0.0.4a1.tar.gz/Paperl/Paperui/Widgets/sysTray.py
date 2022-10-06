from Paperl.Paperc import prWarring
from Paperl.Paperui.Widgets.widget import Widget


class SysTray(object):
    def __init__(self, parent: Widget, tooltip: str = "托盘图标"):
        self.parent = parent
        self.build(parent.Me, tooltip)

    def build(self, parent, tooltip: str = "托盘图标"):
        try:
            from tkdev4.devtcl import DevTray
        except:
            prError("tkDev4 -> tkdev4 needs to be installed")
        else:
            try:
                self.Me = DevTray(parent, text=tooltip)
            except:
                prWarring("tkdev4 -> Parameter error")
            else:
                self.onProc(self.proc)

    def onProc(self, eventFunc):
        self.Me.menu_func = eventFunc

    def proc(self, event, iconId, icon, x, y):
        """
        内置菜单，用于初始化。
        """
        if event == "WM_RBUTTONDOWN":
            from Paperl.Paperui.Widgets.menu import Menu
            menu = Menu()
            menu.setBorder(0)
            menu.setTearOff(False)
            menu.addCommand(label="退出", command=self.parent.destroy)
            menu.popup(x, y)

    def add(self):
        self.Me.taskbar_add()

    def delete(self):
        self.Me.taskbar_delete()

    def deleteMe(self):
        self.Me.taskbar_delete_me()
