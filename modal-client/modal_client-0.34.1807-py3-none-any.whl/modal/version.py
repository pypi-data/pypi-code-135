# This file is executed by setup.py
#
# This is used by:
# * setup.py: defines a package version (will later affect PyPI)
# * client connection: it sends the version to the server
# * web: set the URL for the package
# * base image builder: use this as the path for package

# We use the GITHUB_RUN_NUMBER as a patch number, to create unique versions for each release
import os

major_number = 0
minor_number = 34  # Bump this on breaking changes
patch_number = int(os.environ.get("GITHUB_RUN_NUMBER", "0"))

__version__ = f"{major_number}.{minor_number}.{patch_number}"
