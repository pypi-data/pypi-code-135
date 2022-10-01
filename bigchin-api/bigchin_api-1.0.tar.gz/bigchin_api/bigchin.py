from ast import keyword
import functools
import os
import sys
import random
from tkinter import E
import functools

bigchin_ver = "1.0"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

cr = bcolors.ENDC

def сpermchance(*chancesw):
    # try:
    chances = list(chancesw)
    temp_f = 0
    temp_list = []
    temp_a = 0
    for key in chances:
        temp_a += key
    if temp_a >= 100:
        print(bcolors.FAIL + f"Big Chin: The limit of the allowed amount of luck was exceeded" + cr)
        return
    while temp_f != 1:
        for key in chances:
            if key > 100:
                print(bcolors.FAIL + f"Big Chin: {key} should not higher than 100" + cr)
                return
            if key < 0:
                print(bcolors.FAIL + f"Big Chin: {key} should not lower than 0" + cr)
                return
            number_chance = random.randint(1, 100)
            if number_chance <= key:
                temp_f += 1
                winp = key
        if temp_f > 1:
            temp_f = 0
            winp = 0
            continue
    return winp
    # except TypeError:
    #     print(bcolors.FAIL + f"Big Chin: {chances} not support int type" + cr)
    #     return

def permchance(*chancesw):
    try:
        chances = list(chancesw)
        temp_dict = {}
        for key in chances:
            if key > 100:
                print(bcolors.FAIL + f"Big Chin: {key} should not higher than 100" + cr)
                return
            if key < 0:
                print(bcolors.FAIL + f"Big Chin: {key} should not lower than 0" + cr)
                return
            number_chance = random.randint(1, 100)
            if number_chance <= key:
                key_s = True
            if number_chance > key:
                key_s = False
            t_W = {key: key_s}
            temp_dict.update(t_W)
        return temp_dict
    except TypeError:
        print(bcolors.FAIL + f"Big Chin: {chances} not support int type" + cr)
        return

def perchance(chance):
    try:
        if chance > 100:
            print(bcolors.FAIL + f"Big Chin: {chance} should not higher than 100" + cr)
            return
        if chance < 0:
            print(bcolors.FAIL + f"Big Chin: {chance} should not lower than 0" + cr)
            return
        number_chance = random.randint(1, 100)
        if number_chance <= chance:
            return True
        elif number_chance > chance:
            return False            
    except TypeError:
        print(bcolors.FAIL + f"Big Chin: {chance} not support int type" + cr)
        return


def perchances(number=None, success=None):
    try:
        numbers_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        if number == None:
            number = 100
        if ((success == None) or (success == False)) and success != True:
            if number not in numbers_list:
                temp_txt = bcolors.WARNING + f"Big Chin: Do you really want to set {number} as the maximum luck level? (y/n)\n" + cr
                temp_user_number_input = input(temp_txt)
                user_number_input = temp_user_number_input.lower()
                if user_number_input == "y":
                    pass
                elif user_number_input == "n":
                    print(bcolors.HEADER + "Big Chin: Success" + cr)
                    return None
                else:
                    print(bcolors.WARNING + f"Big Chin: There is no answer option {user_number_input}. Try again" + cr)
                    return
        elif success == True:
            pass
        else:
            print(bcolors.FAIL + f"Big Chin: Parameter {success} is lie" + cr)
            return
        number_chance = random.randint(1, number)
        return number_chance
    except TypeError:
        print(bcolors.FAIL + f"Big Chin: {number} not support int type" + cr)
        return

class system:
    def ver():
        print(bcolors.OKGREEN + "Version BIGCHIN: " + bigchin_ver + cr)
    
        
# perform = command()