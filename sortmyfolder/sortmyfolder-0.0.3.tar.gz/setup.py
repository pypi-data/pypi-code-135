import pathlib
from setuptools import find_packages, setup




VERSION='0.0.3'
DESCRIPTION = 'Auto sorting tool to allow you organise any file or folder in a directory using the file extensions'
install_requires=[
    "shutil"
]


setup(
    name="sortmyfolder",
    version=VERSION,
    author="Emmanuel Agyapong",
    author_email="emmanuelagyapong070@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['shutil'],
    keywords=['python', 'automation', 'sorting'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)