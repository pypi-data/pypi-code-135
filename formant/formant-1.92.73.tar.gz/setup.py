import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="formant",
    version="1.92.73",
    author="Formant",
    author_email="eng@formant.io",
    description="Formant python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://formant.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "grpcio>=1.37.0",
        "grpcio-status>=1.37.0",
        "protobuf>=3.15.8, <=3.19.4",
        "typing-extensions>=3.7.4.2",
        "requests>=2.25.1",
        "python-lzf==0.2.4",
    ],
    python_requires=">=2.7",
)
