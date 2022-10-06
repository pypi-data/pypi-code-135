from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='syncs3',
    version='0.0.1',    
    description='A package to give a document sync experience(and eficciency) like "repo sync", or "awscli s3 sync", and so forth.',
    url='https://github.com/TechnocultureResearch/syncs3',
    py_modules=['syncs3'],
    author='Technoculture',
    author_email='tanishaagrawal2015@gmail.com',
    license='MIT License',
    package_dir={'':'syncs3'},
    setup_requires=['wheel'],
    install_requires=[
        'boto3>=1.24.87',
        ],

    long_description = long_description,
    long_description_content_type = "text/markdown",
    extra_require = {
            "dev": [
                "pytest>=3.7",
                ],
            },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',   
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)