import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_BiliRequestAll",
    version="0.1.1",
    author="Shadow403",
    author_email="anonymous_hax@foxmail.com",
    description="use bilibili uid join in group",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shadow403/nonebot_plugin_BiliRequestAll.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'nonebot-adapter-onebot >= 2.0.0b1',
        'nonebot2 >= 2.0.0b1',
    ],
    classifiers=(
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
