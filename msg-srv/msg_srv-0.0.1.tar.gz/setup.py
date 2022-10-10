from setuptools import setup, find_packages

setup(
    name="msg_srv",
    version="0.0.1",
    description="messages_server",
    long_description = "Проект создания чата в рамках учебного курса GeekBrains по интерфейсам и клиент-серверному взаимодействию. Автор Колесник Иван. Проходил курс в августе-сентябре 2022 года. Hello world.",
    author="KolesnikIvan",
    packages=find_packages(),
    install_requires=["PyQt5", "sqlalchemy", "pycryptodome", "pycryptodomex"]
)
