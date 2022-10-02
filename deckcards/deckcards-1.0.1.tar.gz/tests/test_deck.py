"""Tests on deck module
"""
import pytest
from deckcards import Deck
from deckcards import DeckError

def test_deck_deal():
    """Test error of exceeding numbers of cards
    resquested in dealing.
    """
    with pytest.raises(DeckError):
        n_players = 53
        n_cards = 1
        deck1 = Deck()
        deck1.deal(n_players=n_players, n_cards=n_cards)

# from deckofcards.module1 import Number


# class TestSimple(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual((Number(5) + Number(6)).value, 11)


# if __name__ == '__main__':
#     unittest.main()
