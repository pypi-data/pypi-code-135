# /setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oss-notice-tool",
    version="0.0.2",
    author="Haksung Jang",
    author_email="hakssung@gmail.com",
    description="generate open source software notice based on the SPDX document",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sktelecom/oss-notice-tool",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "oss-notice-tool=tool.oss_notice_tool:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)