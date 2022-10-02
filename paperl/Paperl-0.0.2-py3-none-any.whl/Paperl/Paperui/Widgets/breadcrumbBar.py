from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.button import Button
from Paperl.Paperui.Widgets.label import Label


class BreadcrumbBar(Frame):
    def __init__(self, parent: Widget):
        """
        from Paperl import *


Application = Application()


Window = Window()


Window.useStyleSunValley(STYLE_LIGHT)


Page = Page(Window)


BreadcrumbBar1 = BreadcrumbBar(Page)


BreadcrumbBar1.add("Home", "", "Home").buttonUseSunValleyTitleBarStyle()


BreadcrumbBar1.add("System", "System/", "System").buttonUseSunValleyTitleBarStyle()


BreadcrumbBar1.add("Admin", "Admin/", "Admin").buttonUseSunValleyTitleBarStyle()


BreadcrumbBar2 = BreadcrumbBar(Page)


BreadcrumbBar2.add("Home", "", "Home").buttonUseSunValleyTitleBarStyle()


BreadcrumbBar2.add("Windows", "Windows/", "Windows").buttonUseSunValleyTitleBarStyle()


BreadcrumbBar1.pack(fillType=FILL_WIDTH, sideType=SIDE_TOP, marginX=5, marginY=5)


BreadcrumbBar2.pack(fillType=FILL_WIDTH, sideType=SIDE_TOP, marginX=5, marginY=5)


Page.addPage(BreadcrumbBar1, "1")


Page.addPage(BreadcrumbBar2, "2")


Page.showPage("1")


Page.pack(fillType=FILL_BOTH)


Application.run(Window)


        :param parent:
        """

        super().__init__(parent)
        self.actions = {}
        self.one = False

    def add(self, id: str, arrowId: str = "", text: str = ""):
        if self.one:
            actionArrow = Label(self, ">")
            actionArrow.pack(sideType="left")
            self.actions[arrowId] = actionArrow
        action = Button(self, text=text)
        action.pack(sideType="left", marginX=3)
        self.one = True
        self.actions[id] = action
        return action

    def remove(self, id: str):
        self.actions[id].packForget()

    def show(self):
        self.pack(fillType="x", sideType="top", marginX=3, marginY=3)
