from typing import Optional

from mnemonic import Mnemonic
import hashlib
import binascii
import re


def blns_checksum(data, tag=b'BLNS-salt1'):
    m = hashlib.sha256()
    m.update(tag)
    m.update(data)
    return m.digest()[:4]


class BlnsMnemonic:
    CHECKSUM_LEN = 4
    DATA_LEN = 32  # salt len
    TAG_SALT1 = b'BLNS-salt1'
    TAG_SALT2 = b'BLNS-salt2'

    def __init__(self):
        self.mnemo = Mnemonic("english")

    def to_mnemonic(self, data: bytes, checksum: bytes) -> str:
        h = binascii.hexlify(checksum)
        b = (
                bin(int.from_bytes(data, byteorder="big"))[2:].zfill(len(data) * 8)
                + bin(int(h, 16))[2:].zfill(len(checksum) * 8)
        )
        result = []
        for i in range(len(b) // 11):
            idx = int(b[i * 11: (i + 1) * 11], 2)
            result.append(self.mnemo.wordlist[idx])
        result_phrase = " ".join(result)
        return result_phrase

    def to_binary(self, phrase: str, tag: Optional[bytes] = None) -> bytes:
        phrase = Mnemonic.normalize_string(phrase).strip()
        if tag is None:
            if phrase.startswith('balns1 ') or phrase.startswith('blns1 '):
                tag = BlnsMnemonic.TAG_SALT1
            elif phrase.startswith('balns2 ') or phrase.startswith('blns2 '):
                tag = BlnsMnemonic.TAG_SALT2

        if tag is None:
            raise ValueError('Tag is None')

        phrase = re.sub(r'^ba?lns[12]\s+', '', phrase)
        words = phrase.split(' ')
        num_words = len(words)
        num_checksum_bits = (num_words * 11) - BlnsMnemonic.DATA_LEN * 8
        data_len_bits = num_words * 11 - num_checksum_bits
        if data_len_bits % 8 != 0:
            raise ValueError('Invalid data size')

        try:
            idx = map(
                lambda x: bin(self.mnemo.wordlist.index(x))[2:].zfill(11), words
            )
            b = "".join(idx)
        except ValueError:
            raise ValueError('Invalid phrase')

        d = b[: data_len_bits]
        h = b[data_len_bits:]

        nd = int(d, 2).to_bytes(data_len_bits // 8, byteorder="big")
        nh = bin(int(binascii.hexlify(blns_checksum(nd, tag)), 16))[2:].zfill(BlnsMnemonic.CHECKSUM_LEN * 8)[: num_checksum_bits]
        if nh != h:
            raise ValueError('Invalid checksum')
        return nd

