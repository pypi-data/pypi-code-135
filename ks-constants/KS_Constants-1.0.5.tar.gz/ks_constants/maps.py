from enum import Enum
from devs import Developer


class Map(Enum):
    Classic = ({'en': 'Classic', 'kr': '기본'}, Developer.Luminous, False, None)
    Duck_Map = ({'en': 'Duck Map', 'kr': '오리'}, Developer.Duck, True, None)
    Four_Seasons = ({'en': 'Four Seasons', 'kr': '사계절'}, Developer.Luminous, True, None)
    Zerus_Volcanoes = ({'en': 'Zerus Volcanoes', 'kr': '제루스 화산'}, Developer.Luminous, True, None)
    Ruins_Of_Imladoon = ({'en': 'Ruins of Imladoon', 'kr': '임라둔의 잔해'}, Developer.Fatline, True, Developer.Templar)
    Heart_Of_Amethyst = ({'en': 'Heart of Amethyst', 'kr': '자수정의 심장'}, Developer.Luminous, False, None)
    Vintage_Shores = ({'en': 'Vintage Shores', 'kr': '빈티지 해변'}, Developer.Templar, False, None)
    Aiur_Fountains = ({'en': 'Aiur Fountains', 'kr': '아이어 분수'}, Developer.Luminous, False, None)
    Kaldir_Cliffs = ({'en': 'Kaldir Cliffs', 'kr': '칼디르 절벽'}, Developer.Understudy, True, None)

    def __init__(self, name_dict: dict, original_author: Developer, map_available: bool = False,
                 current_author: Developer = None):
        self._name_dict = name_dict
        self._original_author = original_author
        self._current_author = original_author if current_author is None else current_author
        self._map_available = map_available

    @property
    def name(self):
        return self._name_dict.copy()

    def original_author(self):
        return self._original_author

    def current_author(self):
        return self._current_author

    def is_map_available(self):
        return self._map_available
