"""deck module
"""
import random
from typing import Union
from typing import List
from .error import CardError
from .error import DeckError
from .card import Card
from .logger import log


class Deck:
    """Implement operations on a deck of cards
    """
    def __init__(self, shuffle=True):
        """When building a deck, decide if it's initially shuffled.

        Parameters
        ----------
        shuffle : bool, optional
            If true, deck is shuffled, by default True
        """
        self.build()
        if shuffle:
            self.shuffle()

    def build(self, shuffle=False):
        self.__pack = [
            Card(R, S) for S in Card.suits_symbols \
                for R in Card.ranks
        ]
        self.__pack_dict = {
            card.label: card for card in self.__pack
        }
        self.__wastepile = []
        self.__stock = []
        self.logger = log(self.__class__.__name__)
        if shuffle:
            self.shuffle()

    def shuffle(self,):
        random.shuffle(self.__pack)

    def draw(self,) -> Card:
        """Pops 1 card from Card.pack and
        append to Card.stock

        Returns
        -------
        Card
            Popped card.
        """
        if len(self.__pack) > 0:
            self.__stock.append(self.__pack.pop())
            return self.__stock[-1]
        else:
            self.logger.warning("Draw from empty pack returns None.")
            return None

    def throw(self, c: Card):
        """Throw card c from Card.stock to 
        waste pile.

        Parameters
        ----------
        c : Card
            valid card

        Raises
        ------
        CardError
            _description_
        """
        if len(self.__stock) > 0:
            if c.label in self.stock_labels():
                for card in self.__stock:
                    if c.label == card.label:
                        self.__wastepile.append(card)
                        self.__stock.remove(card)
                        break
            else:
                raise CardError("Card don't belong to deck.")
        else:
            self.logger.info("No card in game.")

    def waste(self, c: Union[Card, None] = None):
        """Takes card c from Deck.pack and discards it to
        Deck.wastepile

        Parameters
        ----------
        c : Card | None
            Valid card from decksofcard.Card. If None is given,
            it picks the card from the top of the pack

        Returns
        -------
        Card
            Card to be wasted

        Raises
        ------
        ValueError
            raised when c is not from Deck.pack
        """
        if len(self.__pack) > 0:
            if c is None:
                    self.__wastepile.append(self.__pack.pop())
            elif c.label in self.pack_labels():
                card = self.__pack_dict[c.label]
                self.__wastepile.append(card)
                self.__pack.remove(card)
            else:
                raise CardError("Card don't belong to pack.")
        else:
            self.logger.info("Pack is empty")

    def pick(self, c: Union[Card, None] = None):
        """Pick card c from Deck.pack and append it to
        Deck.stock

        Parameters
        ----------
        c : Card | None
            Valid card from decksofcard.Card. If None is given,
            it picks the card from the top of the pack

        Returns
        -------
        Card
            Card picked

        Raises
        ------
        ValueError
            raised when c is not from Deck.pack
        """
        if len(self.__pack) > 0:
            if c is None:
                return self.draw()
            elif c.label in self.pack_labels():
                card = self.__pack_dict[c.label]
                self.__stock.append(card)
                self.__pack.remove(card)
                return self.__stock[-1]
            else:
                raise CardError("Card not in pack.")
        else:
            self.logger.warning("Picking from empty pack returns None.")
            return None

    def reset(self,):
        self.build(shuffle=True)

    def stock_labels(self,) -> list:
        return self.list_labels(self.__stock)

    def pack_labels(self,) -> list:
        return self.list_labels(self.__pack)

    def list_labels(self, pile: List[Card]) -> list:
        if len(pile) > 0:
            return [c.label for c in pile]
        else:
            return []
    
    def deal(self, n_players=2, n_cards=2, standard=True) -> List[List[Card]]:
        total_requested = n_players*n_cards
        if total_requested > 52:
            message = f"Requested {total_requested} cards. "
            message += f"Not enough cards on pack ({len(self.__pack)})"
            raise DeckError(message)
        hand = [[] for _ in range(n_players)]
        if standard:
            for i in range(n_cards):
                for j in range(n_players):
                    hand[i].append(self.draw())
        else:
            for j in range(n_players):
                for i in range(n_cards):
                    hand[j].append(self.draw())
        return hand


    @property
    def pack(self,):
        return self.__pack

    @property
    def stock(self,):
        return self.__stock

    @property
    def wastepile(self,):
        return self.__wastepile
