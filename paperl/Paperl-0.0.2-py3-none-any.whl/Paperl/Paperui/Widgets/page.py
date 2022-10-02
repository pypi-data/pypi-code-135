from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.frame import Frame


class Page(Frame):
    def __init__(self, parent: Widget):
        super().__init__(parent)
        self.pages = {}

    def addPage(self, page: Widget, id: int = 0):
        """
        添加页面

        :param page: 页面组件
        :param id: 组件ID
        """
        self.pages[id] = page

    def showPage(self, id: int):
        """
        显示页面，会将其他页面隐藏

        :param id: 被显示的页面ID
        """
        self.pages[id].pack(fillType="both", expandType="yes")
        for item in self.pages.keys():
            if not item == id:
                self.hidePage(item)

    def hidePage(self, id: int):
        """
        内置函数，最好不要使用，因为几乎没有什么用
        """
        self.pages[id].packForget()

    def getPage(self, id: int):
        """
        获取页面

        :param id: 所要获取的页面ID
        """
        return self.pages[id]

    def getPages(self):
        """
        获取所有页面
        """
        return self.pages
