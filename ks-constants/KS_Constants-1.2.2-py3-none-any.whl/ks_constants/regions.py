from enum import Enum
from .locale import Language

class Region(Enum):
    North_America = ({Language.English: 'NA', Language.Korean: '북미'})
    Europe = ({Language.English: 'EU', Language.Korean: '유럽'})
    Korea = ({Language.English: 'KR', Language.Korean: '한국'})
    China = ({Language.English: 'CN', Language.Korean: '중국'})

    def __init__(self, codes):
        self._codes = codes

    def get_code(self, locale: Language):
        return self._codes[locale]

    def get_english_code(self):
        return self.get_code(Language.English)

    def get_korean_code(self):
        return self.get_code(Language.Korean)
