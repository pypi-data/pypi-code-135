from os import environ
from getpass import getpass
import dotenv

quos = lambda str_iter: ",".join([f"'{s}'" for s in str_iter])


def constr(**kwargs):
    if kwargs.get("envfile"):
        dotenv.load_dotenv(kwargs.get("envfile"))

    keys = ["host", "port", "db_name", "username"]
    db = {}

    for key in keys:
        db[key] = environ.get(key) or kwargs.get(key) or input(f"{key}? ")

    db["password"] = environ.get(key) or getpass("password? ")

    result = f"postgresql://{db['username']}:{db['password']}@{db['host']}:{db['port']}/{db['db_name']}"

    if kwargs.get("envfile"):
        for key in keys:
            if key in environ:
                environ.pop(key)
    return result
