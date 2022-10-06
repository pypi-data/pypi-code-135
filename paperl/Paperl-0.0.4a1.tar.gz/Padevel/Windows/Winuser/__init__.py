try:
    from ctypes import windll
    from ctypes import sizeof, c_char
    from Padevel.Windows.Core import *
except:
    pass
else:
    def findWindowA(className=None, windowName=None):
        return windll.user32.FindWindowA(className, windowName)

    def setWindowLongW(hWnd, style=GWL_STYLE, settings=None):
        return windll.user32.SetWindowLongW(hWnd, style, settings)

    def getWindowLongW(hWnd, style=GWL_STYLE):
        return windll.user32.GetWindowLongW(hWnd, style)

    def addWindowLongW(hWnd, style=GWL_STYLE, settings=None):
        setWindowLongW(hWnd, style, getWindowLongW(hWnd, style) & ~settings)

    def getParent(hWnd):
        return windll.user32.GetParent(hWnd)

    def setParent(hWnd, child):
        return windll.user32.SetParent(hWnd, child)

    def releaseCapture():
        return windll.user32.ReleaseCapture()

    def sendMessage(hWnd, message, send1, send2):
        return windll.user32.SendMessage(hWnd, message, send1, send2)

    def sendMessageA(hWnd, message, send1, send2):
        return windll.user32.SendMessageA(hWnd, message, send1, send2)

    def monitorFromPoint(pos=(0, 0)):
        return windll.user32.MonitorFromPoint(pos)

    def getMonitorInfo(monitor):
        return windll.user32.GetMonitorInfo(monitor)

    def beginPaint(hWnd, pos={0}):
        return windll.user32.BeginPaint(hWnd, pos)

    def endPaint(hWnd, pos={0}):
        return windll.user32.EndPaint(hWnd, pos)

    def drawText(Hdc, text: str):
        return windll.user32.drawText(Hdc, text, )

    def registerClassW(windowClass):
        return windll.user32.RegisterClassW(windowClass)

    def defWindowProcW(hWnd, message, wParam, lParam):
        return windll.user32.DefWindowProcW(hWnd, message, wParam, lParam)

    def registerClassExW(windowClass):
        return windll.user32.RegisterClassExW(windowClass)

    def defWindowProcExW(hWnd, message, wParam, lParam):
        return windll.user32.DefWindowProcExW(hWnd, message, wParam, lParam)

    def createWindow(className: str = "Widget", windowName: str = "Widget", windowStyle=None,
                     windowPosX=CW_USEDEFAULT, windowPosY=CW_USEDEFAULT,
                     windowSizeWidth=CW_USEDEFAULT, windowSizeHeight=CW_USEDEFAULT,
                     windowParent=None, windowMenu=None, windowInstance=None, windowParam=None
                     ):
        from win32gui import CreateWindow
        return CreateWindow(className, windowName, windowStyle,
                            windowPosX, windowPosY, windowSizeWidth, windowSizeHeight,
                            windowParent, windowMenu, windowInstance, windowParam
                            )

    def pumpMessages():
        return windll.user32.PumpMessages()

