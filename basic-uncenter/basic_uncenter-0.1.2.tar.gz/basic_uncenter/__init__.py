__version__ = '0.1.2'

def isdecimal(var):
    if var%2 == 0 or var%3 == 0 or var%5 == 0 or var%7 == 0 or var%9 == 0 or var == 1:
        decimal = False
    else:
        decimal = True
    return decimal

def factorial(num):
    if num < 0:
        factorial = "InputError: Factorial does not exist for negative numbers"
    elif num == 0:
       factorial = 1
    else:
        factorial = 1
        for i in range(1, num + 1):
           factorial = factorial * i
    return factorial

def println(var, num = 1):
    print("\n"*num + var)

def printx(var, num):
    for i in range(0, num):
        print(var)
