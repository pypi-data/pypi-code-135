__version__ = '0.1.3'

def isdecimal(var):
    if var.is_integer():
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
