from StarkChat.core import Chatbot
from datetime import datetime

class StarkChat:
    def __init__(self, name="Stark", gender="Male", age=19, birth_year=2004, botmaster="Sathishzus"):
        """Instantiate StarkChat"""

        self.name = name
        self.gender = gender
        self.age = age
        self.birth_year = birth_year
        self.botmaster = botmaster
        self.chatbot = Chatbot()

    def chat(self, message) -> str:
        """Returns a response from the chatbot. If encountered error, returns fallback response"""

        if not message or isinstance(message, str) is False:
            raise TypeError("Message must be a non-empty string")
        else:
            response = self.chatbot.get_response(message=str(message))
            response = response.replace("CHAT_BOT_NAME", self.name)
            response = response.replace("CHAT_BOT_GENDER", self.gender)
            response = response.replace("CHAT_BOT_AGE", str(self.age))
            response = response.replace("CHAT_BOT_MASTER", self.botmaster)
            return response

    def get_age(self) -> int:
        """Returns the age of the chatbot"""

        epoch = self.birth_year
        now = datetime.now().year
        return now - epoch
