"""ABCClassifier testing"""
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from abc_classification.abc_classifier import ABCClassifier


class Test(unittest.TestCase):
    """Class for ABCClassifier testing"""
    def setUp(self) -> None:
        self.abc_classifier = ABCClassifier(pd.read_csv('товары.txt', sep='\t'))
        self.true_abc = pd.read_csv('abc_товары.txt')

    def test_classify(self):
        """Test ABCClassifier.classify()"""
        assert_frame_equal(self.abc_classifier.classify('товар', 'сумма'),
                           self.true_abc)
        self.assertRaises(ValueError, self.abc_classifier.classify, 0, 1)
        self.assertRaises(ValueError, ABCClassifier, 'data')


if __name__ == "__main__":
    unittest.main()
