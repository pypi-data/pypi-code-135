import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open("LXMF/_version.py", "r").read())

setuptools.setup(
    name="lxmf",
    version=__version__,
    author="Mark Qvist",
    author_email="mark@unsigned.io",
    description="Lightweight Extensible Message Format for Reticulum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markqvist/lxmf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['rns>=0.3.12'],
    python_requires='>=3.6',
)
