from enum import Enum

class Region(Enum):
    North_America = ({"English": 'NA', "Korean": '북미'})
    Europe = ({"English": 'EU', "Korean": '유럽'})
    Korea = ({"English": 'KR', "Korean": '한국'})
    China = ({"English": 'CN', "Korean": '중국'})

    def __init__(self, codes):
        self._codes = codes

    def get_english_code(self):
        return self._codes["English"]

    def get_korean_code(self):
        return self._codes["Korean"]
