from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="hexlib",
    version="2.0.3",
    author="5f0",
    url="https://github.com/5f0ne/hexlib",
    description="Basic tools to read, filter, format and display hex values",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    install_requires=[

    ]
)
