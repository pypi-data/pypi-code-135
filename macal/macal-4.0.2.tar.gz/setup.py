from setuptools import setup, find_packages
import shutil
import os



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



cachepath = "macal/Library/Extern/__pycache__"
if os.path.exists(cachepath):
	shutil.rmtree(cachepath)
setup()