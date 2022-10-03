import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lqs-client",
    version="0.0.6",
    author="Nathan Margaglio",
    author_email="nmargaglio@carnegierobotics.com",
    description="LogQS Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carnegierobotics/LogQS-Client",
    project_urls={
        "Bug Tracker": "https://github.com/carnegierobotics/LogQS-Client/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["lqs"],
    python_requires=">=3.6",
    install_requires=[
        'autobahn==22.7.1',
        'cbor2==5.4.3',
        'fire==0.4.0',
        'python-dotenv==0.21.0',
        'requests==2.28.1',
        'Twisted==22.8.0'
    ]
)
