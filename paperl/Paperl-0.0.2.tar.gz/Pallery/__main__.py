from Paperl import *


if __name__ == '__main__':
    App = Application()
    Root = Window()
    Root.setSize(800, 400)
    Root.useStyleSunValley()
    Root.setTitle("Pallery")
    Root.createHeaderBarEx(useSunValley=True)

    Tip = InfoBar(Root, useSunValley=True, message="Welcome to Pallery !")
    Tip.setCloseFunc(lambda: print("Hello"))
    Tip.open()

    App.run(Root)