from random import randint
from countries_capital import countries_capital
from datetime import date, datetime

def get_address(nationality):
    country = nationality
    region = countries_capital[nationality]
    street = f"{randint(11, 124)}th street"
    house = f"House no {randint(1, 30)}"
    return f"{house}, {street}, {region}, {country}"

def get_skin_color():
    skin_colors = ("white","brown", "pale", "black")
    return skin_colors[randint(0, len(skin_colors) - 1)]

def get_eye_color(skin_color):
    eye_colors = []
    if skin_color == "white" or skin_color == "pale":
        eye_colors = ["blue", "green", "grey", "brown", "black"]
    else:
        eye_colors = ["brown", "black"]

    return eye_colors[randint(0, len(eye_colors) - 1)]

def get_hair_style(gender):
    hair_styles = ['short', 'medium', 'long', 'bald', 'sides short center long']
    if gender == "female":
        hair_styles.remove("bald")
    return hair_styles[randint(0, len(hair_styles) - 1)]

def get_hair_color(skin_color, age, hair_style):
    hair_color = []
    if skin_color == "white" or skin_color == "pale":
        hair_color = ["blonde", "brown", "black", "red", "white"]
    else:
        hair_color = ["brown", "black"]
    
    if(age > 65):
        hair_color = ["white"]
    
    if(hair_style == "bald"):
        hair_color = ["bald"]

    return hair_color[randint(0, len(hair_color) - 1)]

def get_email(firstname, lastname, age):
    domains = ("gmail", "yahoo", "outlook", "hotmail", "live")
    random_index = randint(0, len(domains) - 1)
    email = f"{firstname.lower()}{lastname.lower()}{date.today().year - age}@{domains[random_index]}.com"
    return email