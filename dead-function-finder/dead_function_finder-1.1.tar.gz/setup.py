from setuptools import setup

import pypandoc

setup(
    name='dead_function_finder',
    version='1.1',
    description='Utility to find dead functions within a codebase.',
    long_description=pypandoc.convert_file('README.md', 'rst'),
    author='Gabriel Bordeaux',
    author_email='pypi@gab.lc',
    url='https://github.com/gabfl/dead_function_finder',
    license='MIT',
    packages=['dead_function_finder', 'dead_function_finder.modules'],
    package_dir={'dead_function_finder': 'src'},
    install_requires=[],  # external dependencies
    entry_points={
        'console_scripts': [
            'dead_function_finder = dead_function_finder.dead_function_finder:main',
        ],
    },
    classifiers=[  # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        #  'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        #  'Development Status :: 5 - Production/Stable',
    ],
)
