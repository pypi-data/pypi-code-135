from setuptools import setup

setup(
    name='DETL_PKG',
    version='0.1.4',    
    description='A example Python package',
    url='https://github.com/navinnaik1/DecentETL',
    author='navin naik',
    author_email='navin.naik@thinkartha.com',
    license='BSD 2-clause',
    packages=['DETL_PKG'],
    install_requires=['mpi4py>=2.0',
                      'jproperties==2.1.1','pandas==1.4.3','pandas-datareader==0.10.0','redis==4.3.4','requests==2.28.1','toolz==0.12.0','urllib3==1.26.10'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)