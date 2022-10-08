from setuptools import setup, find_packages

setup(
        name="pestuary",
        version="1.0.3",
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
        
