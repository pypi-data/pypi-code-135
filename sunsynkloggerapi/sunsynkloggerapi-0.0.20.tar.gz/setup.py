from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="sunsynkloggerapi",
    version="0.0.20", 
    description="SynSynk Logger API Python Library", 
    long_description=long_description, 
    long_description_content_type="text/markdown", 
    url="https://github.com/StickeyTape/sunsynkloggerapi", 
    author="Jacques Coetzer",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="inverter, sunsynk, logger, python, library",
    packages=find_packages(include=['sunsynkloggerapi', 'sunsynkloggerapi.*']),
    python_requires=">=3.8, <4",
    install_requires=["aiohttp", "asyncio", "voluptuous", "python-dateutil"],
    project_urls={ 
        "Bug Reports": "https://github.com/StickeyTape/sunsynkloggerapi/issues",
        "Source": "https://github.com/StickeyTape/sunsynkloggerapi/",
    },
)