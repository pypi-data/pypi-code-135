class Application(object):
    def quit(self, window):
        window.quit()

    def alwaysUpdate(self, window):
        """
        一直刷新窗口，直到窗口被销毁

        :param window: 被指定运行的窗口
        """

        window.alwaysUpdate()

    def runAsync(self, window):
        """
        异步运行窗口组件

        :param window: 被指定运行的窗口
        """

        window.runAsync()

    def run(self, window):
        """
        运行窗口组件

        :param window: 被指定运行的窗口
        """

        window.run()