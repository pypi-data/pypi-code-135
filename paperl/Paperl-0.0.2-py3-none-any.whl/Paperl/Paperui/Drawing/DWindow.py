from Paperl.Paperui.Widgets.widget import Widget
from typing import Literal

try:
    from tinui import TinUI


    class DWindow(Widget):
        def __init__(self, parent: Widget):
            self.build(parent.Me)

        def build(self, parent: Widget):
            self.Me = TinUI.TinUI(parent)
            self.setBackground("#ffffff")

        def addButton(self, x: int = 0, y: int = 0, text: str = "Button", anchorType="nw",
                      font: tuple[str, int] = ("微软雅黑", 10), command=None,
                      foreground: str = "#1b1b1b", background: str = "#fbfbfb",
                      borderColor="#CCCCCC", activeBorderColor="#e5e5e5",
                      activeForeground: str = "#5d5d5d", activeBackground: str = "#f5f5f5"):
            me = self.Me.add_button(pos=(x, y), text=text, anchor=anchorType, font=font, command=command,
                                    bg=background, fg=foreground, activebg=activeBackground, line=borderColor,
                                    activeline=activeBorderColor, activefg=activeForeground)
            print(me)
            return {"button": me[2], "id": me[3]}

        def addRoundButton(self, x: int = 0, y: int = 0, text: str = "Button", anchorType="nw",
                           font: tuple[str, int] = ("微软雅黑", 10), command=None,
                           foreground: str = "#1b1b1b", background: str = "#fbfbfb",
                           borderColor="#CCCCCC", activeBorderColor="#e5e5e5",
                           activeForeground: str = "#5d5d5d", activeBackground: str = "#f5f5f5"):
            me = self.Me.add_button2(pos=(x, y), text=text, anchor=anchorType, font=font, command=command,
                                     bg=background, fg=foreground, activebg=activeBackground, line=borderColor,
                                     activeline=activeBorderColor, activefg=activeForeground)
            return {"button": me[0], "id": me[4]}

        def addTooltip(self, widget: int = 100, foreground: str = "#3b3b3b", background: str = "#e7e7e7",
                       borderColor="#e1e1e1", width: int = 400,
                       text: str = "Button", delay: int = 0.08,
                       font: tuple[str, int] = ("微软雅黑", 10)):
            me = self.Me.add_tooltip(width=width, uid=widget["id"], bg=background, fg=foreground, font=font,
                                     text=text, delay=delay, outline=borderColor)
except:
    pass
