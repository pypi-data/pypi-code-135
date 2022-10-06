from win32gui import *
from win32con import *


class Widget(object):
    def buildClass(self, className: str = "Widget"):
        self.windowClass = WNDCLASS()
        self.windowClass.lpszClassName = className
        self.windowClass.hbrBackground = COLOR_BTNFACE + 1
        self.windowClass.lpfnWndProc = self.windowProc
        self.windowAtom = RegisterClass(self.windowClass)
        return self.windowAtom

    def build(self, classAtom, windowName: str = "Widget", windowStyle: str = WS_OVERLAPPEDWINDOW,
              windowPos=(CW_USEDEFAULT, CW_USEDEFAULT), windowSize=(CW_USEDEFAULT, CW_USEDEFAULT),
              windowParent=None, windowMenu=0, windowInstance=0, param=None):
        self.hWnd = CreateWindow(
            classAtom, windowName, windowStyle,
            windowPos[0], windowPos[1],
            windowSize[0], windowSize[1],
            windowParent, windowMenu, param
        )

    def windowProc(self, hWnd, message, wParam, lParam):
        if message == WM_DESTROY:
            self.eventDestroy()
        elif message == WM_PAINT:
            self.eventPaint()
        elif message == WM_CLOSE:
            self.eventClose()
        elif message == WM_CREATE:
            self.eventCreate()
        return DefWindowProc(hWnd, message, wParam, lParam)
