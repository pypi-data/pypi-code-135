class NoneVariableException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FoundKeyNameException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)