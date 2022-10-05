from setuptools import find_packages, setup

setup(
    name="cvms",
    version="0.1.1",
    author="voi",
    author_email="develop@cvms.com",
    description=(
        "Codebase For Attention、Transfomrer、Backbone、Convolution、MLP、Re-parameter、Module"
    ),
    long_description=open("README.md", "r", encoding="utf-8").read(),
    keywords=(
        "Attention"
        "Transfomrer"
        "Backbone"
        "Convolution"
        "MLP"
        "Re-parameter"
    ),
    license="GPL-3.0",
    url="https://pypi.org/project/cvms/",
    package_dir={"": "."},
    packages=find_packages("."),
    # packages=['attention'],
    # packages=find_packages(['cvms', 'cvms.attention']),
    python_requires=">=3.7.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)