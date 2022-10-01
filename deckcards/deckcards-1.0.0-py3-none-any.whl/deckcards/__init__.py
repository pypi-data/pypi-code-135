"""Deack of cards module
"""
__version__ = "1.0.0"

from .card import Card
from .deck import Deck
from .error import CardError
from .error import DeckError
from . import examples

__all__ = [
    "Card",
    "CardError",
    "Deck",
    "DeckError",
    "examples"
]
