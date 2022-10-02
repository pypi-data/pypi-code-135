"""Módulo do CPF"""


def CPF(CPF: str = '000.000.000-00') -> bool:
    """CPF.

    Nesta função fazemos a verificação do CPF passado.

    Args:
        CPF (str): CPF para a verificação.

    Returns:
        bool: Retornarmos se é verdadeiro ou falso.
    """
    cpf = [int(char) for char in CPF if char.isdigit()]
    if len(cpf) != 11 or cpf == cpf[::-1]:
        return False
    for index in range(9, 11):
        valor = sum(
            (cpf[num] * ((index + 1) - num) for num in range(0, index))
        )
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[index]:
            return False
    return True


async def CPF_async(CPF: str = '000.000.000-00') -> bool:
    """CPF Async.

    Nesta função fazemos a verificação do CPF passado em uma função assíncrona.

    Args:
        CPF (str): CPF para a verificação.

    Returns:
        bool: Retornarmos se é verdadeiro ou falso.
    """
    cpf = [int(char) for char in CPF if char.isdigit()]
    if len(cpf) != 11 or cpf == cpf[::-1]:
        return False
    for index in range(9, 11):
        valor = sum(
            (cpf[num] * ((index + 1) - num) for num in range(0, index))
        )
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[index]:
            return False
    return True
