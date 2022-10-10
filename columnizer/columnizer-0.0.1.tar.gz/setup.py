import setuptools


VERSION = '0.0.1'


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='columnizer',
    version=VERSION,
    author='mr.message.writer',
    author_email='mr.message.writer@gmail.com',  # TODO: update email
    description='Simple, yet extendable ASCII text columnizer.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mrmessagewriter/columnizer',
    project_urls={
        'Bug Tracker': 'https://github.com/mrmessagewriter/columnizer/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)