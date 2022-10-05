from src.inspector.models import Arrayable
from typing import Union


class HOST(Arrayable):
    hostname: Union[str, None] = None
    ip: Union[str, None] = None
    os: Union[str, None] = None
    url: Union[str, None] = None
    cpu: Union[str, None] = None
    ram: Union[str, None] = None
    hdd: Union[str, None] = None

    def set_hostname(self, hostname: str) -> None:
        self.hostname = hostname

    def set_ip(self, ip: str) -> None:
        self.ip = ip

    def set_os(self, os: str) -> None:
        self.os = os

    def set_cpu(self, cpu: str) -> None:
        self.cpu = cpu

    def set_ram(self, ram: str) -> None:
        self.ram = ram

    def set_hdd(self, hdd: str) -> None:
        self.hdd = hdd

    def get_hostname(self) -> str:
        return self.hostname

    def get_url(self) -> str:
        return self.url

    def get_cpu(self) -> str:
        return self.cpu

    def get_ram(self) -> str:
        return self.ram

    def get_hdd(self) -> str:
        return self.hdd
