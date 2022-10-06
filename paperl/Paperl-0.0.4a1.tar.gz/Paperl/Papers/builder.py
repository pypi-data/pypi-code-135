from Paperl.Paperui.Widgets.window import Window


class Builder(object):
    def __init__(self, window):
        self.Window = window

    def compile(self):
        self.Window.compile()