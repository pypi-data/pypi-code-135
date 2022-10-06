from Paperl import *


if __name__ == '__main__':
    App = Application()
    Root = Window()
    Root.setSize(800, 400)
    Root.useStyleSunValley()
    Root.setTitle("Pallery")
    Root.createHeaderBarEx(useSunValley=True, useSunValleyTheme="light")
    App.alwaysUpdate(Root)