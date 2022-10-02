from .error import CardError


class Card:
    """Build single card
    Notes
    ------
        You must provide valids parameters to contructor.
        For suits: ♣, ♦, ♥, ♠, club, diamond, heart, spade
        For ranks: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K,

    Raises
    ------
    ValueError
        raised when provided invalid rank or suit

    Class attributes
    ----------
    suits_symbols: list
        Valids suit symbols.
    suits_keys: list
        Valids suit names.
    suits: dict
        Maps name to symbol.
    suit_name: dict
        Maps symbol to name.
    ranks
        Valids ranks.

    Attributes
    ----------
    suit : str
        Card's suit symbol, one of "♣ ♦ ♥ ♠".
    suit_name: str
        Card's suit name, one of "club diamond heart spade".
    rank : str
        Card's rank, one of "A 2 3 4 5 6 7 8 9 10 J Q K".

    """
    suits_symbols = "♣ ♦ ♥ ♠".split(' ')
    suits_keys = "club diamond heart spade".split(' ')
    suits = {k: v for k, v in zip(suits_keys, suits_symbols)}
    suits_name = {k: v for k, v in zip(suits_symbols, suits_keys)}
    ranks = "A 2 3 4 5 6 7 8 9 10 J Q K".split(" ")
    pictures = ranks[10:]
    values = {r: v + 1 for r, v in zip(ranks[1:],range(1, 14))}
    values["A"] = 13

    def __init__(self, rank, suit):
        """Provide valid rank and suit:
            You must provide valids parameters to contructor.
            - For suits, it must be one of:
                Card.suits_symbols or Card.suits_keys
            - For ranks, one of:
                Card.ranks
        Parameters
        ----------
        rank : str
            Card's rank: A 2 3 4 5 6 7 8 9 10 J Q or K
        suit : _type_
            Card's suit: ♣, ♦, ♥, ♠, club, diamond, heart or spade

        Raises
        ------
        ValueError
            raised when provided invalid rank or suit
        """
        if rank not in Card.ranks:
            raise ValueError(f"Card's rank must be one of {Card.ranks}")
        if suit not in Card.suits_symbols:
            if suit in Card.suits_keys:
                suit = Card.suits[suit]
            else:
                message = f"Card's suit must be one of {Card.suits_symbols} "
                message += f"or {Card.suits_keys}"
                raise CardError(message)
        self.__rank = rank
        self.__suit = suit
        self.__value = Card.values[self.__rank]
    @property
    def rank(self,) -> str:
        """Card's rank
        """
        return self.__rank
    @property
    def suit(self,) -> str:
        """Card's suit symbol
        """
        return self.__suit
    @property
    def value(self,) -> int:
        """Card's value
        """
        return self.__value
    @property
    def suit_name(self,) ->str:
        """Card's suit name
        """
        return Card.suits_name[self.__suit]
    @property
    def label(self,) -> str:
        """Label in format 'rank suit'

        Returns
        -------
        str
            card label
        """
        return self.__str__()
    @value.setter
    def value(self, v: int) -> int:
        if isinstance(v, int):
            self.__value = v
        else:
            raise CardError("Card's value must be integer.")
    def __repr__(self,):
        return f"Card.rank: {self.__rank}, Card.suit: {self.__suit}"

    def __str__(self,):
        return f"{self.__rank} {self.__suit}"
