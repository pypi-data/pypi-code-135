import dataclasses
import typing

from gather_vision import model


@dataclasses.dataclass
class QueenslandFuelItem:
    pass


class QueenslandFuel(model.WebData):
    def initial_urls(self) -> typing.Iterable[str]:
        return [self.list_url]

    def parse_response(
        self, data: model.WebDataAvailable
    ) -> typing.Generator[typing.Union[str, model.IsDataclass], typing.Any, typing.Any]:
        pass
