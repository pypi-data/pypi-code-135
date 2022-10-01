from abc import abstractmethod
import item
import math

class SizeFormatter:
    @abstractmethod
    def format(self, size: int) -> str:
        pass

class Base10SizeFormatter(SizeFormatter):
    _sizeUnits10 = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
        "PB",
        "EB",
        "ZB",
        "YB"
    ]
    
    def format(self, size: int) -> str:
        if (size == 0): 
            return "0 B"

        mag = math.log10(size) // 3
        return f"{size / (10 ** (mag * 3))} {self._sizeUnits10[mag]}"

class Base2SizeFormatter(SizeFormatter):
    _sizeUnits2 = [
        "B",
        "KiB",
        "MiB",
        "GiB",
        "TiB",
        "PiB",
        "EiB",
        "ZiB",
        "YiB"
    ]

    def format(self, size: int) -> str:
        if (size == 0): 
            return "0 B"
        mag = math.log2(size) // 10
        return f"{size / (10 ** (mag * 10))} {self._sizeUnits2[mag]}"

class Log2SizeFormatter(SizeFormatter): 
    def format(self, size: int) -> str: return f"{math.log2(size)}"

class Log10SizeFormatter(SizeFormatter): 
    def format(self, size: int) -> str: return f"{math.log10(size)}"

class NyaSizeFormatter(SizeFormatter):
    _sizeNya = [
        "nya",
        "big nya",
        "mega nya",
        "sugoi nya",
        "nyaaaaa",
        "nyaaaaaa",
        "nyaaaaaaa",
        "nyaaaaaaaa",
        "nyaaaaaaaaa"
    ]
    def format(self, size: int) -> str:
        if (size == 0): 
            return "ewmpti T.T"
        mag = math.log2(size) // 10
        return f"{size / (10 ** (mag * 10))} {self._sizeNya[mag]}"    

