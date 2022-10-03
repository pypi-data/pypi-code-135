import setuptools

VERSION = '0.1.0'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='MisskeyAPI',
    version=VERSION,
    author='spla',
    author_email='llemena_obrer.0u@icloud.com',
    description='Python wrapper for Misskey API.',
    packages=['misskey'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://git.mastodont.cat/spla/MisskeyAPI',
    install_requires=['requests'],
    project_urls={
        'Bug Tracker': 'https://git.mastodont.cat/spla/MisskeyAPI/issues',
    },
    keywords='misskey api python wrapper',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Communications",
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    python_requires = ">=3.8",
)
