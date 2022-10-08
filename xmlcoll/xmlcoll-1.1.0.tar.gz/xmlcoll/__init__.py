"""
A package of python routines to work with data in XML format of samples.
"""
import os

os.environ["XML_CATALOG_FILES"] = os.path.join(
    os.path.dirname(__file__), "xsd_pub/catalog"
)

from xmlcoll.coll import *
from xmlcoll.base import *
