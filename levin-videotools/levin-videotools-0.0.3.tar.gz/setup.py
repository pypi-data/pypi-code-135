# 本地安装命令：pip install .
# 发布到远程：python setup.py sdist bdist bdist_wheel upload -r dinglevin # souce包、二进制包、wheel包
import ast
import re

import setuptools


def get_version_string():
    with open("videotools/__init__.py", "rb") as f:
        version_line = re.search(
            r"__version__\s+=\s+(.*)", f.read().decode("UTF8")
        ).group(1)
        return str(ast.literal_eval(version_line))


def get_install_requires():
    return [
        "ffmpeg",
        "moviepy",
        "opencv_python",
        "PyYAML",
    ]


setuptools.setup(
    name="levin-videotools",
    version=get_version_string(),
    author="dinglevin",
    author_email="dinglevin@foxmail.com",
    description="视频工具",
    url="https://codeup.aliyun.com/levin/levinspace/video-tools",
    packages=setuptools.find_packages(exclude=["*test*", "*.mp3", "data"]),
    install_requires=get_install_requires(),
    entry_points={
        "console_scripts": [
            "video_text_clip = videotools.main:main",
        ],
    },
    data_files=["videotools/config/default_config.yaml"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)