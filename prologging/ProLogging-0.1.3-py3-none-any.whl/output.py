class Output:
    def __init__(self, pretty: bool = True) -> None:
        self.pretty = pretty

    def __call__(self, msg: str = None, type: str = "INFO") -> None:
        print(f"[{type}] {msg}")