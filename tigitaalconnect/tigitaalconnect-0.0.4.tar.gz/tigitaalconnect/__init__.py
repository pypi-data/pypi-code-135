import requests

def reload(token):
    response = requests.get(f'https://api.tigitaal.nl/user/reload/{token}')
    return response.json()

def reloadadvanced(username, password):
    response = requests.get(f'https://api.tigitaal.nl/user/reloadadvanced/{username}/{password}')
    return response.json()

# Buggy/doesnt work
def pfp(token, pfp):
    response = requests.post(f'https://api.tigitaal.nl/user/reload/{token}/{pfp}')
    return response.json()

def nickname(username, password, nickname):
    response = requests.post(f'https://api.tigitaal.nl/user/nickname/{username}/{password}/{nickname}')
    return response.json()

def mail(username, password, email):
    response = requests.post(f'https://api.tigitaal.nl/user/mail/{username}/{password}/{email}')
    return response.json()