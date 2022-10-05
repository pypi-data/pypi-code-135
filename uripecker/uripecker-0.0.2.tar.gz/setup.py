from distutils.core import setup

long_description = """
__VDK_PYLIB_DESC_MAIN__
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
    version='0.0.2',
)

# setup.py built with MKit 0.0.59
