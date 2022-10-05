import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="corocorona",
    version="0.0.6",
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'corona=corona:printCorona',
        ],
    },
    author="syoshika",
    author_email="syoshika@student.42tokyo.jp",
    description="A covoid-19 tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sho-yoshikawa/corocorona",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
