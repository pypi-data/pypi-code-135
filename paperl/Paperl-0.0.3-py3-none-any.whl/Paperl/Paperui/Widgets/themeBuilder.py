class ThemeBuilder(object):
    def __init__(self):
        self.build()

    def build(self):
        from tkinter.ttk import Style
        self.Me = Style()

    def createTheme(self, themeName: str, settings=None):
        self.Me.theme_create(themeName, settings=settings)

    def settingTheme(self, themeName: str, settings=None):
        self.Me.theme_settings(themeName, settings=settings)

    def quickCreateTheme(self, themeName: str, theme):
        self.createTheme(
            themeName,
            theme
        )

    def quickTheme(self, cofigure={"padding": 3},
                   background="#f8f9fb", activeBackground="#c5c6c7", disabledBackground="#929393", pressedBackground="#a6a7a7",
                   foreground="#262626", activeForeground="#4c4c4c", disabledForeground="#000000", pressedForeground="#262626",
                   ):
        return {
            "configure": cofigure,
            "map": {
                "background": [
                    ("active", activeBackground),
                    ("!disabled", background),
                    ("focus", pressedBackground)
                ],
                "foreground": [
                    ("active", activeForeground),
                    ("!disabled", foreground),
                    ("focus", pressedForeground)
                ]
            }
        }

    def useTheme(self, themeName: str):
        self.Me.theme_use(themeName)