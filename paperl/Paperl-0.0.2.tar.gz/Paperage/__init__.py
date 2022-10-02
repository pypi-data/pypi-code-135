from Paperl import *


def main():
    app = Application()

    root = Window()
    root.removeCaption()
    root.setSystemBackdropMainWindow()
    root.useStyleSunValley()
    root.createHeaderBarEx(useSunValley=True)

    button = Button(root)
    print(button.getParent())
    button.pack()

    app.run(root)


if __name__ == '__main__':
    main()