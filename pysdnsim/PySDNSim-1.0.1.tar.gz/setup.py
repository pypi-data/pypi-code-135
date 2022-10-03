from setuptools import setup, find_packages

setup(
    name="PySDNSim",
    version="1.0.1",
    author="Yifei Ren",
    author_email="ryf0510@live.com",
    description="A SDN simulation tool uses CloudSim Plus as backend.",
    keywords=["SDN", "Microservice", "CloudSim"],
    packages=find_packages(include=["PySDNSim"]),
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
)
