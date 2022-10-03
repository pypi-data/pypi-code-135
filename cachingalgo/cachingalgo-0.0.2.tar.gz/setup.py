from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='cachingalgo',
      packages = find_packages("cachingalgo"),
      version='0.0.2',
      description='Package consists of implementation of caching algorithms and request generation modules',
      author="Surya Krishna Guthikonda",
      author_email="suryakguthikonda@gmail.com",
      url="https://github.com/SuryaKrishna02/caching-algorithms",
      keywords = ['LFU', 'LFU-Lite', 'WLFU', 'LRU', 'LRUm', 'fLRU', 'CB-MPS', 'CB-SI', 'CB-SILite'],
      package_dir = {"":"cachingalgo"},
      include_package_data=True,
      package_data={
        "cachingalgo":["data/*.pkl"],
      },

      long_description = long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
      ],
      )
