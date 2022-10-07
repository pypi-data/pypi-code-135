from setuptools import setup
VERSION = "0.2"
DESCRIPTION = "A Python module for easily drawing turtle shapes in Python."

setup(
    name="turtlekit",
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.md", "r").read(),
    long_description_content_type = "text/markdown",
    scripts = ["turtlesuite.py"],
    install_requires = ["turtle"],
    author="Wyatt Garrioch",
    author_email="w.garrioch456@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    keywords= ["Python", "Turtle"]
)