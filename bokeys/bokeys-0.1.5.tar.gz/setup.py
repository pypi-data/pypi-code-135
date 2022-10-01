import setuptools

setuptools.setup(
        name='bokeys',  # 包名
        version='0.1.5',  # 版本
        description="",  # 包简介
        long_description=open('README.md').read(),  # 读取文件中介绍包的详细内容
        include_package_data=True,  # 是否允许上传资源文件
        author='bokey',  # 作者
        author_email='',  # 作者邮件
        url='',  # github或者自己的网站地址
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',  # 设置编写时的python版本
        ],
        python_requires='>=3.8',  # 设置python版本要求
        install_requires=[''],  # 安装所需要的库
        entry_points={
            'console_scripts': [
                ''],
        },  # 设置命令行工具(可不使用就可以注释掉)
)
