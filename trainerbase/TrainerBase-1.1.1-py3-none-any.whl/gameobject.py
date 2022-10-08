import typing
import trainerbase.memory


class GameObject:
    updated_objects = []

    def __init__(
        self,
        address: typing.Union[trainerbase.memory.Address, int],
        pm_read: typing.Callable,
        pm_write: typing.Callable,
        frozen=None,
    ):
        GameObject.updated_objects.append(self)

        self.address = trainerbase.memory.make_address(address)
        self.frozen = frozen
        self.pm_read = pm_read
        self.pm_write = pm_write

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}"
            f" at {hex(self.address.resolve())}:"
            f" value={self.value},"
            f" frozen={self.frozen}"
            ">"
        )

    def after_read(self, value):
        return value

    def before_write(self, value):
        return value

    @property
    def value(self):
        return self.after_read(self.pm_read(self.address.resolve()))

    @value.setter
    def value(self, new_value):
        self.pm_write(self.address.resolve(), self.before_write(new_value))

    @staticmethod
    def update_frozen_objects():
        for game_object in GameObject.updated_objects:
            if game_object.frozen is not None:
                game_object.value = game_object.frozen


class GameInt(GameObject):
    def __init__(self, pointer: typing.Union[trainerbase.memory.Address, int]):
        super().__init__(
            pointer,
            trainerbase.memory.pm.read_int,
            trainerbase.memory.pm.write_int,
        )


class GameFloat(GameObject):
    def __init__(self, pointer: typing.Union[trainerbase.memory.Address, int]):
        super().__init__(
            pointer,
            trainerbase.memory.pm.read_float,
            trainerbase.memory.pm.write_float,
        )

    def before_write(self, value):
        return float(value)


class GameByte(GameObject):
    def __init__(self, pointer: typing.Union[trainerbase.memory.Address, int]):
        super().__init__(
            pointer, trainerbase.memory.pm.read_char, trainerbase.memory.pm.write_char
        )

    def before_write(self, value: int):
        return value.to_bytes(1, "little").decode()

    def after_read(self, value):
        return int.from_bytes(value.encode(), "little")
