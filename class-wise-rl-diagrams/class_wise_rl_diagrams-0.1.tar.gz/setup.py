from distutils.core import setup
setup(
  name = 'class_wise_rl_diagrams',         # How you named your package folder (MyLib)
  packages = ['class_wise_rl_diagrams'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Libraray to generate multiple classwise calibration diagrams for multi-class classification domain',   # Give a short description about your library
  author = 'Sanskar Gupta',                   # Type in your name
  author_email = 'snskr95@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Sanskar95/class_wise_rl_diagrams',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Sanskar95/class_wise_rl_diagrams/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['Calibration', 'Uncertainty', 'Confidence'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'matplotlib'
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