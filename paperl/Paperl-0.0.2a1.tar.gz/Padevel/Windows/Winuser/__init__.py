try:
    from ctypes import windll
except:
    pass
else:
    def findWindowA(className=None, windowName=None):
        return windll.user32.FindWindowA(className, windowName)

    def getParent(hWnd):
        return windll.user32.GetParent(hWnd)