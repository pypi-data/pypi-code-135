import requests

def reload(token):
    response = requests.get(f'https://api.tigitaal.nl/user/reload/{token}')
    return response.text

def reloadadvanced(username, password):
    response = requests.get(f'https://api.tigitaal.nl/user/reloadadvanced/{username}/{password}')
    return response.text

# Buggy/doesnt work
def pfp(token, pfp):
    response = requests.post(f'https://api.tigitaal.nl/user/reload/{token}/{pfp}')
    return response.text

def nickname(username, password, nickname):
    response = requests.post(f'https://api.tigitaal.nl/user/nickname/{username}/{password}/{nickname}')
    return response.text

def mail(username, password, email):
    response = requests.post(f'https://api.tigitaal.nl/user/mail/{username}/{password}/{email}')
    return response.text

# Buggy/Doesnt work
# Will be added in later release
# def aboutme(username, password, aboutme):
#     response = requests.post(f'https://api.tigitaal.nl/user/aboutme/{username}/{password}/{aboutme}')
#     return response.text
