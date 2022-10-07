from setuptools import setup, find_packages



setup(name = 'mzStudio3',
      version = '2.1',
      author = 'Scott Ficarro, William Max Alexander',
      author_email = 'Scott_Ficarro@dfci.harvard.edu',
      packages = ['mzStudio3'],
      package_data = {'mzStudio3' : ['mzStudio3/image/*',
                                    'mzStudio3/settings/*',
                                    'mzStudio3/settings/*']},
      include_package_data = True,
      url = 'http://github.com/BlaisProteomics/mzStudio3',
      description = 'Mass Spectrometry/Proteomics Data Analysis Application',
      install_requires = ['multiplierz']
      )
