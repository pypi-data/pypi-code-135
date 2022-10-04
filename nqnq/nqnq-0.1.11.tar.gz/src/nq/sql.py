from os import environ
import dotenv

quos = lambda str_iter: ",".join([f"'{s}'" for s in str_iter])


def constr(**kwargs):
    if kwargs.get("envfile"):
        dotenv.load_dotenv(kwargs.get("envfile"))

    keys = ["host", "port", "db_name", "username", "password"]
    db = {}

    for key in keys:
        db[key] = environ.get(key) or kwargs.get(key) or input(f"{key}?")

    result = f"postgresql://{db['username']}:{db['password']}@{db['host']}:{db['port']}/{db['db_name']}"

    if kwargs.get("envfile"):
        for key in keys:
            environ.pop(key)
    return result
