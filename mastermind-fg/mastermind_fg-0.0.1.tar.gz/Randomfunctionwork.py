import random

def Random_Function(Difficulty) :
    if Difficulty == 4 :
        Random_number = str(random.randrange(1000, 10000))
    elif Difficulty == 5 :
        Random_number = str(random.randrange(10000, 100000))
    elif Difficulty == 6 :
        Random_number = str(random.randrange(100000, 1000000))
    elif Difficulty == 7 :
        Random_number = str(random.randrange(1000000, 10000000))
    elif Difficulty == 8 :
        Random_number = str(random.randrange(10000000, 100000000))
    elif Difficulty == 9 :
        Random_number = str(random.randrange(100000000, 1000000000))
       
    return Random_number