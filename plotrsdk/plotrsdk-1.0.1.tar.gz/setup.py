from setuptools import setup, find_packages

long_desc = open("README.md").read()
required = ["termcolor", "requests"]
print(find_packages())
setup(
    name="plotrsdk",
    version="1.0.1",
    author="Prabhu Marappan",
    author_email="prabhum.794@gmail.com",
    description="A Python SDK for the Lord of the Rings API",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/prabhumarappan/prabhu-lotr-SDK",
    packages=find_packages(),
    install_requires=required,
    python_requires=">=3.6",
)
