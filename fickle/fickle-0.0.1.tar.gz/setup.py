from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="fickle",
    description="load pickled data as safely as possible",
    version="0.0.1",
    author="eduard",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=Path("README.md").read_text("utf-8"),
    long_description_content_type="text/markdown",
    license="LGPLv3+",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
