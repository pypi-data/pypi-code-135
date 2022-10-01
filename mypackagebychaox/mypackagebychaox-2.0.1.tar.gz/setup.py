from distutils.core import setup
from setuptools import find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='mypackagebychaox',  # 包名(一致，不重复)
      version='2.0.1',  # 版本号
      description='A small example package',
      long_description=long_description,
      author='chaox',
      author_email='1872254902@qq.com',
      url='https://github.com/loveyoufooyou',
      install_requires=[],  # 依赖库，下载时候会额外的下载
      license='MIT License',
      packages=find_packages(),  # 找到package列表
      platforms=['all'],  # 指定平台运行，windows、Linux
      classifiers=[  # 其他信息
            'Intended Audience :: Developers',
            'Natural Language :: Chinese (Simplified)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries',
      ]

      )