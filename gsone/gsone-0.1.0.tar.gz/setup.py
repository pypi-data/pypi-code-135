from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

test_deps = [
    "pytest",
]

extras = {
    'test': test_deps,
}

setup(
    name='gsone',
    use_scm_version=True,
    description="GS1 Barcode helpers",
    long_description=readme,
    author="Versada (Andrius Laukavičius)",
    author_email='andrius.laukavicius@versada.eu',
    url="https://github.com/versada/gsone",
    license='LGPLv3',
    packages=find_packages(),
    tests_require=test_deps,
    extras_require=extras,
    setup_requires=[
        'setuptools_scm',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
