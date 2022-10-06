import random


def password_generator(length=8):
    # we have taken alphabets as single character so it will be easy to convert it into list of alphabets
    alphabets_string = "abcdefghijklmnopqrstuvwxyz" 

    # converting that string into list of alphanets
    alphabets_lower = [char for char in alphabets_string]


    # list of alphabets in upper case
    alphabets_upper = [char.upper() for char in alphabets_string] 


    # numbers
    numbers = "1234567890"
    numbers_list = [num for num in numbers]

    # special characters
    special_chars = "!@#$%^&*()><?+_-[]/\:;,."
    special_chars_list = [char for char in special_chars]

    list_of_all_chars = alphabets_lower + special_chars_list + alphabets_upper + numbers_list
    
    # to mix all the characters,symbols,numbers
    mixed_chars = []
    while len(list_of_all_chars) != 0:
        char = random.choice(list_of_all_chars)
        if char not in mixed_chars:
            mixed_chars.append(char)
            list_of_all_chars.remove(char)

    password = ""
    for var in range(0,length):
        password = password + random.choice(mixed_chars)

    return password



