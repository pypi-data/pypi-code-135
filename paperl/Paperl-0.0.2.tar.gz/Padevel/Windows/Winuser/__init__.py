try:
    from ctypes import windll
except:
    pass
else:
    def findWindowA(className=None, windowName=None):
        return windll.user32.FindWindowA(className, windowName)

    def getParent(hWnd):
        return windll.user32.GetParent(hWnd)

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