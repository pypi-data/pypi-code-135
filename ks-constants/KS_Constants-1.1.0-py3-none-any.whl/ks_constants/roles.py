from enum import Enum
from devs import Developer


class Team(Enum):
    Survivor = 0
    Kerrigan = 1


class RoleType(Enum):
    Builder = (0, Team.Survivor)
    Support = (1, Team.Survivor)
    Defender = (2, Team.Kerrigan)
    Hunter = (3, Team.Kerrigan)

    def __init__(self, _id: int, team: Team):
        self._id = id
        self._team: team

    def get_team(self):
        return self._team

class Role(Enum):
    Kerrigan = (0, RoleType.Hunter, {'en': 'Kerrigan', 'kr': '케리건'}, Developer.geo, Developer.Luminous, True)
    Scientist = (1, RoleType.Builder, {'en': 'Scientist', 'kr': '과학자'}, Developer.geo, Developer.Luminous, True)
    Dark_Templar = (2, RoleType.Support, {'en': 'Dark Templar', 'kr': '암흑기사'}, Developer.geo, Developer.Luminous, True)
    Ascendant = (3, RoleType.Builder, {'en': 'Ascendant', 'kr': '승천자'}, Developer.Luminous, None, True)
    Spirit = (4, RoleType.Builder, {'en': 'Spirit', 'kr': '혼령'}, Developer.Luminous, None, True)
    Ares = (5, RoleType.Builder, {'en': 'Ares', 'kr': '아레스'}, Developer.Luminous, None, True)
    Prophet = (6, RoleType.Support, {'en': 'Prophet', 'kr': '선지자'}, Developer.Luminous, None, True)
    Stukov = (7, RoleType.Builder, {'en': 'Stukov', 'kr': '스투코프'}, Developer.Luminous, None, True)
    Artanis = (8, RoleType.Builder, {'en': 'Artanis', 'kr': '아르타니스'}, Developer.Luminous, None, True)
    Zagara = (9, RoleType.Defender, {'en': 'Zagara', 'kr': '자가라'}, Developer.Luminous, None, True)
    Engineer = (10, RoleType.Builder, {'en': 'Engineer', 'kr': '공학자'}, Developer.Luminous, None, True)
    Team_Nova = (11, RoleType.Support, {'en': 'Team Nova', 'kr': '팀노바'}, Developer.Luminous, None, True)
    Nomad = (12, RoleType.Builder, {'en': 'Nomad', 'kr': '유랑선'}, Developer.Luminous, None, True)
    Dehaka = (13, RoleType.Hunter, {'en': 'Dehaka', 'kr': '데하카'}, Developer.Luminous, None, True)
    Helios = (14, RoleType.Builder, {'en': 'Helios', 'kr': '헬리오스'}, Developer.Luminous, None, True)
    Random = (15, None, {'en': 'Random', 'kr': '무작위'}, Developer.Luminous, None, True)
    Thakras = (16, RoleType.Hunter, {'en': 'Thakras', 'kr': '타크라스'}, Developer.Luminous, None, True)
    Swann = (17, RoleType.Support, {'en': 'Swann', 'kr': '스완'}, Developer.Luminous, None, True)
    Warden = (18, RoleType.Support, {'en': 'Warden', 'kr': '수호자'}, Developer.Luminous, None, True)
    Selendis = (19, RoleType.Builder, {'en': 'Selendis', 'kr': '셀렌디스'}, Developer.hex, Developer.Susu, True)
    Niadra = (20, RoleType.Defender, {'en': 'Niadra', 'kr': '니아드라'}, Developer.Luminous, None, True)
    Mira = (21, RoleType.Builder, {'en': 'Mira', 'kr': '미라'}, Developer.Luminous, None, True)
    Scion = (22, RoleType.Support, {'en': 'Scion', 'kr': '후계자'}, Developer.Luminous, None, True)
    Technician = (23, RoleType.Builder, {'en': 'Technician', 'kr': '기술자'}, Developer.Fatline, Developer.Sox, True)
    Warfield = (24, RoleType.Builder, {'en': 'Warfield', 'kr': '워필드'}, Developer.Fatline, Developer.Sox, True)
    Champion = (25, RoleType.Builder, {'en': 'Champion', 'kr': '챔피언'}, Developer.Luminous, None, True)
    Elementalist = (26, RoleType.Support, {'en': 'Elementalist', 'kr': '원소술사'}, Developer.Fatline, Developer.Sox, True)
    Brakk = (27, RoleType.Hunter, {'en': 'Brakk', 'kr': '브라크'}, Developer.Fatline, Developer.Sox, True)
    Glevig = (28, RoleType.Defender, {'en': 'Glevig', 'kr': '글레빅'}, Developer.Fatline, Developer.Sox, True)
    Delta_Squad = (29, RoleType.Support, {'en': 'Delta Squad', 'kr': '델타 특공대'}, Developer.Luminous, None, True)
    Phaegore = (30, RoleType.Defender, {'en': 'Phaegore', 'kr': '파에고르'}, Developer.Templar, None, True)
    Alarak = (31, RoleType.Builder, {'en': 'Alarak', 'kr': '알라라크'}, Developer.Luminous, None, True)
    Izsha = (32, RoleType.Defender, {'en': 'Izsha', 'kr': '이즈샤'}, Developer.Susu, None, True)
    Malus = (33, RoleType.Hunter, {'en': 'Malus', 'kr': '말러스'}, Developer.Susu, None, True)
    Kraith = (34, RoleType.Hunter, {'en': 'Kraith', 'kr': '크레이스'}, Developer.Templar, None, True)
    Energizer = (35, RoleType.Builder, {'en': 'Energizer', 'kr': '에너자이저'}, Developer.Fatline, Developer.Sox, True)
    Andor = (36, RoleType.Builder, {'en': 'Andor', 'kr': '안도르'}, Developer.Korneel, None, True)
    DJ = (37, RoleType.Builder, {'en': 'DJ', 'kr': 'DJ'}, Developer.Sox, None, True)
    Rattlesnake = (38, RoleType.Support, {'en': 'Rattlesnake', 'kr': '방울뱀'}, Developer.Legacy, Developer.Templar, True)
    SgtHammer = (39, RoleType.Builder, {'en': 'SgtHammer', 'kr': '해머 상사'}, Developer.Archlei, Developer.Sox, True)
    Chew = (40, RoleType.Support, {'en': 'Chew', 'kr': '추'}, Developer.Sox, None, True)
    Aewyn = (41, RoleType.Builder, {'en': 'Aewyn', 'kr': '애윈'}, Developer.Luminous, None, True)

    def __init__(self,
                 _id: int,
                 role_type: RoleType,
                 name: dict,
                 original_author: Developer,
                 current_author: Developer,
                 available: bool
                 ):
        self._index = _id
        self._name = name
        self._role_type = role_type
        self._original_author = original_author
        self._current_author = original_author if current_author is None else current_author
        self._available = available

    @classmethod
    def from_index(cls, index):
        return list(Role)[index]

    def get_role_type(self):
        return self._role_type

    def get_name(self):
        return self._name

    def get_original_author(self):
        return self._original_author

    def get_current_author(self):
        return self._current_author

    def is_available(self):
        return self._available
