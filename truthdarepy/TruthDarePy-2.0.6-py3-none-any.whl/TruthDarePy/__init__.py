from requests import get

version = "2.0.6"

class TD():
    def __init__(self):
        self.url = "https://api.truthordarebot.xyz/v1"
        self.langs = ["en", "bn", "de", "es", "fr", "hi", "tl"]

    def truth(self, lang):
        try:
            url = f"{self.url}/truth"
            if lang == "en":
                response = get(url).json()["question"]
                return response
            if lang == "bn":
                response = get(url).json()["translations"]["bn"]
                return response
            if lang == "de":
                response = get(url).json()["translations"]["de"]
                return response
            if lang == "es":
                response = get(url).json()["translations"]["es"]
                return response
            if lang == "fr":
                response = get(url).json()["translations"]["fr"]
                return response
            if lang == "hi":
                response = get(url).json()["translations"]["hi"]
                return response
            if lang == "tl":
                response = get(url).json()["translations"]["tl"]
                return response
            if lang not in self.langs:
                return "The Following Lang Is Not Supported Check Out TD().languages"
        except Exception as e:
            return "Got An Error! Report At @ProgrammerSupport\n\n{}".format(e)

    def dare(self, lang):
        try:
            url = f"{self.url}/dare"
            if lang == "en":
                response = get(url).json()["question"]
                return response
            if lang == "bn":
                response = get(url).json()["translations"]["bn"]
                return response
            if lang == "de":
                response = get(url).json()["translations"]["de"]
                return response
            if lang == "es":
                response = get(url).json()["translations"]["es"]
                return response
            if lang == "fr":
                response = get(url).json()["translations"]["fr"]
                return response
            if lang == "hi":
                response = get(url).json()["translations"]["hi"]
                return response
            if lang == "tl":
                response = get(url).json()["translations"]["tl"]
                return response
            if lang not in self.langs:
                return "The Following Lang Is Not Supported Check Out TD().languages"
        except Exception as e:
            return "Got An Error! Report At @ProgrammerSupport\n\n{}".format(e)

    def languages():
        try:
            return """
• English - en
• বাংলা (Bengali) - bn
• Deutsch (German) - de
• Español (Spanish) - es
• Français (French) - fr
• हिंदी (Hindi) - hi
• Tagalog (Filipino) - tl
  """
        except Exception as e:
            return "Got An Error! Report At @ProgrammerSupport\n\n{}".format(e)
