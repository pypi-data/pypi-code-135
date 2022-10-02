"""Módulo do CNPJ"""


def CNPJ(CNPJ: str = '00.000.000/0000-00') -> bool:
    """CNPJ.

    Nesta função fazemos a verificação do CNPJ passado.

    Args:
        CNPJ (str): CNPJ para a verificação.

    Returns:
        bool: Retornarmos se é verdadeiro ou falso.
    """
    cnpj = [int(char) for char in CNPJ if char.isdigit()]
    CNPJ = cnpj[:12]
    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    if sum(cnpj) == 0:
        return False

    while len(CNPJ) < 14:
        valor = sum([x * y for (x, y) in zip(CNPJ, prod)]) % 11
        if valor > 1:
            resto = 11 - valor
        else:
            resto = 0
        CNPJ.append(resto)
        prod.insert(0, 6)
    if CNPJ == cnpj:
        return True
    return False


async def CNPJ_async(CNPJ: str = '00.000.000/0000-00') -> bool:
    """CNPJ Async.

    Nesta função fazemos a verificação do CNPJ passado em uma função assíncrona.

    Args:
        CNPJ (str): CNPJ para a verificação.

    Returns:
        bool: Retornarmos se é verdadeiro ou falso.
    """
    cnpj = [int(char) for char in CNPJ if char.isdigit()]
    CNPJ = cnpj[:12]
    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    if sum(cnpj) == 0:
        return False

    while len(CNPJ) < 14:
        valor = sum([x * y for (x, y) in zip(CNPJ, prod)]) % 11
        if valor > 1:
            resto = 11 - valor
        else:
            resto = 0
        CNPJ.append(resto)
        prod.insert(0, 6)
    if CNPJ == cnpj:
        return True
    return False
