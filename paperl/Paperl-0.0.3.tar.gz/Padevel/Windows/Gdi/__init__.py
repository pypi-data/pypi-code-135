try:
    from Paperl.Paperc import prError
    from ctypes.wintypes import RGB
except:
    pass
else:
    def rgb(red: int, green: int, blue: int):
        """
        获取RGB颜色

        :param red: 红色
        :param green: 绿色
        :param blue: 蓝色
        :return:
        """
        return RGB(red, green, blue)
