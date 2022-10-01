import Paperl

def test():
    Application = Paperl.Application()

    Window = Paperl.Window()
    Window.maximizeBox()
    Window.minimizeBox()
    Window.setTitle("")
    Window.setSize(200, 50)
    Window.useStyleSunValley()
    Window.setSystemBackdropTabbedWindow()
    Label = Paperl.Label(Window, f"This is Paperl version {Paperl.__version__}")
    Label.setAnchor(Paperl.ANCHOR_CENTER)
    Label.pack(fillType=Paperl.FILL_BOTH, expandType=Paperl.EXPAND_YES)

    Application.run(Window)

if __name__ == '__main__':
    test()