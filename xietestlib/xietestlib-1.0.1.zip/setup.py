# from distutils.core import setup
# setup(形参1=实参1, 形参2=实参2, ...)
# # 一般推荐使用
# from setuptools import setup
# setup(形参1=实参1, 形参2=实参2, ...)

from setuptools import setup


def readme_file():
    with open("README.rst", encoding="utf-8") as rf:
        return rf.read()


setup(name="xietestlib", version="1.0.1", description="this is a test lib666", packages=["xietestlib"],
      py_modules=["Tool"], long_description=readme_file(), author="xie",
      author_email="166@163.com", url="https://github.com/Miraclerice/python3Project", license="MIT")
