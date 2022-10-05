from setuptools import setup, find_packages
import re


def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)

# with open("README.md", "r") as f:
#     long_description = f.read()

package_name = 'thatool'

setup(
  name = package_name,         # How you named your package folder (MyLib)
  version = get_property('__version__', package_name),
  author = get_property('__author__', package_name),   
  description = get_property('__description__', package_name),  
  long_description = get_property('__long_description__', package_name),  
  author_email = 'thangckt@gmail.com',                      

  license='MIT',                           # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  license_files = ('LICENSE.md'),
  # url = 'https://github.com/thangckt/thatool',   # Provide either the link to your github or to your website
  # download_url="https://github.com/thangckt/thatool/tarball/{}".format(__version__),    # I explain this later on
  # keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best

  packages = find_packages(),
  install_requires=[            # May not use it, due to potential conflict
          # 'scipy', 
          # 'pandas', 
          # 'matplotlib', 
          # 'numpy',
          # 'lmfit', 
          # 'shapely',
          # 'jupyterlab',
      ],

  python_requires='>=3.6',

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Topic :: Software Development',
    'Programming Language :: Python :: 3.7',
  ],

)
