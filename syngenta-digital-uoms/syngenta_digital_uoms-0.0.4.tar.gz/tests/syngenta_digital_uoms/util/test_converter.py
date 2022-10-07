from unittest import TestCase

from syngenta_digital_uoms.util.converter import Converter


class TestVocaulary(TestCase):
    def setUp(self) -> None:
        self.__converter = Converter()

    def test_convert_uom(self):
        result = self.__converter.convert_uom('ft')
        self.assertEqual(result, 'm')

    def test_convert_value(self):
        result = self.__converter.convert_value(input_uom_code='ft', input_value=100,
                                                output_uom_code='km')
        self.assertEqual(result, 0.03048)