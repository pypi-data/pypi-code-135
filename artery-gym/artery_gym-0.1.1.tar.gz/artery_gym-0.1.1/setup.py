from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="artery_gym",
    version="0.1.1",
    author="Anupama Hegde",
    author_email="anupama.hegde@carissma.eu",
    description="ML-based Cellular V2X environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anupama1990/Artery-C",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_dir={"": "src"},
    data_files=[("protobuf", ["src/artery/protobuf/lte.proto"])],
    packages=["artery_gym"],
    install_requires=[
        "gym",
        "protobuf",
        "zmq",
    ],
)
