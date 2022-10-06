from win32gui import *
from win32con import *
from Paperl.Paperw.widget import Widget


class Window(Widget):
    def __init__(self, className: str = ..., windowName: str = "Window", windowStyle: str = WS_OVERLAPPEDWINDOW,
                 windowPos: tuple[int, int] = (CW_USEDEFAULT, CW_USEDEFAULT),
                 windowSize: tuple[int, int] = (CW_USEDEFAULT, CW_USEDEFAULT),
                 windowParent=None,
                 windowMenu: int = 0,
                 ):
        super().__init__()

        self.build(self.buildClass(className=className), windowName=windowName, windowStyle=windowStyle)


if __name__ == '__main__':
    Window = Window()
