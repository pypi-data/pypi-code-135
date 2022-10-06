import hashlib
import hmac


def recover_seed(part1, part2):
    h = hmac.new(b'\xFE\x42\xEF', part1 + part2, hashlib.sha512)
    return h.digest()[:32]


def bitcoin_seed(seed):
    h = hmac.new(b'Bitcoin seed', seed, hashlib.sha512)
    r = h.digest()
    return r[:32], r[32:]
