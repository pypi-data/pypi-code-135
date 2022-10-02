from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame
from Paperl.Paperc import prWarring


class WebBrowser(Frame):
    def __init__(self, parent: Widget, messagesEnabled: bool = True,
                 verticalScrollbar: str = "auto", horizontalScrollbar: bool = False):
        self.build(parent.Me, messagesEnabled, verticalScrollbar, horizontalScrollbar)

    def build(self, parent: Widget, messagesEnabled: bool = True,
              verticalScrollbar: str = "auto", horizontalScrollbar: bool = False):
        try:
            from tkinterweb.htmlwidgets import HtmlFrame
        except:
            prWarring("tkinterWeb -> Check -> Not Installed")
        else:
            self.Me = HtmlFrame(parent, messages_enabled=messagesEnabled,
                                vertical_scrollbar=verticalScrollbar, horizontal_scrollbar=horizontalScrollbar)

    def loadUrl(self, url):
        self.Me.load_url(url)

    def loadWebsite(self, web):
        self.Me.load_website(web)

    def loadFile(self, file):
        self.Me.load_file(file)