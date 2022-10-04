# -*- coding: utf-8 -*-
"""

@author: sagar
"""

from distutils.core import setup
setup(
  name = 'ConsultJarvis',         # How you named your package folder (MyLib)
  packages = ['ConsultJarvis'],   # Chose the same as "name"
  version = '0.0.0',      # Start with a small number and increase it with every change you make
  license= 'Proprietary License',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'ConsultJarvis description.',   # Give a short description about your library
  author = 'Sagar Rao',                   # Type in your name
  author_email = 'sagar.rao@neumodlabs.com',      # Type in your E-Mail
  url = 'https://github.com/ultimatetheory/ConsultJarvis',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['Jarvis', 'Jarvis Data Models', 'Building Design', 
              'Building Performance Modeling',
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