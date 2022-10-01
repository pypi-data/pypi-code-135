from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(r"C:\Users\Gamer\anaconda3\envs\dfdir\_tmp_PyGitUpload_000031\README.md", encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.3'
DESCRIPTION = "Library to handle any nested iterable (list, tuple, dict, json, etc.) in Pandas - no matter how deep it is nested!"

# Setting up
setup(
    name="a_pandas_ex_plode_tool",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_plode_tool',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_pandas_ex_df_to_string', 'BruteCodecChecker', 'flatten_any_dict_iterable_or_whatsoever', 'flatten_everything', 'numpy', 'pandas', 'regex', 'ujson'],
    keywords=['flatten', 'pandas', 'dict', 'list', 'numpy', 'tuple', 'Tagsiter', 'nested', 'iterable', 'lists of lists', 'flatten json', 'iter', 'explode', 'squeeze'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_pandas_ex_df_to_string', 'BruteCodecChecker', 'flatten_any_dict_iterable_or_whatsoever', 'flatten_everything', 'numpy', 'pandas', 'regex', 'ujson'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*