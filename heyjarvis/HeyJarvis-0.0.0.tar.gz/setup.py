# -*- coding: utf-8 -*-
"""

@author: sagar
"""

from distutils.core import setup
setup(
  name = 'HeyJarvis',
  packages = ['HeyJarvis'],
  version = '0.0.0',
  license= 'Proprietary License',
  description = 'This is a python package for the Jarvis SDK.',
  author = 'Sagar Rao',
  author_email = 'sagar.rao@neumodlabs.com',      # Type in your E-Mail
  url = 'https://github.com/ultimatetheory/ConsultJarvis',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['Consult Jarvis', 'Jarvis Data Models', 'Building Design', 
              'Building Performance Modeling', 'Jarvis SDK',
              'EnergyPlus', 'Automation'],
  install_requires=[
          '',
          '',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'License :: Other/Proprietary License',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)