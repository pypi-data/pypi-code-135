"""
Setup file for fstring_to_format
"""
from __future__ import absolute_import
import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent.resolve()

LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="fstring_to_format",
    version="0.1.1",
    description="fstring_to_format converts Python f-string expressions to .format() for backwards compatibility.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/eftalgezer/fstring_to_format",
    author="Eftal Gezer",
    author_email="eftal.gezer@astrobiyoloji.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Typing :: Typed",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="f-string, fstring, format, f-string to format converter, fstring to format converter",
    packages=["fstring_to_format"],
    install_requires=[],
    project_urls={
        "Bug Reports": "https://github.com/eftalgezer/fstring_to_format/issues",
        "Source": "https://github.com/eftalgezer/fstring_to_format/",
        "Blog": "https://beyondthearistotelian.blogspot.com/search/label/fstring_to_format",
        "Developer": "https://www.eftalgezer.com/",
    },
)
