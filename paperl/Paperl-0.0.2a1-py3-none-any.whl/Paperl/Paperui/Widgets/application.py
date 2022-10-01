class Application(object):
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