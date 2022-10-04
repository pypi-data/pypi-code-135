import typing


class CordException(Exception):
    pass


class CordTypeError(CordException, TypeError):
    def __init__(self, expectation: str, received: typing.Any):
        super().__init__(f"Expected {expectation}, received '{received}' of type '{type(received).__name__}'")


class CordValueError(CordException, ValueError):
    pass


class CordExhaustedBufferError(CordException, EOFError):
    def __init__(self, field_type: str):
        super().__init__(f"Reached end of input while decoding {field_type}")
