try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='redisgetapi',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    version='0.0.1',
    description='This package is used to handl redis persistence',
    license='MIT',
    author='Nicolus Rotich',
    author_email='nicholas.rotich@gmail.com',
    install_requires=[
    	"setuptools>=58.1.0",
    	"wheel>=0.36.2",
    	"redis==4.1.2",
    	"requests==2.27.1",
        "fire"
    ],
    url='https://nkrtech.com',
    download_url='https://github.com/moinonin/redisgetapi/archive/refs/heads/main.zip',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
