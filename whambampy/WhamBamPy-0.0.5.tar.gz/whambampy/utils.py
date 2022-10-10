import string
import random


def generate_username(size=8, chars=string.digits + string.ascii_lowercase) -> str:
    """
    Generates random username for CPanels
    :param size: username length
    :param chars: characters to use during generation
    :return: str: generated username
    """
    return ''.join(random.choice(chars) for _ in range(size))


def generate_password(size=14, chars=string.ascii_letters + string.ascii_uppercase + string.digits) -> str:
    """
    Generates random password for CPanels
    :param size: password length
    :param chars: characters to use during generation
    :return: str: generated password
    """
    return ''.join(random.choice(chars) for _ in range(size)) + '@' + str(random.randint(1, 999))
