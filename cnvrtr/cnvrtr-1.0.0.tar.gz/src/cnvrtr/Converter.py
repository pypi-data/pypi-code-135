class Converter():
    def __init__(self) -> None:
        pass

    def toLittleEndian(self, value):
        # example for value = "20 21 00"
        s = value.split(" ")
        h_ = "".join(s[i] for i in range(len(s)-1, -1, -1))
        return h_

    def hexToBin(self, hex):
        return bin(int(hex, base=16)).replace("0b","")

    def hexToDec(self, hex_):
        return int(hex_, 16)

    def binToDec(self, bin):
        # example for bin = "100001"
        return int(bin, 2)

    def decToAscii(self, dec):
        result = ""
        if (dec >= 32 and dec <= 126):
            result = chr(dec) 
        return result