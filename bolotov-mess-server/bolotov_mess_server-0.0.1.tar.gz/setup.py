from setuptools import setup, find_packages

setup(name="bolotov_mess_server",
      version="0.0.1",
      description="messanger server",
      author="Alex Bolotov",
      author_email="alexbolotov@gmail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run']
      )
