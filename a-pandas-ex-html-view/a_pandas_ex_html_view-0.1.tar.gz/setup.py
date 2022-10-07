from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = "View/save any Pandas DataFrame/Series as HTML, works with MultiIndex as well"

# Setting up
setup(
    name="a_pandas_ex_html_view",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_html_view',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_pandas_ex_plode_tool', 'pandas', 'regex'],
    keywords=['json', 'dict', 'list', 'HTML', 'CSS'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_pandas_ex_plode_tool', 'pandas', 'regex'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*