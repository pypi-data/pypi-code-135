class Path:
    DELIMITER = "/"

    def __init__(self, *parts: str):
        if any(self.DELIMITER in part for part in parts):
            raise ValueError(f"Path initialization must not contain delimiter character `{self.DELIMITER}`")

        self.parts = list(filter(bool, parts))

    @staticmethod
    def from_child_path(path: str) -> str:
        assert isinstance(path, str), "Child path must be a string"
        return Path.from_path(path).parent.resolve()

    @classmethod
    def from_path(cls, path: str):
        assert isinstance(path, str), "Path must be a string"
        return cls(*path.split(cls.DELIMITER))

    @property
    def parent(self):
        return Path(*self.parts[:-1])

    def resolve(self):
        return self.DELIMITER + self.DELIMITER.join(self.parts)

    def is_parent_of(self, other: "Path") -> bool:
        return self.parts == other.parts[: len(self.parts)]

    def is_child_of(self, other: "Path") -> bool:
        return other.is_parent_of(self)

    def __truediv__(self, other: str):
        return Path(*self.parts, other)

    def __eq__(self, other):
        return self.parts == other.parts

    def chain(self):
        parent = self.parent

        if self != parent:
            yield from parent.chain()

        yield self


# Reserved paths
SERVICE_PATH = Path(".backbone")
SERVICE_STREAM_PATH = SERVICE_PATH / "stream"
