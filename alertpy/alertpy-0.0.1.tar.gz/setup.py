""" Setup module for the alertpy package """
from setuptools import setup
from alertpy import __version__ as version

REQUIREMENTS = [
]
DEV_REQUIREMENTS = {
    "dev": [
    ]
}

with open("README.md", encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = "".join(readme_file.readlines())

setup(
    name="alertpy",
    version=version,
    url="https://github.com/changukshin/alertpy",
    license="MIT",
    author="Chang-Uk Shin",
    author_email="changuk.shin.1991@gmail.com",
    description="Python library to support to send various alerts/notifications",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=["notification", "alert"],
    packages=["alertpy"],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require=DEV_REQUIREMENTS,
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
)
