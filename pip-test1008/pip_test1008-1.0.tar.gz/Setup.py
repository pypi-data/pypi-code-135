from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pip_test1008', # 需要打包的名字,即本模块要发布的名字
    version='v1.0',#版本
    description='A  module for test', # 简要描述
    py_modules=['pip_test1008'],   #  需要打包的模块
    author='zenghui_shu', # 作者名
    author_email='zenghui_shu@163.com',   # 作者邮件
    license='MIT',
    long_description=long_description,
)