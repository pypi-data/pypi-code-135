def showMessageEx(title: str = "title", message: str = "message", buttonText: str = "OK", useSunValley: bool = False, useSunValleyTheme="auto"):
    from Paperl import Toplevel, HeaderBarEx, Label, Frame, Button

    dialog = Toplevel()

    if useSunValley:
        dialog.useStyleSunValley(useSunValleyTheme)

    titlebar = HeaderBarEx(dialog, dialog, style=False)
    messageBox = Frame(titlebar, False)

    title = Label(messageBox, text=title)
    title.setFont("Microsoft YaHei", 13, "bold")
    title.pack(anchorType="nw")
    message = Label(messageBox, text=message)
    message.setFont("Microsoft YaHei", 10)
    message.pack(anchorType="nw", marginY=10)

    title.drag(dialog)
    message.drag(dialog)
    messageBox.drag(dialog)

    messageBox.pack(fillType="x", marginX=15, marginY=15)

    if useSunValley:
        if useSunValleyTheme == "auto":
            from darkdetect import isDark
            if isDark():
                messageBox.setBackground("#2b2b2b")
                titlebar.setBackground("#2b2b2b")
                title.setBackground("#2b2b2b")
                message.setBackground("#2b2b2b")
            else:
                messageBox.setBackground("#ffffff")
                titlebar.setBackground("#ffffff")
                title.setBackground("#ffffff")
                message.setBackground("#ffffff")
        if useSunValleyTheme == "light":
            messageBox.setBackground("#ffffff")
            titlebar.setBackground("#ffffff")
            title.setBackground("#ffffff")
            message.setBackground("#ffffff")
        if useSunValleyTheme == "dark":
            messageBox.setBackground("#2b2b2b")
            titlebar.setBackground("#2b2b2b")
            title.setBackground("#2b2b2b")
            message.setBackground("#2b2b2b")

    titlebar.show()

    buttonBox = Frame(dialog)

    buttonOK = Button(buttonBox, text=buttonText)
    if useSunValley:
        buttonOK.buttonUseSunValleyAccentStyle()
    buttonOK.pack(fillType="y", marginX=10, marginY=10, sideType="right", paddingX=40)

    buttonBox.pack(fillType="both")
    buttonOK.onCommand(dialog.destroy)
    dialog.setMinsize(325, 140)
    dialog.setSize(325, 120)

    return {"dialog": dialog, "titlebar": titlebar, "messageBox": messageBox, "title": title, "message": message, "buttonBox": buttonBox, "buttonOK": buttonOK}


if __name__ == '__main__':
    import Paperl
    window = Paperl.Window()
    showMessageEx("Warrings", "Your project is error", useSunValley=True, useSunValleyTheme="dark")
    window.mainLoop()
