import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastner",
    version="0.1.3",
    author="Vittorio Maggio",
    author_email="posta.maggio@gmail.com",
    description="Finetune transformer-based models for the Named Entity Recognition task in a simple and fast way.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vittoriomaggio/fastner",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy'
        'torch',
        'transformers',
        'datasets',
        'seqeval'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)