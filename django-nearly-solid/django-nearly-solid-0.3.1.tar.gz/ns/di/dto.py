from dataclasses import dataclass


@dataclass
class Dependency:
    name: str
    interface: type
    impl: object
