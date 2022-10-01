import setuptools
from pathlib import Path

setuptools.setup(
    install_requires=[
        'pandas ==1.4.4',
        'SQLAlchemy==1.4.41'
    ],
    name="BFPAPERdbhandler",
    version=0.0,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests"])
)
