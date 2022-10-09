import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydantic-fetch",
    version="0.0.3",
    author="ed",
    author_email="ed@bayis.co.uk",
    description="Extension of pydantic models for HTTP send/recieve",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bayinfosys/pydantic-fetch",
    packages=["pydantic_fetch"],
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
      "pydantic",
    ],
    extras_require={
      "httpx": [
        "httpx",
      ],
      "tests": [
        "mock",
        "pytest",
      ]
    }
)
