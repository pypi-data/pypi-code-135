from setuptools import setup
import sys

requires = ['requests>=0.10.8']

if sys.version_info < (2, 6):
    requires.append('simplejson')

setup(
    name="SignalAds",
    py_modules=['signal-ads'],
    version="0.0.0",
    description="Signal Ads Python library",
    author="Iman Naseri",
    author_email="inaseri.20@gmail.com",
    keywords=["signalads", "sms", "signal"],
    install_requires=requires
)
