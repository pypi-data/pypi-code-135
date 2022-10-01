from setuptools import setup, find_packages
import pathlib
import os

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent


def get_version():
    with open(os.path.join(HERE, "version.txt")) as f:
        version = f.read().strip().split(" ")[-1]
    return version


def read_requirements():
    with open(os.path.join(HERE, "requirements.txt")) as f:
        content = f.read()
        requirements = content.split("\n")
    return requirements


setup(
    name="phel",
    version=get_version(),
    author="kienthuc.phan@gmail.com",
    python_requires=">=3.8",
    packages=["", "phel"],
    include_package_data=True,
    package_data={
        "phel": [
            "config.toml"
        ]
    },
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        phel=phel.__main__:main
    """,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
