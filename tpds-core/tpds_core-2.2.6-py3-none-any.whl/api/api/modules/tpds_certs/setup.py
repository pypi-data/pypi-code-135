from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tpds_certs",
    version="1.0.0",
    author="Microchip Technology",
    author_email="SPG.Tools@microchip.com",
    description="Microchip(SPG) Trust Platform Certificates package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="#",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: Closed :: Microchip",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
