import pathlib
from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent.resolve()
install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

VERSION='0.0.4'
DESCRIPTION = 'Auto sorting tool to allow you organise any file or folder in a directory using the file extensions'

setup(
    name="sortmyfolder",
    version=VERSION,
    author="Emmanuel Agyapong",
    author_email="emmanuelagyapong070@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=install_requires,
    keywords=['python', 'automation', 'sorting'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'sortmyfolder=auto_group.determine_location:main'
        ],
    },
)