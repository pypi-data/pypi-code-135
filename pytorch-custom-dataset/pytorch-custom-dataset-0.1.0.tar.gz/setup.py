from setuptools import setup

setup(
    name='pytorch-custom-dataset',
    version='0.1.0',    
    description='build a pytorch custom dataset in two steps',
    url='https://github.com/shuds13/pyexample',
    author='Max Ng',
    author_email='maxnghello@gmail.com',
    license='',
    packages=['pytorchdataset'],
    install_requires=['numpy>=1.19.2',
                        'Pillow>=9.2.0',
                        'spacy>=3.4.1',
                        'torch>=1.12.1',
                        'torchvision>=0.13.1',
                        'transformers>=4.21.2'                   
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)