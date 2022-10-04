from dataclasses import dataclass
from enum import Enum


class WsMethodEnum(Enum):
    SUBSCRIBE = "subscribe"
    UNSUBSCRIBE = "unsubscribe"


@dataclass
class WsMethod:
    subscribe: str
    unsubscribe: str


class WsChannelEnum(Enum):
    TRADE = "trade"
    BOOK_TICKER = "book_ticker"


@dataclass
class WsChannel:
    trade: str
    book_ticker: str