from setuptools import setup, find_packages


setup(
    name='SimpleSoundPlayer',
    version='1.1',
    license='MIT',
    author="Pedro Szabo Silva",
    author_email='pepe.szabo.silva@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Pepe-77777/SimpleSoundPlayer',
    keywords='Sound Player',
    install_requires=[
          'python-vlc',
          'playsound',
      ],

)