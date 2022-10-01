from .user import UserCompact
from dateutil import parser

from ..util import prettify


class SeasonalBackgrounds:
    """
    Contains data on the seasonal backgrounds.

    **Attributes**

    ends_at: :class:`datetime.datetime`
        The date when the seasonal backgrounds will end.

    backgrounds: Sequence[:class:`SeasonalBackground`]
        A list of all the seasonal backgrounds.
    """
    __slots__ = ('ends_at', 'backgrounds')

    def __init__(self, data):
        self.ends_at = parser.parse(data['ends_at'])
        self.backgrounds = list(map(SeasonalBackground, data['backgrounds']))

    def __repr__(self):
        return prettify(self, 'ends_at', 'backgrounds')


class SeasonalBackground:
    """
    Represents a seasonal background.

    **Attributes**

    url: :class:`str`
        The url of the background.

    user: :class:`UserCompact`
        The artist of the background.
    """
    __slots__ = ('url', 'user')

    def __init__(self, data):
        self.url = data['url']
        self.user = UserCompact(data['user'])

    def __repr__(self):
        return prettify(self, 'url', 'user')
