class TclAnalysis(object):
    def __init__(self):
        self.build()

    def build(self):
        from tkinter import Tcl
        self.Me = Tcl()

    def evalScript(self, Script: str = ""):
        self.Me.eval(Script)

    def call(self, __command, *args):
        self.Me.tk.call(__command, args)