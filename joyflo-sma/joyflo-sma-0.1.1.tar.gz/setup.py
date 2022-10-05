from distutils.core import setup
setup(
  name = 'joyflo-sma',         # How you named your package folder (MyLib)
  packages = ['joyflo'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Some description',   # Give a short description about your library
  author = 'smahmed',                   # Type in your name
  author_email = 'flojoy@email.com',      # Type in your E-Mail
  url = 'https://github.com/flojoy-io/flojoy-python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/flojoy-io/flojoy-python/archive/refs/heads/main.zip',    # I explain this later on
  keywords = ['flojoy', 'visual', 'python-visual'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'python-box',
          'networkx',
          'numpy',
          'redis',
          'rq',
          'scipy',
          'pytest'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)