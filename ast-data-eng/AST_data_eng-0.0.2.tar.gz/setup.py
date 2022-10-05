
"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://www.freecodecamp.org/news/build-your-first-python-package/
"""

from setuptools import setup, find_packages
import pathlib

# Always prefer setuptools over distutils
here = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

VERSION = '0.0.2' 
DESCRIPTION = 'Data engineering for large scale geospatial datasets'
LONG_DESCRIPTION = 'BLAH BLAH BLAH Do later'

# Setting up
setup(
        name="AST_data_eng", # the name must match the folder name that contains modules
        version=VERSION,
        author="Celine Robinson",
        author_email="<cscrobi@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        python_requires=">=3.8",
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows"],
        url="http://github.com/celinerobi/",
        install_requires=[
            "numpy >= 1.21.2", # add any additional packages that 
            "opencv-python >= 4.5.3.56", # needs to be installed along with your package.
            "pandas >= 1.3.3",
            "matplotlib >= 3.5.1",
            "GDAL >= 3.4.1",
            "Fiona >= 1.8.20",
            "geopandas >= 0.10.2",
            "geopy >= 2.2.0",
            "rasterio >= 1.2.10",
            "rioxarray >= 0.10.1",
            "Shapely >= 1.8.1",
            "pyproj >= 3.3.0",
            "Pillow == 8.3.1",
            "progressbar2 >= 3.54.0",
            "Rtree >= 0.9.7",
            "scikit-image >= 0.16.2",
            "scikit-learn >= 1.0.2",
            "lxml >= 4.6.4",
            "tqdm >= 4.62.2"]
)

