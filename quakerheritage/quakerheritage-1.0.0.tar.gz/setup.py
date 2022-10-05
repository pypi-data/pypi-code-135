import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="quakerheritage",
  version="1.0.0",
  description="",
  long_description=README,
  long_description_content_type="text/markdown",
  author="",
  author_email="",
  license="AGPL",
  packages=["quakerheritage"],
  zip_safe=False
)