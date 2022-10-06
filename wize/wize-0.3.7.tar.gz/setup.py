import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wize",
    version="0.3.7",
    author="Diwan Mohamed Faheer",
    author_email="diwanmohamedfaheer@gmail.com",
    description="Module specialising in everything...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cu3t0m/wize",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'wize=wize:main',
        ],
    },  
  
    install_requires=["colored==1.4.3"],    
)