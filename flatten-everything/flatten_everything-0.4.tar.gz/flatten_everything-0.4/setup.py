from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(r"C:\Users\Gamer\anaconda3\envs\dfdir\_tmp_PyGitUpload_000027\README.md", encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.4'
DESCRIPTION = "Flattens everything - lists, tuples, dicts, np, pd... Option to protect iterables from being flattened"

# Setting up
setup(
    name="flatten_everything",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/flatten_everything',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=[],
    keywords=['flatten', 'pandas', 'dict', 'list', 'numpy', 'tuple'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=[],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*