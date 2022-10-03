import random


def generator():
    lower_bound = 10 ** (9 - 1)
    upper_bound = 10 ** 9 - 1
    base_tckn = str(random.randint(lower_bound, upper_bound))
    odd_sum = sum(int(base_tckn[i]) for i in range(0, 10, 2))
    even_sum = sum(int(base_tckn[i]) for i in range(1, 9, 2))
    tenth_digit = ((odd_sum * 7) - even_sum) % 10
    base_tckn_lst = [int(i) for i in base_tckn]
    base_tckn_lst.append(tenth_digit)
    eleventh_digit = sum(base_tckn_lst) % 10
    base_tckn_lst.append(eleventh_digit)
    return "".join(map(str, base_tckn_lst))
