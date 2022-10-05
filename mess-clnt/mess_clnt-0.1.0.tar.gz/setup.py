from setuptools import setup, find_packages

setup(name="mess_clnt",
      version="0.1.0",
      description="mess_clnt",
      author="android156",
      author_email="4_registrations@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
