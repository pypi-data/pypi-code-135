# package_test\__init__.py
from .pkg_1 import *   # 从同级目录的pkg_1模块中调用所有元素
from .test1 import *   # 从同级目录的test1模块（test1\__init__.py将test1文件夹变为一个Python模块）中调用所有元素（即test1\__init__.py调用的元素）
# file_name = 'package_test'