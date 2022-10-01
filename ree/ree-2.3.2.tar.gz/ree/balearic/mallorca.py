from typing import Union

from ..core import Scraper


class Mallorca(Scraper):

    def __init__(self, session=None, verify=True):
        super(self.__class__, self).__init__(session, verify)

    def get(self, date: Union[str, None]=None, last=True):
        return super(self.__class__, self).get("MALLORCA5M", "Europe/Madrid", "Baleares", date, last)

    def get_all(self, date: Union[str, None]=None):
        return self.get(date, False)
