import pytest
from deckcards import Card
from deckcards import CardError

def test_card_suit():
    """Checks if adding space to valid suit string still
    raises CardError.
    """
    with pytest.raises(CardError):
        suit = "spade "
        Card('2', suit)

def test_card_value():
    """Checks if adding space to valid suit string still
    raises CardError.
    """
    with pytest.raises(CardError):
        suit = "spade"
        card = Card('A', suit)
        card.value = 1.0
