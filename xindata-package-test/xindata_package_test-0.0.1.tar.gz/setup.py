# setup.py
import setuptools # 导入setuptools打包工具

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
     name="xindata_package_test"                # 必要参数
    ,version="0.0.1"                    # 必要参数，包版本号，便于维护版本
    ,packages=setuptools.find_packages() # 必要参数，源代码所在文件夹在项目根目录下
    ,author="Xin_data"                     # 作者，可以写自己的姓名
    ,author_email="jaxmin.lee@outlook.com" # 作者联系方式，可写自己的邮箱地址
    ,description="A test package"          # 包的简述
    ,long_description=long_description     # 包的详细介绍，一般在README.md文件内
    ,long_description_content_type="text/markdown"
    ,classifiers=[
         "Programming Language :: Python :: 3"
        ,"License :: OSI Approved :: MIT License"
    ]
    ,python_requires='>=3.6'               # Python版本要求
)