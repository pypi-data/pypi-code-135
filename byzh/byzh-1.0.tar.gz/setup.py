from setuptools import setup

setup(
 name="byzh", #pypi中的名称，pip或者easy_install安装时使用的名称
 version="1.0",
 author="Bai_Yangzihui",
 author_email="2221337045@qq.com",
 license="GPLv3",
 packages=['byzh'], # 需要打包的目录列表
 # 此项需要，否则卸载时报windows error
 zip_safe=False
)