import random

def make_my_passwords(n_password = 1, password_len = 6):
    """
    A function that generates one or more random passwords, where you enter as the first parameter the password number you want and in the second parameter the size of the password(s).
    :param n_password: Number of ramdom passwords you want.
    :param password_len: The length of the password(s).
    :return: Return an array with the generates random password(s).
    """
    chars = "0123456789abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*%$#@"
    list = []
    for num in range(n_password):
        password = ''
        for len in range(password_len):
            password += random.choice(chars)
        list.append(password)
    return list
