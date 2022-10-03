from setuptools import setup, find_packages

setup(name="py_messanger_r2_client",
      version="1.0.0",
      description="Messenger client",
      author="Roman Sl",
      author_email="",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
