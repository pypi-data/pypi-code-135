from Paperl.Paperui.Widgets.constant import *
from Paperl.Paperc import prDebugging, prError


class EventHandle(object):
    def __init__(self):
        self.build()

    def build(self):
        from tkinter import Widget
        try:
            self.Me = Widget()
        except:
            pass

    def waitEvent(self, eventTime: int, eventFunc: None = ...):
        try:
            return self.Me.after(eventTime, eventFunc)
        except:
            prError("Widget -> Bind -> Please confirm whether the eventTime is correct or the eventFunc is wrong")

    def bindEvent(self, eventName=None, eventFunc: None = ..., add=None):
        try:
            return self.Me.bind(eventName, eventFunc, add=add)
        except:
            prError("Widget -> Bind -> Please confirm whether the eventName is correct or the eventFunc is wrong")

    def unBindEvent(self, eventName=None, eventId: str = None):
        try:
            return self.Me.unbind(eventName, eventId)
        except:
            prError("Widget -> UnBind -> Please confirm whether the eventName is correct or the eventFunc is wrong")

    # Event Button

    def onButtonLeft(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonLeft")
        return self.bindEvent(EVENT_BUTTON1, eventFunc)

    def onButtonMiddle(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonMiddle")
        return self.bindEvent(EVENT_BUTTON2, eventFunc)

    def onButtonRight(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonRight")
        return self.bindEvent(EVENT_BUTTON3, eventFunc)

    def onButtonAll(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonAll")
        return self.bindEvent(EVENT_BUTTON_ALL, eventFunc)

    def onButtonPress(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonPress")
        return self.bindEvent(EVENT_BUTTON_PRESS, eventFunc)

    # Event Button Release

    def onButtonReleaseLeft(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonReleaseLeft")
        return self.bindEvent(EVENT_BUTTON1_RELEASE, eventFunc)

    def onButtonReleaseMiddle(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonReleaseMiddle")
        return self.bindEvent(EVENT_BUTTON2_RELEASE, eventFunc)

    def onButtonReleaseRight(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonReleaseRight")
        return self.bindEvent(EVENT_BUTTON3_RELEASE, eventFunc)

    def onButtonReleaseAll(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonReleaseAll")
        return self.bindEvent(EVENT_BUTTON_ALL_RELEASE, eventFunc)

    # Event Button Double

    def onButtonDoubleLeft(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonDoubleLeft")
        return self.bindEvent(EVENT_BUTTON1_DOUBLE, eventFunc)

    def onButtonDoubleMiddle(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonDoubleMiddle")
        return self.bindEvent(EVENT_BUTTON2_DOUBLE, eventFunc)

    def onButtonDoubleRight(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonDoubleRight")
        return self.bindEvent(EVENT_BUTTON3_DOUBLE, eventFunc)

    def onButtonDoubleAll(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonDoubleAll")
        return self.bindEvent(EVENT_BUTTON_ALL_DOUBLE, eventFunc)

    def onButtonDoublePress(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonDoublePress")
        return self.bindEvent(EVENT_BUTTON_PRESS_DOUBLE, eventFunc)

    # Event Button Triple

    def onButtonTripleLeft(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonTripleLeft")
        return self.bindEvent(EVENT_BUTTON1_TRIPLE, eventFunc)

    def onButtonTripleMiddle(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonTripleMiddle")
        return self.bindEvent(EVENT_BUTTON2_TRIPLE, eventFunc)

    def onButtonTripleRight(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonTripleRight")
        return self.bindEvent(EVENT_BUTTON3_TRIPLE, eventFunc)

    def onButtonTripleAll(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonTripleAll")
        return self.bindEvent(EVENT_BUTTON_ALL_TRIPLE, eventFunc)

    def onButtonTriplePress(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonTriplePress")
        return self.bindEvent(EVENT_BUTTON_PRESS_TRIPLE, eventFunc)

    # Event Widget

    def onDestroy(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onDestroy")
        return self.bindEvent(EVENT_DESTROY, eventFunc)

    def onKey(self, key: str = "", eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onKey")
        return self.bindEvent(f"<{key}>", eventFunc)

    def onEnter(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onEnter")
        return self.bindEvent(EVENT_ENTER, eventFunc)

    def onLeave(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onLeave")
        return self.bindEvent(EVENT_LEAVE, eventFunc)

    def onFocusIn(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onFocusIn")
        return self.bindEvent(EVENT_FOCUS_IN, eventFunc)

    def onFocusOut(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onFocusOut")
        return self.bindEvent(EVENT_FOCUS_OUT, eventFunc)

    def onConfigure(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onConfigure")
        return self.bindEvent(EVENT_CONFIGURE, eventFunc)

    def onDropFiles(self, eventFunc=None, unicode: bool = False):
        try:
            from windnd import hook_dropfiles
        except:
            pass
        else:
            hook_dropfiles(tkwindow_or_winfoid=self.Me, func=eventFunc, force_unicode=unicode)