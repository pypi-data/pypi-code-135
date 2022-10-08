from enum import Enum
from ks_constants.devs import Developer
from ks_constants.locale import Language


class Map(Enum):
    Classic = ({Language.English: 'Classic', Language.Korean: '기본'},
               "CLASSIC",
               Developer.Luminous,
               ["Base.SC2Data/GameData/Terrain/Classic.xml"],
               False,
               None)
    Duck_Map = ({Language.English: 'Duck Map', Language.Korean: '오리'},
                "DUCK_MAP",
                Developer.Duck,
                ["Base.SC2Data/GameData/Terrain/DuckMap.xml"],
                True,
                None)
    Four_Seasons = ({Language.English: 'Four Seasons', Language.Korean: '사계절'},
                    "ZERUS_VOLCANOES",
                    Developer.Luminous,
                    ["Base.SC2Data/GameData/Terrain/FourSeasons.xml"],
                    True,
                    None)
    Zerus_Volcanoes = ({Language.English: 'Zerus Volcanoes', Language.Korean: '제루스 화산'},
                       "FOUR_SEASONS",
                       Developer.Luminous,
                       ["Base.SC2Data/GameData/Terrain/ZerusVolcanoes.xml"],
                       True,
                       None)
    Ruins_Of_Imladoon = ({Language.English: 'Ruins of Imladoon', Language.Korean: '임라둔의 잔해'},
                         "RUINS_OF_IMLADOON",
                         Developer.Fatline,
                         ["Base.SC2Data/GameData/Terrain/RuinsOfImladoon.xml"],
                         True,
                         Developer.Templar)
    Heart_Of_Amethyst = ({Language.English: 'Heart of Amethyst', Language.Korean: '자수정의 심장'},
                         "HEART_OF_AMETHYST",
                         Developer.Luminous,
                         ["Base.SC2Data/GameData/Terrain/HeartOfAmethyst.xml"],
                         False,
                         None)
    Vintage_Shores = ({Language.English: 'Vintage Shores', Language.Korean: '빈티지 해변'},
                      "VINTAGE_SHORES",
                      Developer.Templar,
                      ["Base.SC2Data/GameData/Terrain/VintageShores.xml"],
                      False,
                      None)
    Aiur_Fountains = ({Language.English: 'Aiur Fountains', Language.Korean: '아이어 분수'},
                      "AIUR_FOUNTAINS",
                      Developer.Luminous,
                      ["Base.SC2Data/GameData/Terrain/AiurFountains.xml"],
                      False,
                      None)
    Kaldir_Cliffs = ({Language.English: 'Kaldir Cliffs', Language.Korean: '칼디르 절벽'},
                     "KALDIR_CLIFFS",
                     Developer.Understudy,
                     ["Base.SC2Data/GameData/Terrain/KaldirCliffs.xml"],
                     True,
                     None)

    # galaxy representation is the string value of the Preset in KS2 Galaxy
    def __init__(self, name_dict: dict,
                 galaxy_representation: str,
                 original_author: Developer,
                 custom_file_list: list[str],
                 map_available: bool = False,
                 current_author: Developer = None):
        self._name_dict = name_dict
        self._galaxy_representation = galaxy_representation
        self._custom_file_list = custom_file_list
        self._original_author = original_author
        self._current_author = original_author if current_author is None else current_author
        self._map_available = map_available

    def get_name(self, locale: Language):
        return self._name_dict[locale]

    def get_english_name(self):
        return self.get_name(Language.English)

    def get_galaxy_representation(self):
        return self._galaxy_representation

    def original_author(self):
        return self._original_author

    def current_author(self):
        return self._current_author

    def is_map_available(self):
        return self._map_available

    def custom_file_list(self):
        return self._custom_file_list
