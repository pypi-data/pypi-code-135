
from setuptools import setup


def readme_file():
      with open('README.rst') as rf:
            return rf.read()


setup(name='bwhu',
      version='1.0.0',
      description='this is a test lib created by QJ',   # 简单介绍包的作用
      packages=['bwhu'],   # 和setup.py 同级的文件夹中，哪些是包文件
      #py_modules=['soul','body','myheart'],  # 和setup.py 同级的文件夹中，哪些是模块文件
      author='QJ',
      author_email='qianjianghu@gmail.com',
      long_description=readme_file(),
      url= 'https://github.com/QianjiangHu/bwhu'
      )