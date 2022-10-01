from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperui.Widgets.widget import Widget


class DragFrameEx(Frame):
    def __init__(self, parent: Widget):
        self.build(parent.Me, parent)

    def build(self, parent: Widget, window: Widget):
        from tkinter.ttk import Frame
        self.Me = Frame(parent)

        def move():
            try:
                from Padevel import releaseCapture, sendMessageA, WM_SYSCOMMAND, SC_MOVE, HTCAPTION
                releaseCapture()
                sendMessageA(window.gethWnd(), WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0)
            except:
                pass

        self.onButtonLeftMotion(lambda event: move())