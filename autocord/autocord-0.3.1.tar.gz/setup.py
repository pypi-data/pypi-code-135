from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="autocord",
    version="0.3.1",
    author="walker",
    description="Discord API wrapper centered around automation",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=['autocord'],
    url="https://github.com/wa1ker38552/autocord",
    install_requires=["requests"],
    python_requires=">=3.7",
    py_modules=["autocord"]
)