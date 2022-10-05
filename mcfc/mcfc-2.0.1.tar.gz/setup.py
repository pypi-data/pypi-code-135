from setuptools import setup
import io

with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(name='mcfc',
    author="WoidZero",
    version='2.0.1',
    url="https://github.com/woidzero/MCFC",
    description='Python module for color print using Minecraft color codes.', 
    packages=['mcfc'], 
    author_email='woidzeroo@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False)