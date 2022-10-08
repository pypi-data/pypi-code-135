import unittest

from src.devs import Developer
from src.maps import Map
from src.roles import Hero, RoleType

class TestStringMethods(unittest.TestCase):

    def test_maps(self):
        self.assertEqual(Map.Aiur_Fountains.original_author(), Developer.Luminous)
        self.assertEqual(Map.Ruins_Of_Imladoon.original_author(), Developer.Fatline)
        self.assertEqual(Map.Ruins_Of_Imladoon.current_author(), Developer.Templar)
        self.assertFalse(Map.Vintage_Shores.is_map_available())

    def test_roles(self):
        self.assertEqual(Hero.Ares.get_current_author(), Hero.Aewyn.get_current_author())
        self.assertEqual(Hero.Ascendant.get_role_type(), RoleType.Builder)
        self.assertEqual(Hero.Dark_Templar.get_role_type(), RoleType.Support)
        self.assertEqual(Hero.Brakk.get_role_type(), RoleType.Hunter)
        self.assertEqual(Hero.from_index(5), Hero.Ares)

if __name__ == '__main__':
    unittest.main()