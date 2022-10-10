import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyfii',
    version='1.1.0',
    author='细-粒体',
    url='https://www.bilibili.com/video/BV1Ee411T7YY/',
    description=u'用python编写Fii无人机程序并预览',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['opencv-python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)