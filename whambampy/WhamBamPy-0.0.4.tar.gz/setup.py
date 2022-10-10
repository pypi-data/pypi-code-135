import setuptools

setuptools.setup(
   name='WhamBamPy',
   version='0.0.4',
   author='Dmitry Minin',
   author_email='dmitry.m@bbdmgroup.com',
   packages=['whambampy'],
   scripts=[],
   url='http://pypi.python.org/pypi/whambampy/',
   license='LICENSE.txt',
   description='WHM Api interface',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   install_requires=[
      "certifi==2022.9.24",
      "charset-normalizer==2.1.1",
      "colorama==0.4.5",
      "idna==3.4",
      "requests==2.28.1",
      "urllib3==1.26.12"
   ],
   download_url="https://github.com/BBDM-Group/bbdm-whm-manager/archive/refs/tags/0.0.4.tar.gz"
)