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
uripecker takes text and finds URLs.  Along
with URLs it also supports several forms
of short-hand indentifiers such as "bug 1234",
which it can also locate and translate to URLs
according to provided mapping.
"""

requires = [
    'neaty',
]

setup(
    description='uripecker - Peck them URIs out',
    license='License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
    long_description=vdk_cleanup(long_description),
    maintainer_email='Alois Mahdal <netvor+uripecker@vornet.cz>',
    name='uripecker',
    packages=['uripecker'],
    package_dir={'uripecker': 'src/uripecker'},
    url='https://gitlab.com/vornet/python/python-uripecker',
    requires=vdk_cleanup(requires),
    version='0.0.5',
)

# setup.py built with MKit 0.0.60 and vdk-pylib-0.0.10
