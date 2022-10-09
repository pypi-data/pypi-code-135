from skbuild import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="mumpropagator",
    version="1.0.3",
    description="A python interface to Muon Propagator package MUM, developed by Igor Sokalski",
    license="MIT",
    packages=['mumpropagator'],
    cmake_args=['-DSKBUILD=ON'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
