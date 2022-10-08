""" Module sur le passage entre les diverses représentations de données."""


def dec2bin(n: int, sep="_") -> str:
    # https://docs.python.org/3/library/string.html#format-specification-mini-language

    # on groupe les bits par 4 séparés par des tirets bas par défaut
    b = "{0:_b}".format(n)
    if sep is None:
        return b
    return b.replace("_", sep)


def bin2dec(b: str) -> int:
    # https://stackoverflow.com/a/11029366
    if isinstance(b, str):
        return int(b, 2)
    elif isinstance(b, int):
        return int(str(b), 2)
    else:
        raise Exception("Format d'entrée invalide")


def dec2hex(n: int) -> str:
    # https://stackoverflow.com/a/11029366

    return "{0:_X}".format(n)


def hex2dec(x: str) -> int:
    # https://stackoverflow.com/a/11029366

    return int(x, 16)


def ascii2bin(l: str, replace=False, **kwargs) -> str:
    """Convertir une lettre ASCII en octet"""
    assert len(l) == 1, "Ne convertit qu'une lettre à la fois"
    # if replace:
    #    l = l.encode("ascii", "replace")
    # else:
    #    l = l.encode("ascii")*
    n = ord(l)
    assert n < 2**8, "seuls les lettres ascii sont auotrisées"
    if "sep" in kwargs:
        return dec2bin(n, **kwargs).zfill(8 + len(kwargs["sep"]))
    else:
        return dec2bin(n, sep="", **kwargs).zfill(8)
