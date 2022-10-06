from Paperl.Paperui.Widgets.eventHandle import EventHandle
from Paperl.Paperui.Widgets.themes import Themes
from Paperl.Paperc import prError, prDebugging, prWarring, prSuccess


class Widget(EventHandle, Themes):

    __name__ = "Widget"

    style = "None"

    def __init__(self):
        self.style = "None"
        super().__init__()

    def getStyle(self):
        return self.style

    def drag(self, window):
        def move():
            try:
                from Padevel import releaseCapture, sendMessageA, WM_SYSCOMMAND, SC_MOVE, HTCAPTION
                releaseCapture()
                sendMessageA(window.gethWnd(), WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0)
            except:
                pass

        self.onButtonLeftMotion(lambda event: move())

    def loadSvg(self):
        from tksvg import load
        load(self.Me)

    def setOrient(self, orient):
        from tkinter import TclError
        try:
            self.Me.configure(orient=orient)
        except TclError:
            prError("Widget -> Orient -> This property is not supported or this value is not supported")

    def getOrient(self):
        from tkinter import TclError
        try:
            return self.Me.cget("orient")
        except TclError:
            prError("Widget -> Orient -> This property is not supported or this value is not supported")

    def setVerticalScrollBar(self, scrollBar):
        from tkinter import TclError
        try:
            self.Me.configure(yscrollcommand=scrollBar.setValue)
        except TclError:
            prError("Widget -> VerticalScrollBar -> This property is not supported or this value is not supported")

    def setHorizontalScrollBar(self, scrollBar):
        from tkinter import TclError
        try:
            self.Me.configure(xscrollcommand=scrollBar.setValue)
        except TclError:
            prError("Widget -> HorizontalScrollBar -> This property is not supported or this value is not supported")

    def verticalView(self, *args):
        return self.Me.yview()

    def horizontalView(self, *args):
        return self.Me.xview()

    def getParent(self):
        return self.Me.winfo_parent()

    def register(self, func=None):
        self.Me.register(func=func)

    def setMe(self, Widget):
        self.Me = Widget

    def asyncHandle(self):
        try:
            from async_tkinter_loop import async_handler
            async_handler()
        except:
            pass

    def getMe(self):
        return self.Me

    def upDate(self):
        self.Me.update()

    def build(self):
        from tkinter import Widget
        try:
            self.Me = Widget()
        except:
            pass
        prDebugging("Widget -> Create")

    def setFocus(self):
        self.Me.focus()

    def setParent(self, parnet):
        try:
            from Padevel import setParent
        except:
            pass
        else:
            try:
                setParent(self.gethWnd(), parnet.gethWnd())
            except:
                pass

    def embedEx(self, widget):
        self.setParent(widget)

    def destroy(self):
        try:
            self.Me.destroy()
        except:
            pass

    def setState(self, state):
        from tkinter import TclError
        try:
            self.Me.configure(state=state)
        except TclError:
            prError("Widget -> State -> This property is not supported or this value is not supported")

    def useState(self, state):
        try:
            self.Me.state(state)
        except:
            pass

    def setTearOff(self, tearOff: bool):
        from tkinter import TclError
        try:
            self.Me.configure(tearoff=tearOff)
        except TclError:
            prError("Widget -> TearOff -> This property is not supported or this value is not supported")

    def getTearOff(self):
        from tkinter import TclError
        try:
            self.getAttribute("tearoff")
        except TclError:
            prError("Widget -> TearOff -> This property is not supported or this value is not supported")

    def setMenu(self, menu):
        from tkinter import TclError
        try:
            self.Me.configure(menu=menu.Me)
        except TclError:
            prError("Widget -> Menu -> This property is not supported or this value is not supported")

    def getMenu(self):
        from tkinter import TclError
        try:
            self.getAttribute("menu")
        except TclError:
            prError("Widget -> Menu -> This property is not supported or this value is not supported")

    def setFont(self, family="", size: int = 12, weight="normal"):
        from tkinter import TclError
        try:
            self.Me.configure(font=(family, size))
        except TclError:
            prError("Widget -> Font -> This property is not supported or this value is not supported")

    def tkCall(self, __command, *args):
        try:
            self.Me.tk.call(__command, args)
        except:
            prError("Widget -> Tcl -> Error")

    def useDpi(self):
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
            self.Me.tk.call('tk', 'scaling', ScaleFactor / 75)
        except:
            prError("Widget -> Tcl -> Dpi -> The system does not support DPI")

    def setBackground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(background=color)
        except TclError:
            prError("Widget -> Background -> This property is not supported or this value is not supported")

    def setActiveBackground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(activebackground=color)
        except TclError:
            prError("Widget -> ActiveBackground -> This property is not supported or this value is not supported")

    def getActiveBackground(self):
        from tkinter import TclError
        try:
            self.getAttribute("activebackground")
        except TclError:
            prError("Widget -> ActiveBackground -> This property is not supported or this value is not supported")

    def setActiveForeground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(activeforeground=color)
        except TclError:
            prError("Widget -> ActiveForeground -> This property is not supported or this value is not supported")

    def getActiveForeground(self):
        from tkinter import TclError
        try:
            self.getAttribute("activeforeground")
        except TclError:
            prError("Widget -> ActiveForeground -> This property is not supported or this value is not supported")

    def setDisabledForeground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(disabledfackground=color)
        except TclError:
            prError("Widget -> DisabledForeground -> This property is not supported or this value is not supported")

    def getDisabledForeground(self):
        from tkinter import TclError
        try:
            self.getAttribute("disabledfackground")
        except TclError:
            prError("Widget -> DisabledForeground -> This property is not supported or this value is not supported")

    def setDisabledBackground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(disabledbackground=color)
        except TclError:
            prError("Widget -> DisabledBackground -> This property is not supported or this value is not supported")

    def getDisabledBackground(self):
        from tkinter import TclError
        try:
            self.getAttribute("disabledbackground")
        except TclError:
            prError("Widget -> DisabledBackground -> This property is not supported or this value is not supported")

    def setBorder(self, width: int = 0):
        from tkinter import TclError
        try:
            self.Me.configure(border=width)
        except TclError:
            prError("Widget -> Border -> This property is not supported or this value is not supported")

    def getBorder(self):
        from tkinter import TclError
        try:
            self.getAttribute("border")
        except TclError:
            prError("Widget -> Border -> This property is not supported or this value is not supported")

    def setRelief(self, relief):
        from tkinter import TclError
        try:
            self.Me.configure(relief=relief)
        except TclError:
            prError("Widget -> Relief -> This property is not supported or this value is not supported")

    def getRelief(self):
        from tkinter import TclError
        try:
            self.getAttribute("relief")
        except TclError:
            prError("Widget -> Relief -> This property is not supported or this value is not supported")

    def setJustify(self, justifyType="left"):
        from tkinter import TclError
        try:
            self.Me.configure(justify=justifyType)
        except TclError:
            prError("Widget -> Justify -> This property is not supported or this value is not supported")

    def getJustify(self):
        from tkinter import TclError
        try:
            self.getAttribute("justify")
        except TclError:
            prError("Widget -> Justify -> This property is not supported or this value is not supported")

    def setAnchor(self, anchorType="center"):
        from tkinter import TclError
        try:
            self.Me.configure(anchor=anchorType)
        except TclError:
            prError("Widget -> Anchor -> This property is not supported or this value is not supported")

    def getAnchor(self):
        from tkinter import TclError
        try:
            self.getAttribute("anchor")
        except TclError:
            prError("Widget -> Anchor -> This property is not supported or this value is not supported")

    def setText(self, text: str):
        from tkinter import TclError
        try:
            self.Me.configure(text=text)
        except TclError:
            prError("Widget -> Text -> This property is not supported or this value is not supported")

    def getText(self):
        from tkinter import TclError
        try:
            return self.getAttribute("text")
        except TclError:
            prError("Widget -> Text -> This property is not supported or this value is not supported")

    def setImage(self, image):
        from tkinter import TclError
        try:
            self.Me.configure(image=image)
        except TclError:
            prError("Widget -> Image -> This property is not supported or this value is not supported")

    def getImage(self):
        from tkinter import TclError
        try:
            return self.getAttribute("image")
        except TclError:
            prError("Widget -> Image -> This property is not supported or this value is not supported")

    def getAttribute(self, attributeName: str):
        return self.Me.cget(attributeName)

    def setForeground(self, color):
        from tkinter import TclError
        try:
            self.Me.configure(foreground=color)
        except TclError:
            prError("Widget -> Foreground -> This property is not supported or this value is not supported")

    def getSize(self):
        return self.Me.winfo_width(), self.Me.winfo_height()

    def getId(self):
        return self.Me.winfo_id()

    def gethWnd(self):
        try:
            from Padevel.Windows.Winuser import getParent
        except:
            return None
        else:
            return getParent(self.getId())

    def getSizeWidth(self) -> int:
        return self.Me.winfo_width()

    def getSizeHeight(self) -> int:
        return self.Me.winfo_height()

    def getScreenSizeWidth(self) -> int:
        return self.Me.winfo_screenwidth()

    def getScreenSizeHeight(self) -> int:
        return self.Me.winfo_screenheight()

    def getPosition(self):
        return self.Me.winfo_x(), self.Me.winfo_y()

    def getPositionX(self) -> int:
        return self.Me.winfo_x()

    def getPositionY(self) -> int:
        return self.Me.winfo_y()

    def treeViewUseSunValleyItemStyle(self):
        try:
            self.Me.configure(style="Treeview.Item")
        except:
            prWarring(
                "Widget -> Use Item Style -> Please use the SunValley theme"
            )

    def buttonUseDafaultStyle(self):
        self.Me.configure(style="TButton")

    def buttonUseSunValleyAccentStyle(self):
        try:
            self.Me.configure(style="Accent.TButton")
        except:
            prWarring(
                "Widget -> Use Accent Style -> Please use the SunValley theme"
            )

    def buttonUseSunValleyTitleBarStyle(self):
        try:
            self.Me.configure(style="Titlebar.TButton")
        except:
            prWarring(
                "Widget -> Use TitleBar Style -> Please use the SunValley theme"
            )

    def buttonUseSunValleyTitleBarCloseStyle(self):
        try:
            self.Me.configure(style="Close.Titlebar.TButton")
        except:
            prWarring(
                "Widget -> Use TitleBarClose Style -> Please use the SunValley theme"
            )

    def buttonUseSunValleyToggleStyle(self):
        try:
            self.Me.configure(style="Toggle.TButton")
        except:
            prWarring(
                "Widget -> Use Toggle Style -> Please use the SunValley theme"
            )

    def frameUseSunValleyCardStyle(self):
        try:
            self.Me.configure(style="Card.TFrame")
        except:
            prWarring(
                "Widget -> Use Card Style -> Please use the SunValley theme"
            )

    def checkButtonUseSunValleySwichStyle(self):
        try:
            self.Me.configure(style="Switch.TCheckbutton")
        except:
            prWarring(
                "Widget -> Use Swich Style -> Please use the SunValley theme"
            )

    def setStyle(self, style):
        try:
            self.Me.configure(style=style)
        except:
            prWarring(
                "Widget -> Set Style -> Cannot"
            )

    def pack(self, paddingX: int = None, paddingY: int = None,
             marginX: int = None, marginY: int = None,
             fillType=None, expandType=None, sideType=None, anchorType=None):
        try:
            self.Me.pack(ipadx=paddingX, ipady=paddingY, padx=marginX, pady=marginY,
                         fill=fillType, expand=expandType, side=sideType, anchor=anchorType)
        except:
            prError(
                "Widget -> Pack -> This component does not support this method or the value is filled in incorrectly"
            )

    def packForget(self):
        try:
            self.Me.pack_forget()
        except:
            prError(
                "Widget -> Pack Forget -> This component does not support this method or the value is filled in incorrectly"
            )

    def place(self, x: int = None, y: int = None, width: int = None, height: int = None, anchorType=None):
        try:
            self.Me.place(x=x, y=y, width=width, height=height, anchor=anchorType)
        except:
            prError(
                "Widget -> Place -> This component does not support this method or the value is filled in incorrectly"
            )

    def placeForget(self):
        try:
            self.Me.place_forget()
        except:
            prError(
                "Widget -> Place Forget -> This component does not support this method or the value is filled in incorrectly"
                    )

    def grid(self, column: int = None, row: int = None,
             paddingX: int = 0, paddingY: int = 0,
             marginX: int = 0, marginY: int = 0,):
        try:
            self.Me.grid(column=column, row=row, ipadx=paddingX, ipady=paddingY, padx=marginX, pady=marginY)
        except:
            prError(
                "Widget -> Grid -> This component does not support this method or the value is filled in incorrectly"
            )

    def gridForget(self):
        try:
            self.Me.grid_forget()
        except:
            prError(
                "Widget -> Grid Forget -> This component does not support this method or the value is filled in incorrectly"
                    )

    def showToast(self, title: str = "",
                  message: str = "Message",
                  appName: str = "Python",
                  appIcon: str = "",
                  timeOut: int = 0):
        try:
            from tkdev4 import DevNotification
        except:
            prError("tkDev4 -> Check -> Not Installed")
        else:
            try:
                DevNotification(title, message, appName, appIcon, timeOut).show()
            except:
                prError("Plyer -> Check -> Not Installed")

    def quit(self):
        self.Me.quit()