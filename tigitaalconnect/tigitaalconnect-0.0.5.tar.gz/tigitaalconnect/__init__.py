import requests

class UserConnect():
    
  def __init__(self, username, password):
      self.username = username
      self.password = password
      self.token = requests.post(f'https://api.tigitaal.nl/auth/login/{username}/{password}').json()["data"]
    
  def reload(self):
      response = requests.get(f'https://api.tigitaal.nl/user/reload/{self.token}')
      return response.json()

  def reloadadvanced(self):
      response = requests.get(f'https://api.tigitaal.nl/user/reloadadvanced/{self.username}/{self.password}')
      return response.json()

  # Buggy/doesnt work
  def pfp(self, pfp):
      response = requests.post(f'https://api.tigitaal.nl/user/reload/{self.token}/{pfp}')
      return response.json()

  def nickname(self, nickname):
      response = requests.post(f'https://api.tigitaal.nl/user/nickname/{self.username}/{self.password}/{nickname}')
      return response.json()

  def mail(self, email):
      response = requests.post(f'https://api.tigitaal.nl/user/mail/{self.username}/{self.password}/{email}')
      return response.json()
  
#   def aboutme(self, aboutme):
#       response = requests.post(f'https://api.tigitaal.nl/user/aboutme/{self.username}/{self.password}/{aboutme}')
#       return response.json()
