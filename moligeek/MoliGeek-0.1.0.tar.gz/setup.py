import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MoliGeek",
    version="V0.1.0",
    author="yourmoln",
    author_email="help@api-coolplaylin.eu.org",
    description=r"MoliGeek's dependency library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    license='Apache-2.0 license',
    project_urls={
        "Bug Report": "https://github.com/CoolPlayLin/MoliGeek-Library/issues",
    },
    download_url="https://github.com/CoolPlayLin/MoliGeek-Library/releases",
    url="https://github.com/CoolPlayLin/MoliGeek-Library",
    install_requires=[
        "beautifulsoup4>=4.11.1",
        "meo>=0.0.7.2022.9.10",
        "requests>=2.28.1"

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ]
)