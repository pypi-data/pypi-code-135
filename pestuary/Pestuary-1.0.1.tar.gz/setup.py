from setuptools import setup, find_packages

setup(
        name="Pestuary",
        version="1.0.1",
        py_modules="pestuary",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
                'Click',
                "estuary_client",
                "requests",
            ],
        entry_points='''
            [console_scripts]
            pestuary=pestuary_cli:main
        '''
)
        
