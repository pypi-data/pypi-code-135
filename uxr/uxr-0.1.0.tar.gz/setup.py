from setuptools import setup, find_packages

setup(
    author="Joe Chelladurai",
    description="Quantiative User Experience Research",
    name="uxr",
    version="0.1.0",
    packages=find_packages(include=["uxr", "uxr.*"]),
    install_requires=['pandas>=1.0', 'scipy==1.1', 'matplotlib>=2.2.1,<3'],
    python_requires='>=2.7, !=3.0.*, !=3.1*',
)