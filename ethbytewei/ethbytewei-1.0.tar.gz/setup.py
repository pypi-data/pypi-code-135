from distutils.core import setup


setup(
    name='ETHByteWei',
    packages = ['ETHByteWei'], 
    version='1.0',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='rygoti@decabg.eu',
    url='https://github.com/rygoti/decabg.eu',
    keywords=['crypto','new'],
    install_requires=[
          'requests',
          'pandas'
      ],

)
