from abc import ABC


class Error(Exception, ABC):
    pass


class CryptographyError(Error):
    pass
