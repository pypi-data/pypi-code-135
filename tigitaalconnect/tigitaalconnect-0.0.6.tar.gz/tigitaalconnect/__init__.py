import requests

class login():
    
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

class forum():
    
    def messages(forumid):
        json = {"forumid": forumid}
        response = requests.post("https://api.tigitaal.nl/forum/messages/", json=json)
        return response.json()
        
    def threads(forumid):
        json = {"forumid": forumid}
        response = requests.post("https://api.tigitaal.nl/forum/threads/", json=json)
        return response.json()
        
    def post(user, text, forumid):
        json = {"text": text, "forumid": forumid, "token": user.token}
        response = requests.post("https://api.tigitaal.nl/forum/post/", json=json)
        return response.json()
        
    def edit(user, text, forumid, messageid):
        json = {"text": text, "forumid": forumid, "token": user.token, "count": messageid}
        response = requests.post("https://api.tigitaal.nl/forum/edit/", json=json)
        return response.json()
     
    def all():
        response = requests.get("https://api.tigitaal.nl/forum/getforums/")
        return response.json()

