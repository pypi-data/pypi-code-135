try:
    DWMWA_NCRENDERING_ENABLED = 1
    DWMWA_NCRENDERING_POLICY = 2
    DWMWA_TRANSITIONS_FORCEDISABLED = 3
    DWMWA_ALLOW_NCPAINT = 4
    DWMWA_CAPTION_BUTTON_BOUNDS = 5
    DWMWA_NONCLIENT_RTL_LAYOUT = 6
    DWMWA_FORCE_ICONIC_REPRESENTATION = 7
    DWMWA_FLIP3D_POLICY = 8
    DWMWA_EXTENDED_FRAME_BOUNDS = 9
    DWMWA_HAS_ICONIC_BITMAP = 10
    DWMWA_DISALLOW_PEEK = 11
    DWMWA_EXCLUDED_FROM_PEEK = 12
    DWMWA_CLOAK = 13
    DWMWA_CLOAKED = 14
    DWMWA_FREEZE_REPRESENTATION = 15
    DWMWA_PASSIVE_UPDATE_MODE = 16
    DWMWA_USE_HOSTBACKDROPBRUSH = 17
    DWMWA_CAPTION_COLOR = 19
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    DWMWA_LAST = 24
    DWMWA_WINDOW_CORNER_PREFERENCE = 33
    DWMWA_BORDER_COLOR = 34
    DWMWA_TEXT_COLOR = 36
    DWMWA_VISIBLE_FRAME_BORDER_THICKNESS = 37
    DWMWA_SYSTEMBACKDROP_TYPE = 38

    DWMSBT_AUTO = 0
    DWMSBT_NONE = 1
    DWMSBT_MAINWINDOW = 2
    DWMSBT_TRANSIENTWINDOW = 3
    DWMSBT_TABBEDWINDOW = 4

    DWMNCRP_USEWINDOWSTYLE = 0
    DWMNCRP_DISABLED = 1
    DWMNCRP_ENABLED = 2
    DWMNCRP_LAS = 3

    DWMWCP_DEFAULT = 0
    DWMWCP_DONOTROUND = 1
    DWMWCP_ROUND = 2
    DWMWCP_ROUNDSMALL = 3
except:
    pass

try:
    from Paperl.Paperc import prError
    from ctypes import windll, Structure
    from ctypes import c_int, byref, sizeof
except:
    pass
else:
    class Margins(Structure):
        _fields_ = [
            ("cxLeftWidth", c_int),
            ("cxRightWidth", c_int),
            ("cyTopHeight", c_int),
            ("cyBottomHeight", c_int),
        ]

    def dwmSetWindowAttribute(hWnd, attributeName, attributeValue):
        try:
            return windll.dwmapi.DwmSetWindowAttribute(
                hWnd,
                attributeName,
                byref(c_int(attributeValue)),
                sizeof(c_int(attributeValue))
            )
        except:
            prError("DwmSetWindowAttribute -> The property is not supported or the value is incorrect")

    def dwmGetWindowAttribute(hWnd, attributeName):
        try:
            return windll.dwmapi.DwmGetWindowAttribute(
                hWnd,
                attributeName,
                sizeof(c_int(attributeName))
            )
        except:
            prError("DwmGetWindowAttribute -> The property is not supported or the value is incorrect")

    def dwmExtendFrameIntoClientArea(hWnd, Margin):
        try:
            return windll.dwmapi.DwmExtendFrameIntoClientArea(
                hWnd,
                byref(Margin)
            )
        except:
            prError("DwmExtendFrameIntoClientArea -> The property is not supported or the value is incorrect")