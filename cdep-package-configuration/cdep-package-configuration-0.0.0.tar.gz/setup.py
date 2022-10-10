import setuptools
from pathlib import Path

# * Read version from VERSION file
version_file = Path("VERSION")
version_file.touch()
version_content = version_file.read_text().splitlines()
VERSION = version_content[0] if len(version_content) != 0 else "0.0.0"

PACKAGE_NAME = "cdep-package-configuration"
DESCRIPTION = "cdep configuration package."
URL = ""
AUTHOR = "xxx-xxxxxx"
AUTHOR_EMAIL = "xxx-xxxxxx@xxxxxxxxx.es"
LICENSE = "UNLICENSED"
REQUIREMENTS = [
    "pydantic",
    "PyYAML",
]

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    extras_require={
        "handle": ["cdep-package-handle"],
    },
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=["Programming Language :: Python :: 3"],
)
