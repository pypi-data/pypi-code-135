from setuptools import setup, find_packages

setup(
    name="spreg-satosa-sync",
    python_requires=">=3.6",
    url="https://gitlab.ics.muni.cz/perun-proxy-aai/python/spreg-satosa-sync.git",
    description="Script to sync SATOSA clients from Perun RPC to mongoDB",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "pycryptodomex>=3.11.0,<4",
        "pymongo>=3.12.1,<4",
        "requests>=2.26.0,<3",
        "PyYAML>=6.0,<7",
    ],
)
