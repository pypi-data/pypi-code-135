# -*- coding: utf-8 -*-
# 作者: xwy
# 时间: 2022/7/22 18:43
# 版本: python3.10
import os


def make_dirs(path):
    """
    合并路径名
    基于 os.path.join() 若无则创建
    :param path:  文件夹、文件名列表 list []
    :return: 返回路径名
    """
    path_out = ''
    for folder in path:
        path_out = os.path.join(path_out, folder)

    if not os.path.exists(path_out):
        os.makedirs(path_out)
        print('文件夹{}创建成功'.format(path_out))
    return path_out
