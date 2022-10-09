#coding=utf-8
from distutils.core import setup

setup(
    name='GZY_first',  #对外我们模块的名字
    version='1.0',  #版本号
    description="这是第一个对外发布的模块",  #描述
    author="guzhenyi",  #作者
    author_email="13967394771@163.com",  #作者邮箱
    py_modules=['GZY_first.demo1', 'GZY_first.demo2']  #要发布的模块
)