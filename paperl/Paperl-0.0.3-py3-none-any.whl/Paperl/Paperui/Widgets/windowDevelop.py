import sys
from functools import singledispatch

try:
    import darkdetect
except:
    pass

from Paperl.Paperc import prWarring, prSuccess, prError
from typing import Literal

try:
    from ctypes import Structure, c_int, POINTER, pointer, sizeof
    from ctypes.wintypes import DWORD, ULONG
    import ctypes
except:
    pass
else:
    class AccentPolicy(Structure):
        """ 设置客户区的具体属性 """
        _fields_ = [
            ('AccentState', DWORD),
            ('AccentFlags', DWORD),
            ('GradientColor', DWORD),
            ('AnimationId', DWORD),
        ]


    class WindowCompositionAttribute(Structure):
        _fields_ = [
            ('Attribute', DWORD),
            ('Data', POINTER(AccentPolicy)),  # POINTER()接收任何ctypes类型，并返回一个指针类型
            ('SizeOfData', ULONG),
        ]

if sys.platform == "win32":
    try:
        import win32gui
    except:
        pass
    else:
        pass


        class ExButton(object):
            def __init__(self, parent, text: str = "", pos=(10, 10), size=(100, 100), className="Button"):
                self.initEvent()
                self.build(parent, text, pos, size, className)

            def build(self, parent, text: str = "", pos=(10, 10), size=(100, 100), className="Button"):
                from win32gui import WNDCLASS, CreateWindow, RegisterClass
                from win32con import COLOR_BTNFACE, WS_VISIBLE, WS_CHILD, BS_PUSHBUTTON, WS_TABSTOP
                wnd = WNDCLASS()
                wnd.lpszClassName = className
                wnd.hbrBackground = COLOR_BTNFACE + 1
                wnd.lpfnWndProc = self.windowProc
                classAtom = RegisterClass(wnd)
                self.hWnd = CreateWindow(
                    classAtom, text, WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON | WS_TABSTOP,
                    pos[0], pos[1],
                    size[0], size[1],
                    parent.gethWnd(), None, parent.gethWnd(), None)

            def initEvent(self):
                self.eventDestroy = self.quit

            def quit(self):
                from win32gui import PostQuitMessage
                PostQuitMessage(0)

            def onDestroy(self, eventFunc: None = ...):
                self.eventDestroy()

            def windowProc(self, hWnd, message, wParam, lParam):
                if message == WM_DESTROY:
                    self.eventDestroy()
                return DefWindowProc(hWnd, message, wParam, lParam)


class Windows22H2(object):
    def setTransient(self):
        self.setSystemBackdropTransientWindow()
        self.setDarkTheme()
        self.setBackground("#000000")
        self.setExtendFrameIntoClientArea(-1, -1, -1, -1)

    def setSystemBackdropNone(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_NONE
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_NONE)
        except:
            pass

    def setSystemBackdropAuto(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_AUTO
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_AUTO)
            self.windows_manage.dwm_set_window_attribute_systembackdrop_type_auto()
        except:
            pass

    def setSystemBackdropMainWindow(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_MAINWINDOW
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_MAINWINDOW)
        except:
            pass

    def setSystemBackdropTabbedWindow(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_TABBEDWINDOW
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_TABBEDWINDOW)
        except:
            pass

    def setSystemBackdropTransientWindow(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_TRANSIENTWINDOW
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_TRANSIENTWINDOW)
        except:
            pass


class Windows21H2(object):
    def setRenderingBasic(self):
        try:
            self.windows_manage.dwm_set_ncrendering_policy(1)
        except:
            pass

    def setAutoTheme(self):
        try:
            import darkdetect
            if darkdetect.isDark():
                self.setDarkTheme()
            else:
                self.setLightTheme()
        except:
            pass

    def setDarkTheme(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_USE_IMMERSIVE_DARK_MODE
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_USE_IMMERSIVE_DARK_MODE, 1)
        except:
            pass

    def setLightTheme(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_USE_IMMERSIVE_DARK_MODE
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_USE_IMMERSIVE_DARK_MODE, 0)
        except:
            pass

    def useMica(self, theme: Literal["light", "dark", "auto"] = "auto"):
        """
        启用云母特效（仅支持windows11）（需安装win32mica库）

        :param theme: 设置云母特效的主题 参考值 -> "light" "dark"
        """
        import sys
        if sys.platform == "win32" and sys.getwindowsversion().build >= 22000:
            try:
                from win32mica import ApplyMica
            except:
                prWarring("win32mica -> Check -> Not Installed")
            else:
                try:
                    def light():
                        ApplyMica(self.gethWnd(), False)
                        self.setBackground("#fcfcfc")

                    def dark():
                        ApplyMica(self.gethWnd(), True)
                        self.setBackground("#000000")

                    if theme == "auto":
                        try:
                            from darkdetect import isDark
                        except:
                            prError("darkdetect -> Check -> Not Installed")
                        else:
                            if isDark():
                                dark()
                            else:
                                light()
                    elif theme == "dark":
                        dark()
                    else:
                        light()
                except:
                    prWarring("win32mica -> Use -> Cannot be used normally")

    def setCaptionColor(self, red=0, green=0, blue=0):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_CAPTION_COLOR, rgb
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_CAPTION_COLOR, rgb(red, green, blue))
        except:
            pass

    def setBorderColor(self, red=0, green=0, blue=0):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_BORDER_COLOR, rgb
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_BORDER_COLOR, rgb(red, green, blue))
        except:
            pass

    def setTitleColor(self, red=0, green=0, blue=0):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_TEXT_COLOR, rgb
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_TEXT_COLOR, rgb(red, green, blue))
        except:
            pass

    def setRound(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_WINDOW_CORNER_PREFERENCE, DWMWCP_ROUND
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_WINDOW_CORNER_PREFERENCE, DWMWCP_ROUND)
        except:
            pass

    def setRoundSmall(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_WINDOW_CORNER_PREFERENCE, DWMWCP_ROUNDSMALL
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_WINDOW_CORNER_PREFERENCE, DWMWCP_ROUNDSMALL)
        except:
            pass

    def setRoundDoNot(self):
        try:
            from Padevel import dwmSetWindowAttribute, DWMWA_WINDOW_CORNER_PREFERENCE, DWMWCP_DONOTROUND
            dwmSetWindowAttribute(self.gethWnd(), DWMWA_WINDOW_CORNER_PREFERENCE, DWMWCP_DONOTROUND)
        except:
            pass

    def setExtendFrameIntoClientArea(self, Left, Right, Top, Bottom):
        try:
            from Padevel import dwmExtendFrameIntoClientArea, Margins
            dwmExtendFrameIntoClientArea(self.gethWnd(), Margins(Left, Right, Top, Bottom))
        except:
            pass


class WindowsAll(object):
    def registerThumbnail(self):
        try:
            import ctypes
            from win32con import NULL
            from win32gui import FindWindow
            self.RegisterThumbnail = ctypes.windll.dwmapi.DwmRegisterThumbnail
            id = self.RegisterThumbnail(self.gethWnd(),
                                        FindWindow("Program", None),
                                        None)
            if id == -2147024809:
                return False
            else:
                return True
        except:
            return None

class WindowsEffect(object):
    def __init__(self):
        self.ACCENT_DISABLED = 0,
        self.ACCENT_ENABLE_GRADIENT = 1,
        self.ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
        self.ACCENT_ENABLE_BLURBEHIND = 3,  # Aero效果
        self.ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,  # 亚克力效果
        self.ACCENT_INVALID_STATE = 5

        self.WCA_UNDEFINED = 0,
        self.WCA_NCRENDERING_ENABLED = 1,
        self.WCA_NCRENDERING_POLICY = 2,
        self.WCA_TRANSITIONS_FORCEDISABLED = 3,
        self.WCA_ALLOW_NCPAINT = 4,
        self.WCA_CAPTION_BUTTON_BOUNDS = 5,
        self.WCA_NONCLIENT_RTL_LAYOUT = 6,
        self.WCA_FORCE_ICONIC_REPRESENTATION = 7,
        self.WCA_EXTENDED_FRAME_BOUNDS = 8,
        self.WCA_HAS_ICONIC_BITMAP = 9,
        self.WCA_THEME_ATTRIBUTES = 10,
        self.WCA_NCRENDERING_EXILED = 11,
        self.WCA_NCADORNMENTINFO = 12,
        self.WCA_EXCLUDED_FROM_LIVEPREVIEW = 13,
        self.WCA_VIDEO_OVERLAY_ACTIVE = 14,
        self.WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15,
        self.WCA_DISALLOW_PEEK = 16,
        self.WCA_CLOAK = 17,
        self.WCA_CLOAKED = 18,
        self.WCA_ACCENT_POLICY = 19,
        self.WCA_FREEZE_REPRESENTATION = 20,
        self.WCA_EVER_UNCLOAKED = 21,
        self.WCA_VISUAL_OWNER = 22,
        self.WCA_LAST = 23

    def useAcrylic(self, theme="light"):
        try:
            from BlurWindow.blurWindow import GlobalBlur
        except:
            prWarring("BlurWindow -> Check -> Not Installed")
        else:
            prSuccess("BlurWindow -> Check -> Installed")
            try:
                if theme == "dark":
                    GlobalBlur(self.gethWnd(), Dark=True)
                else:
                    GlobalBlur(self.gethWnd(), Dark=False)
            except:
                prWarring("BlurWindow -> Use -> Cannot be used normally")

    def setWindowCompositionAttribute(self, Attribute):
        try:
            self.SetWindowCompositionAttribute(self.gethWnd(), Attribute)
        except:
            prError("Widget -> SetWindowCompositionAttribute -> Error")

    def setAccent(self, Accent):
        try:
            self.AccentPolicy = AccentPolicy()
            self.AccentPolicy.AccentState = Accent
        except:
            pass
        try:
            import ctypes
            self.WindowCompAttributeData = WindowCompositionAttribute()
            self.WindowCompAttributeData.Attribute = 19
            self.WindowCompAttributeData.SizeOfData = sizeof(self.AccentPolicy)
            self.WindowCompAttributeData.Data = pointer(self.AccentPolicy)
            ctypes.windll.user32.SetWindowCompositionAttribute(self.gethWnd(), pointer(self.WindowCompAttributeData))
        except TypeError:
            prError("Widget -> SetAccent -> Error")

    def useEnableGradient(self):
        self.setAccent(1)

    def useEnableTransparentGradient(self):
        self.setAccent(2)

    def useEnableBlurBehind(self):
        self.setAccent(3)

    def useEnableAcrylicBlurBehind(self):
        self.setAccent(4)

    def useAero(self):
        self.useEnableBlurBehind()


class WindowsDev(Windows21H2, Windows22H2, WindowsEffect, WindowsAll):
    pass
