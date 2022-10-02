from Paperl.Paperui.Drawing.DWindow import DWindow
from Paperl.Paperui.Widgets.widget import Widget


try:
    from tinui import TinUI

    class DTheme:
        def __init__(self, parent: DWindow):
            self.build(parent.Me)

        def build(self, parent: Widget):
            self.Me = TinUI.TinUITheme(parent)

        def setAuto(self):
            self.Me.change_theme_name("auto")

        def setLight(self):
            self.Me.change_theme_name("light")

except:
    pass