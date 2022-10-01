import unittest


class TestMyPackage(unittest.TestCase):

    def test_installation(self):
        import marcownpack

    def test_import_main(self):
        from package.marcownpack import main
