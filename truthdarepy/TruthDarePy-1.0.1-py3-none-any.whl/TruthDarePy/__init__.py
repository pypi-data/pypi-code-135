from requests import get

class TD():
    def __init__(self):
        self.url = "https://api.truthordarebot.xyz/v1"

    def truth(self):
        try:
            url = f"{self.url}/truth"
            response = get(url)
            return response.json()
        except Exception as e:
            return "Got An Error! Report At @ProgrammerSupport\n\n{}".format(e)

    def dare(self):
        try:
            url = f"{self.url}/dare"
            response = get(url)
            return response.json()
        except Exception as e:
            return "Got An Error! Report At @ProgrammerSupport\n\n{}".format(e)

    def languages():
        try:
            return """
• English - question
• বাংলা (Bengali) - bn
• Deutsch (German) - de
• Español (Spanish) - ea
• Français (French) - fr
• हिंदी (Hindi) - hi
• Tagalog (Filipino) - tl
  """
        except Exception as e:
            return "Got An Error! Report At @ProgrammerSupport\n\n{}".format(e)
