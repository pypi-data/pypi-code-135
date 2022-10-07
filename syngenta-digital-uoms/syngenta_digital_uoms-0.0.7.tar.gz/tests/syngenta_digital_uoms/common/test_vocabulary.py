from unittest import TestCase

from syngenta_digital_uoms.common.vocabulary import Vocabulary, UnsupportedVocabularyException


class TestVocaulary(TestCase):
    def setUp(self) -> None:
        self.__vocab = Vocabulary()

    def test_unsupported_vocab(self):
        with self.assertRaises(UnsupportedVocabularyException):
            Vocabulary(vocab_type='unsupported_type')

    def test_get_dimension(self):
        dimension = self.__vocab.get_dimension('ft')
        self.assertEqual(dimension, 'DISTANCE')

    def test_list_dimensions(self):
        dimensions = self.__vocab.list_dimensions()
        self.assertEqual(dimensions, ['DISTANCE', 'TIME', 'TEMPERATURE', 'MASS', 'PERCENT', 'UNITLESS', 'AREA', 'VOLUME', 'SPEED', 'MASS_PER_AREA', 'VOLUME_PER_AREA', 'ANGLE', 'MASS_PER_VOLUME', 'VOLUME_PER_TIME', 'CONTAINER', 'BAG', 'TIMESPAN', 'BARREL', 'SACK', 'CONTAINER_PER_AREA', 'BAG_PER_AREA', 'BARREL_PER_AREA', 'SACK_PER_AREA', 'BALE', 'BALES_PER_AREA', 'BALES_PER_MASS', 'BALES_PER_TIME', 'MASS_PER_BALE', 'BALES_PER_VOLUME', 'CURRENCY', 'CURRENCY_PER_CONTAINER', 'CURRENCY_PER_BAG', 'MASS_PER_CONTAINER', 'MASS_PER_BAG', 'MASS_PER_BARREL', 'MASS_PER_SACK', 'CURRENCY_PER_BALE', 'CURRENCY_PER_AREA', 'CURRENCY_PER_VOLUME', 'CURRENCY_PER_TIME', 'SEEDS', 'DATA_POINTS', 'SEEDS_PER_AREA', 'SEEDS_PER_MASS', 'SEEDS_PER_TIME', 'SEEDS_PER_VOLUME', 'SEEDS_PER_CONTAINER', 'SEEDS_PER_BAG', 'SEEDS_PER_BARREL', 'SEEDS_PER_SACK', 'MASS_PER_SEEDS', 'DATA_POINTS_PER_TIME', 'ROWS', 'AREA_PER_TIME', 'MASS_PER_TIME', 'VOLUME_PER_MASS', 'PRESSURE', 'FORCE', 'ANGULAR_VELOCITY', 'DISTANCE_PER_PERCENT', 'DISTANCE_PER_DEGREE', 'FREQUENCY', 'COUNT', 'MASS_PER_MASS', 'VOLUME_PER_VOLUME', 'VOLTAGE', 'ELECTRIC_CURRENT', 'FIELD', 'PER_CONTAINER', 'PER_BAG', 'PER_SACK', 'PER_VOLUME', 'PER_MASS', 'PER_AREA', 'PER_FIELD', 'PER_TIME', 'PER_BALE', 'COUNT_PER_AREA', 'VOLUME_PER_DISTANCE', 'MASS_PER_DISTANCE', 'ENERGY', 'POWER'])

    def test_list_dimension_uoms(self):
        dimensional_uoms = self.__vocab.list_dimension_uoms('DISTANCE')
        self.assertEqual(dimensional_uoms, ['m', 'ft', 'in', 'mi', 'Nmi', 'yd', 'Em', 'Pm', 'Tm', 'Gm', 'Mm', 'km', 'hm', 'dam', 'dm', 'cm', 'mm', 'um', 'nm', 'pm', 'fm', 'am', '100m', '100yd'])

    def test_get_canonical_uom(self):
        canonical_uom = self.__vocab.get_canonical_uom('DISTANCE')
        self.assertEqual(canonical_uom, 'm')

    def test_get_factor_and_offset(self):
        factor, offset = self.__vocab.get_factor_and_offset('km')
        self.assertEqual(factor, 1000)
        self.assertEqual(offset, 0)

