from Paperl.Paperui.Widgets.window import Window


__all__ = ["example", "compile", "buildExample", "buildDocs"]


docs = """
'''
title :: 设置为窗口标题

theme ::
    mode :: 设置窗口主题 ::
                    light -> 浅色模式,
                    dark -> 深色模式
    style :: 设置主题 ::
                    aqua,
                    default,
                    clam,
                    classic,
                    sunValley,
                    vista
    style-attr :: 设置主题的额外属性 ::
                                light -> 浅色模式,
                                dark -> 深色模式,
                                auto -> 自动模式
    use-mica :: 是否启用Windows11云母特效 ::
                                    True -> 启用,
                                    False -> 禁用
    use-mica-attr :: 设置Windows11云母特效的主题 ::
                                            light -> 浅色模式,
                                            dark -> 深色模式,
                                            auto -> 自动模式

headerBar ::
    mode :: 设置标题栏的模式 ::
                    ex -> 仅Windows系统
    border :: 设置窗口是否保留边框 ::
                            True -> 启用,
                            False -> 禁用
    sizeGrip :: 设置窗口是否有大小调整手柄 ::
                                    True -> 启用,
                                    False -> 禁用
    use-sunValley :: 启用SunValley主题，并对其主题进行设置 ::
                                                True -> 启用,
                                                False -> 禁用
    use-sunValley-attr :: 设置SunValley的主题配置 ::
                                            light -> 浅色模式,
                                            dark -> 深色模式,
                                            auto -> 自动模式
'''
"""


example = """
title = "Paperl"

theme = {
    "mode": "light",
    "style": "default",
    "style-attr": "auto",
    "use-mica": False,
    "use-mica-attr": "auto"
}
"""


def compile(window: Window):
    buildExample()

    def checkTitle():
        try:
            window.setTitle(title)
        except:
            pass

    def checkStyle():
        try:
            mode = theme["mode"]
        except:
            mode = "light"
        try:
            style = theme["style"]
        except:
            from sys import platform
            if platform == "win32":
                style = "vista"
            else:
                style = "default"
        try:
            style_attr = theme["style-attr"]
        except:
            style_attr = "auto"
        try:
            use_mica = theme["use-mica"]
        except:
            use_mica = False
        try:
            use_mica_attr = theme["use-mica-attr"]
        except:
            use_mica_attr = "auto"

        if mode == "dark":
            window.setDarkTheme()
        else:
            window.setLightTheme()

        if use_mica:
            window.useMica(use_mica_attr)

        if style == "default":
            window.useStyleDefault()
        elif style == "sunValley":
            window.useStyleSunValley(style_attr)
        elif style == "classic":
            window.useStyleClassic()
        elif style == "clam":
            window.useStyleClam()
        elif style == "aqua":
            window.useStyleAqua()
        elif style == "vista":
            window.useStyleVista()
        else:
            from Paperl.Paperc import prWarring
            prWarring("Papers -> Compile -> This component was not found")

    def checkHeaderBar():
        try:
            mode = headerBar["mode"]
        except:
            from sys import platform
            if platform == "win32":
                mode = "ex"
            else:
                mode = ""
        if mode == "ex":
            try:
                border = headerBar["border"]
            except:
                border = True
            try:
                sizeGrip = headerBar["sizeGrip"]
            except:
                sizeGrip = False
            try:
                useSunValley = headerBar["use-sunValley"]
            except:
                useSunValley = False
            try:
                useSunValley_attr = headerBar["use-sunValley-attr"]
            except:
                useSunValley_attr = "auto"
            headerbar = window.createHeaderBarEx(border, sizeGrip)
            if useSunValley:
                headerbar.useSunValley(useSunValley_attr)
            headerbar.setTitle(window.getTitle())
        return headerbar

    try:
        from papers import title
    except:
        pass
    else:
        checkTitle()

    try:
        from papers import theme
    except:
        pass
    else:
        checkStyle()

    try:
        from papers import headerBar
    except:
        pass
    else:
        headerbar = checkHeaderBar()

    return {"headerBar": headerbar}


def buildDocs():
    from os.path import exists
    if not exists("papers-docs.py"):
        with open("papers-docs.py", "w+", encoding="gbk") as file:
            file.write(docs)
            file.close()


def buildExample():
    from os.path import exists
    if not exists("papers.py"):
        with open("papers.py", "w+", encoding="gbk") as file:
            file.write(example)
            file.close()
