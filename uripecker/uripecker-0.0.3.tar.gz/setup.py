from distutils.core import setup

long_description = """
uripecker takes text and finds URLs.  Along
with URLs it also supports several forms
of short-hand indentifiers such as "bug 1234",
which it can also locate and translate to URLs
according to provided mapping.
"""

setup(
    description='uripecker - Peck them URIs out',
    license='License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
    long_description=long_description,
    maintainer_email='Alois Mahdal <netvor+uripecker@vornet.cz>',
    name='uripecker',
    packages=['uripecker'],
    package_dir={'uripecker': 'src/uripecker'},
    url='https://gitlab.com/vornet/python/python-uripecker',
    version='0.0.3',
)

# setup.py built with MKit 0.0.59 and vdk-pylib-0.0.8+t20221005222851.py3.g92cccd1
