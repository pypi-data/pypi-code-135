from requests import get

version = "2.0.0"

class TD():
    def __init__(self):
        self.url = "https://api.truthordarebot.xyz/v1"
        self.langs = ["en", "bn", "de", "ea", "fr", "hi", "tl"]

    def truth(self, lang=None):
        try:
            url = f"{self.url}/truth"
            if lang == "en":
                response = get(url).json()["question"]
                return response
            if lang == "bn":
                response = get(url).json()["bn"]
                return response
            if lang == "de":
                response = get(url).json()["de"]
                return response
            if lang == "ea":
                response = get(url).json()["ea"]
                return response
            if lang == "fr":
                response = get(url).json()["fr"]
                return response
            if lang == "hi":
                response = get(url).json()["hi"]
                return response
            if lang == "tl":
                response = get(url).json()["tl"]
                return response
            if lang not in self.langs:
                return "The Following Lang Is Not Supported Check Out TD().languages"
                return response
        except Exception as e:
            return "Got An Error! Report At @ProgrammerSupport\n\n{}".format(e)

    def dare(self, lang=None):
        try:
            url = f"{self.url}/dare"
            if lang == "en":
                response = get(url).json()["question"]
                return response
            if lang == "bn":
                response = get(url).json()["bn"]
                return response
            if lang == "de":
                response = get(url).json()["de"]
                return response
            if lang == "ea":
                response = get(url).json()["ea"]
                return response
            if lang == "fr":
                response = get(url).json()["fr"]
                return response
            if lang == "hi":
                response = get(url).json()["hi"]
                return response
            if lang == "tl":
                response = get(url).json()["tl"]
                return response
            if lang not in self.langs:
                return "The Following Lang Is Not Supported Check Out TD().languages"
                return response
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

if __name__ == "__main__":
            print("Welcome To TruthDarePy v{}".format(version))
            print("Powered By @Its_IZ_PRINCE_xD")
