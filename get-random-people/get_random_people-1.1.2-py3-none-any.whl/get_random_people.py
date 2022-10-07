from random import randint
from countries import countries
from qualifications import qualifications
from get_name_gender_religion import get_name_gender_religion
from uuid import uuid1
from datetime import date, datetime
from utils import *

class get_random_people:

    def get_highest_education(self):
        return qualifications[randint(0, len(qualifications) - 1)]

    def get_nationality(self):
        random_index = randint(0,len(countries) - 1)
        return countries[random_index]

    def get_DOB(self, age):
        year = date.today().year - age
        month = randint(1, 12)
        day = randint(1, 28)
        return datetime(year, month, day).strftime("%b %dth, %Y")

    def get_phone_number(self, length = 10):
        phone_number = str(randint(7, 9))
        for _ in range(0, length - 1):
            phone_number += str(randint(0, 9))
        return phone_number

    def get_person(self):
        firstname, lastname, gender, religion = get_name_gender_religion()
        age = randint(18, 110)
        nationality = self.get_nationality()
        side_bussiness = ("Youtuber", "Vlogger", "Blogger", "Tiktoker", "Gamer")
        skin_color = get_skin_color()
        hair_style = get_hair_style(gender)
        person = {
            "id": str(uuid1()),
            "firstname": firstname,
            "lastname": lastname,
            "dob": self.get_DOB(age),
            "email": get_email(firstname, lastname, age),
            "phone_number": self.get_phone_number(),
            "address": get_address(nationality),
            "gender": gender,
            "religion": religion,
            "age": age,
            "skin_color": skin_color,
            "eye_color": get_eye_color(skin_color),
            "hair_style": hair_style,
            "hair_color": get_hair_color(skin_color, age, hair_style),
            "is_married": True if randint(0, 1) else False,
            "highest_education": self.get_highest_education(),
            "occupation": "Bussiness" if randint(0, 1) else "Service",
            "side_bussiness": side_bussiness[randint(0, len(side_bussiness) - 1)],
            "annaul_income_USD": randint(2500, 20000) * 12,
            "nationality": nationality,
            "height_in_feet": round(randint(15, 24) / 10 * 3.281, 1),
            "weight_in_kg": randint(35, 90)    
        }
        return person

    def get_peoples(self, totalPeoples = 10):
        peoples = []
        for _ in range(0, totalPeoples):
            peoples.append(self.get_person())

        return peoples

print(get_random_people().get_person())