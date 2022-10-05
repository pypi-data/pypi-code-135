"""
Nicely typed env mgmt.
"""
from dataclasses import dataclass

from dotenv import dotenv_values
from pydantic import BaseSettings

config = dotenv_values(".env")

__all__ = ["environment"]


class Common(BaseSettings):
    test: str = config["TEST"]


class Servers(BaseSettings):
    pass


class Databases(BaseSettings):
    pass


class Environment(Common, Servers, Databases):
    pass


environment = Environment()
