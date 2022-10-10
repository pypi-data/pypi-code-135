from distutils.core import setup

setup(name='bhargabchipkg',
      packages = ['bhargabchipkg'],
      version='0.0.1',
      description='helpful chi-square package',
      url='https://github.com/bhargabganguli/bhargabchipkg',
      download_url = 'https://github.com/bhargabganguli/bhargabchipkg/archive/0.1.tar.gz', #FILL IN LATER
      author='Bhargab',
      author_email='bhargab.ganguli@gmail.com',
      keywords = ['chi_test',],
      license='MIT', #YOUR LICENSE HERE!

      install_requires=['pandas','numpy','scipy','math'],  #YOUR DEPENDENCIES HERE
  

      classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', # Your License Here  
        'Programming Language :: Python :: 3',    # List Python versions that you support Here  
        'Programming Language :: Python :: 3.4',
        ],
)