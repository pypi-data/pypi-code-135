import setuptools
setuptools.setup(
    name='singularitylib',#库名
    version='0.0.7',#版本号，建议一开始取0.0.1
    author='Singularity',#你的名字，名在前，姓在后，例：张一一 Yiyi Zhang
    author_email='zhw521024@outlook.com',#你的邮箱（任何邮箱都行，只要不是假的）
    description='奇点库，功能整合',#库介绍
    long_descripition_content_type="text/markdown",
    url='https://github.com/',
    packages=setuptools.find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent" ,
    ],
)
