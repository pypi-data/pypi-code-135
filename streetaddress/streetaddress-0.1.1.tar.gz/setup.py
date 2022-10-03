from distutils.core import setup

setup(
    name="streetaddress",
    version="0.1.1",
    description="A Python port of the Perl address parser.",
    author="Mike Jensen",
    url="https://github.com/ArcadiaPower/python-streetaddress",
    keywords="streetaddress",
    packages=["streetaddress"],
    install_requires=["regex>=2021.10.8,<=2022.9.13"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
    ],
)
