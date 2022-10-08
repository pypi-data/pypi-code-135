from distutils.core import setup

import re


def vdk_cleanup(value):
    """
    Remove unexpanded vdk-pylib macros from value
    """

    def has_macro(S):
        return (
            bool(re.match('.*__VDK_PYLIB_[A-Z][A-Z0-9_]__.*', S.strip()))
            or bool(re.match('.*__MKIT_[A-Z][A-Z0-9_]__.*', S.strip()))
        )

    def vdk_cleanup_str(value):
        if has_macro(value):
            return ''
        return value

    def vdk_cleanup_list(value):
        if len(value) == 1:
            if has_macro(value[0]):
                return []
        return value

    if type(value) is str:
        return vdk_cleanup_str(value)
    if type(value) is list:
        return vdk_cleanup_list(value)
    else:
        raise NotImplementedError(f"cannot cleanup: {type(value)}")


long_description = """
inigrep is designed to read a particular simplistic dialect of
INI configuration files.  In a sense, it can be considered as
a "grep for INIs", in that rather than parsing the file into
a typed memory structure for later access, it passes file each
time a query is done, and spits out relevant parts; treating
everything as text.  Hence, it's not intended as replacement
for a full-blown configuration system but rather a quick & dirty
"swiss axe" for quick & dirty scripts.
"""

requires = [
    '__VDK_PYLIB_REQUIRES_PYSTUFF__',
]

setup(
    description='inigrep - grep for (some) INIs',
    license='License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
    long_description=vdk_cleanup(long_description),
    maintainer_email='Alois Mahdal <netvor+inigrep@vornet.cz>',
    name='inigrep',
    packages=['inigrep'],
    package_dir={'inigrep': 'src/inigrep'},
    url='https://gitlab.com/vornet/python/python-inigrep',
    requires=vdk_cleanup(requires),
    version='0.3.0',
)

# setup.py built with MKit 0.0.60 and vdk-pylib-0.0.10
