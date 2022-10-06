from Paperl.Paperui.Widgets.widget import Widget


class Button(Widget):
    def __init__(self, parent: Widget, text: str = ""):
        """
        按钮组件

        -----

        onCommand -> 按钮被点击的事件，无返回

        :param parent: 按钮的父组件
        :param text: 按钮的文本
        """
        self.build(parent.Me, text)

    def build(self, parent, text: str):
        from tkinter.ttk import Button
        self.Me = Button(parent, text=text)

    def onCommand(self, eventFunc: None = ...):
        self.Me.configure(command=eventFunc)