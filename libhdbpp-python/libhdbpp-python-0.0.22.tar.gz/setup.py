# coding: utf-8
import setuptools

try:
	import pyhdbpp
	version = '.'.join(map(str,pyhdbpp.RELEASE))
except:
        import traceback
        traceback.print_exc()
        version = '0.0.0'

if __name__ == "__main__":
    setuptools.setup(
	name="libhdbpp-python",
    version=version,
    license='LGPL-3+',
    packages=setuptools.find_packages(),
    description="Python bindings for Tango Control System Archiving",
    long_description="hdbbpp readers for mariadb and timescaledb\n"
    "Extract data from HDB++ Tango Archiving Systems, using either "
    "MariaDB or TimeScaleDB",
    author="Sergi Rubio",
    author_email="srubio@cells.es",
    )
