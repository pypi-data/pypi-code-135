# setup.py
from setuptools import find_namespace_packages, setup

# setup.py
setup(
    name="pierl",
    version='1.9',
    description="Environment Agnostic RL algorithm implementations using Pytorch.",
    author="Charlie Gaynor",
    author_email="charliejackcoding@gmail.com",
    python_requires=">=3.10.1",
    install_requires=[
        'gym==0.25.0',
        'matplotlib==3.5.3',
        'torch==1.12.1',
        'numpy==1.23.2',
        ],
    packages=['pierl']
)