import typing
import pymem
import config


for process_name in config.PROCESS_NAMES:
    try:
        pm = pymem.Pymem(process_name)
    except pymem.exception.ProcessNotFound:
        continue
    break
else:
    raise pymem.exception.ProcessNotFound(f"not any: {config.PROCESS_NAMES}")


read_pointer = pm.read_uint if pm.is_WoW64 else pm.read_longlong


class Address:
    def __init__(self, address: int, offsets: list[int] = None, add: int = 0):
        self.address = address
        self.offsets = [] if offsets is None else offsets
        self.add = add

    def resolve(self):
        pointer = self.address
        for offset in self.offsets:
            pointer = read_pointer(pointer) + offset

        return pointer + self.add


def make_address(address: typing.Union[Address, int]):
    if isinstance(address, Address):
        return address
    else:
        return Address(address)
