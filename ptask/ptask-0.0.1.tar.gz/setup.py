"""Setup for build this cli application."""

from setuptools import setup
from setuptools import find_packages

setup(
    name="ptask",
    author="Pantless Coder (Nghia Lam)",
    author_email="nghialam@gmx.com",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/pantlesscoder/painless_project",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "ptask=ptask.__main__:main"
        ],
    },
)
