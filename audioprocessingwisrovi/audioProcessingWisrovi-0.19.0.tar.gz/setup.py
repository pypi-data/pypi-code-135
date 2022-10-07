from setuptools import setup, find_packages
#from distutils.core import setup

with open ( "README.md" , "r" ) as fh :
    long_description = fh.read ()

setup(
    name = "audioProcessingWisrovi",
    packages = ["ProcessAudio"],
    include_package_data=True,
    version = "0.19.0",
    description = "Procesamiento de audios",
    long_description = long_description ,
    long_description_content_type = "text/markdown" ,
    author = "William Rodriguez",
    author_email = "wisrovi.rodriguez@gmail.com",
    license="GPLv3",
    url = "https://github.com/wisrovi/ProcessAudio",
    download_url = "http://chardet.feedparser.org/download/python3-chardet-1.0.1.tgz",
    keywords = ["encoding", "i18n", "xml"],
    install_requires=['librosa', 'matplotlib'], #external packages as dependencies
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)", 
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", 
        "Intended Audience :: Developers", 
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)