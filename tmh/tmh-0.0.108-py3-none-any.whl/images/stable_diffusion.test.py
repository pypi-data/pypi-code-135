import unittest
from tmh.images.stable_diffusion import generate_image

class TestStringMethods(unittest.TestCase):

    def test_stable_diffusion(self):
        file_name = generate_image("Hilma Af Klint Endless Love", "hilma.png")
        # generate_with_image()
        self.assertTrue(isinstance(file_name, str))
if __name__ == '__main__':
    unittest.main()


