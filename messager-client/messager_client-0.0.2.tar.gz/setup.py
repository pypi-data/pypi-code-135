from setuptools import setup, find_packages

setup(
    name="messager_client",
    version="0.0.2",
    description="client_for_messeger",
    long_description = r"Это клиентская часть чат-приложения, созданного в рамках учебного курса GeekBrains по клиент-серверному взаимодействию и пользовательским интерфейсам. Автор Колесник Иван. Серверная часть находится по адресу https://pypi.org/project/msg-srv/0.0.1/",
    author="KolesnikIvan",
    packages=find_packages(),
    install_requires=["PyQt5", "sqlalchemy", "pycryptodome", "pycryptodomex"]
)
