class InvalidRequestException(Exception):
    def __init__(self, message: str = "Request is not valid"):
        self.message = message
        super().__init__(self.message)


class InvalidCoinIDException(Exception):
    def __init__(self, message: str = "Coin ID is not valid"):
        self.message = message
        super().__init__(self.message)


class InvalidCurrencyException(Exception):
    def __init__(self, message: str = "Currency is not valid"):
        self.message = message
        super().__init__(self.message)


class InvalidTimestamp(Exception):
    def __init__(self, message: str = "Timestamp is not valid"):
        self.message = message
        super().__init__(self.message)
