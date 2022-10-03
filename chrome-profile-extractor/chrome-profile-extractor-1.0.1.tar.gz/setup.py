from setuptools import setup

with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="chrome-profile-extractor",
    version="1.0.1",
    description="this package for education purpose only.",
    long_description=description,
    long_description_content_type="text/markdown",
    packages=['chrome_profile_extractor'],
    author="Han Zaw Nyein",
    author_email="hanzawnyineonline@gmail.com",
    zip_safe=False,
    url=' https://github.com/HanZawNyein/chrome-profile-extractor.git',
    install_requires=['pycryptodome==3.14.1', 'pywin32==303']
)
