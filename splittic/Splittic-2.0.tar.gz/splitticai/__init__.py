from bs4 import BeautifulSoup
import requests


class AI:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def makeimg(self, text, filename):
        req = requests.get(
            f"https://ai.dragonspot.tk/api/img/{text}",
            headers={"api-key": self.API_KEY},
            timeout = 120
        )
        if req.status_code == 200:
            bs = BeautifulSoup(req.text, "html.parser")
            img = bs.find("img")
            if img:
                img = img.get("src")
                if img:
                    with open(filename, "wb") as f:
                        f.write(requests.get(img).content)
                    return True
        return False

    def qa(self, text, userid = None):
        if not userid:
            req = requests.get(
                f"https://ai.dragonspot.tk/api/qa/{text}",
                headers={"api-key": self.API_KEY},
                timeout = 120
            )
            if req.status_code == 200:
                return req.text
            return False
        else:
            req = requests.get(
                f"https://ai.dragonspot.tk/api/qa/{userid}/{text}",
                headers={"api-key": self.API_KEY},
                timeout = 120
            )
            if req.status_code == 200:
                return req.text
            return False

    def scan(self,url):
        req = requests.get(
            f"https://ai.dragonspot.tk/api/scan/{url}",
            headers={"api-key": self.API_KEY},
            timeout = 120
        )
        if req.status_code == 200:
            return req.text
        return False
