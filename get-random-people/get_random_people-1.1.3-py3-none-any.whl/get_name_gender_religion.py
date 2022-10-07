from names import *
from random import randint

def get_name_gender_religion():
    religions = ('islam', 'christianity', 'other')
    genders = ('male', 'female')
    religion = religions[randint(0, 2)]
    gender = genders[randint(0, 1)]

    firstname = ""
    lastname = ""

    if religion == 'islam':
        if gender == 'male':
            firstname = arabic_male[randint(0, len(arabic_male) - 1)]
            lastname = arabic_surnames[randint(0, len(arabic_surnames) - 1)]
        else:
            firstname = arabic_female[randint(0, len(arabic_female) - 1)]
            lastname = arabic_surnames[randint(0, len(arabic_surnames) - 1)]
            
    elif religion == 'christianity':
        if gender == 'male':
            firstname = english_male[randint(0, len(english_male) - 1)]
            lastname = english_surnames[randint(0, len(english_surnames) - 1)]
        else:
            firstname = english_female[randint(0, len(english_female) - 1)]
            lastname = english_surnames[randint(0, len(english_surnames) - 1)]
    else:
        if gender == 'male':
            firstname = english_male[randint(0, len(english_male) - 1)]
            lastname = english_surnames[randint(0, len(english_surnames) - 1)]
        else:
            firstname = english_female[randint(0, len(english_female) - 1)]
            lastname = english_surnames[randint(0, len(english_surnames) - 1)]
        
    return firstname, lastname, gender, religion