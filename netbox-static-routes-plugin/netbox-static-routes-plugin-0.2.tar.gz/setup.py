from setuptools import find_packages, setup

setup(
    name = 'netbox-static-routes-plugin',
    version = '0.2', # would be nice to import the version from netbox_static_routes/version.py
    description = 'Manage static routes in Netbox',
    url = 'https://github.com/jbparrish17/netbox-static-routes',
    author = 'Joshua Parrish',
    license = 'Apache 2.0',
    install_requires = [],
    packages = find_packages(),
    include_package_data = True,
    package_data = {
        'netbox_static_routes': ['templates/*/*.html']
    },
    zip_safe = False
)
