from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.13'
DESCRIPTION = "Intuitive way of using fuzz matching in pandas"

# Setting up
setup(
    name="a_pandas_ex_fuzz",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_fuzz',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_pandas_ex_df_to_string', 'a_pandas_ex_plode_tool', 'fuzzywuzzy', 'pandas', 'rapidfuzz'],
    keywords=['debugger', 'debugging', 'fuzz', 'fuzzywuzzy'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_pandas_ex_df_to_string', 'a_pandas_ex_plode_tool', 'fuzzywuzzy', 'pandas', 'rapidfuzz'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*