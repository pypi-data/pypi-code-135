import dataclasses
import typing

from gather_vision import model


@dataclasses.dataclass
class AustralianGovernmentPetitionItem:
    pass


class AustralianGovernmentPetitions(model.WebData):

    list_url = "https://www.aph.gov.au/e-petitions"
    item_url = f"{list_url}/petition/${{item_id}}"

    def initial_urls(self) -> typing.Iterable[str]:
        return [self.list_url]

    def parse_response(
        self, data: model.WebDataAvailable
    ) -> typing.Generator[typing.Union[str, model.IsDataclass], typing.Any, typing.Any]:
        pass
