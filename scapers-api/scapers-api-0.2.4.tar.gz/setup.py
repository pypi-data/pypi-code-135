import sys

import setuptools

__version__ = "0.2.4"

setuptools.setup(
    name="scapers-api",
    version=__version__,
    author="Jarod Daming",
    author_email="jmdaming@gmail.com",
    description="Allows http access to Runescape API Endpoints",
    url="https://gitlab.com/maximized/scapers_api",
    project_url={"Bug Tracker": "https://gitlab.com/maximized/scapers_api/-/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "aiohttp~=3.8.3",
        "aiolimiter~=1.0.0",
        "python-semantic-release==7.32.0",
        "python-dotenv~=0.21.0",
        "setuptools==65.4.0",
        "Unidecode~=1.3.4",
    ],
)

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass
