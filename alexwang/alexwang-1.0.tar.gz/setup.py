from distutils.core import setup

packages = ['alexwang']  # 唯一的包名，自己取名
setup(name='alexwang',
      version='1.0',
      author='xyy',
      packages=packages,
      package_dir={'requests': 'requests'}, )
