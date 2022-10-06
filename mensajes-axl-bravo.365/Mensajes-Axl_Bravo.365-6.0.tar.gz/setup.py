from setuptools import setup, find_packages

setup(
    name ='Mensajes-Axl_Bravo.365',
    version ='6.0',
    description ='Un paquete para saludar y despedir',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    author='Axl Bravo',
    author_email='axl@hmail.com',
    url='',
    license_files=['LICENSE'],
    packages=find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires = [paquete.strip() for paquete in open("requirements.txt").readlines()],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
