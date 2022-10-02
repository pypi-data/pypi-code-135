from .logger import log


class CardError(Exception):
    """Handle errors related to card operations on Deck
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.logger = log(self.__class__.__name__)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self,):
        if self.message is None:
            self.message = "Failed dealing card."
        self.logger.error(self.message)
        return self.message


class DeckError(Exception):
    """Handle errors related to card operations on Deck
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.logger = log(self.__class__.__name__)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self,):
        if self.message is None:
            self.message = "Invalid action on deck."
        self.logger.error(self.message)
        return self.message