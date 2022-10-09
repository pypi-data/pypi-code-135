# setup.py
from setuptools import setup

# setup.py
setup(
    name="testeetestee",
    version='0.1',
    description="justaquicktest",
    author="Charlie Gaynor",
    author_email="charliejackcoding@gmail.com",
    python_requires=">=3.10.1",
    install_requires=[
        'gym==0.25.0',
        'matplotlib==3.5.3',
        'torch==1.12.1',
        'numpy==1.23.2',
        ],
    packages=['test_pppackage']  
)