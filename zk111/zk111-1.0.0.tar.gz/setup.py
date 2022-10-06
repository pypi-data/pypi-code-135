
from distutils.core import setup
setup(
    name='zk111',  # 对外模块的名字
    version='1.0.0',  # 版本号
    description='测试本地发布模块',  # 描述
    author='zk',  # 作者
    author_email='2475092874@qq.com',
    py_modules=['zk_01.add', 'zk_01.sub'],  # 要发布的模块
    )
