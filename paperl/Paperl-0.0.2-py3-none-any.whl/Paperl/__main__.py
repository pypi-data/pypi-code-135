import Paperl

from darkdetect import isDark

if isDark():
    theme = "dark"
else:
    theme = "light"

def test():
    def swichTheme():
        global theme
        if theme == "dark":
            theme = "light"
            Window.useStyleSunValley("light")
        elif theme == "light":
            theme = "dark"
            Window.useStyleSunValley("dark")

    Application = Paperl.Application()

    Window = Paperl.Window()
    Window.setSize(200, 50)
    Window.maximizeBox()
    Window.minimizeBox()
    Window.setTitle("")
    Window.useStyleSunValley(theme)
    Window.setSystemBackdropMainWindow()

    Window.onKey("s", lambda event: swichTheme())
    Window.onKey("S", lambda event: swichTheme())

    Label = Paperl.Label(Window, f"This is Paperl version {Paperl.__version__}")
    Label.setAnchor(Paperl.ANCHOR_CENTER)
    Label.pack(fillType=Paperl.FILL_BOTH, expandType=Paperl.EXPAND_YES)

    Application.run(Window)

if __name__ == '__main__':
    test()