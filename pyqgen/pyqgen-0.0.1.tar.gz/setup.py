from setuptools import setup

setup(name='pyqgen',
      version='0.1',
      description='Generate questions from orgmode files',
      url='http://github.com/glipari/pyqgen',
      author='Giuseppe Lipari',
      author_email='giuseppe.lipari@univ-lille.fr',
      license='MIT',
      packages=['pyqgen'],
      scripts=['bin/pyqgen'],
      install_requires=['orgparse'],
      zip_safe=False)
