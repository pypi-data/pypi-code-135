from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.11'
DESCRIPTION = "Get repeated capture groups, search without having to fear Exceptions in any df/Series, convert results to appropriate dtypes, use fast Trie regex"

# Setting up
setup(
    name="a_pandas_ex_regex_enhancements",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_regex_enhancements',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_pandas_ex_df_to_string', 'a_pandas_ex_less_memory_more_speed', 'a_pandas_ex_plode_tool', 'a_pandas_ex_string_to_dtypes', 'flatten_everything', 'numpy', 'pandas', 'regex'],
    keywords=['pandas', 'dtypes', 'regex', 'regular expressions', 're'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_pandas_ex_df_to_string', 'a_pandas_ex_less_memory_more_speed', 'a_pandas_ex_plode_tool', 'a_pandas_ex_string_to_dtypes', 'flatten_everything', 'numpy', 'pandas', 'regex'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*