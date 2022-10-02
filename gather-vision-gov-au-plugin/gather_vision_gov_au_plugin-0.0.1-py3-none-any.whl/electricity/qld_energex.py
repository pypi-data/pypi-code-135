import dataclasses
import typing

from gather_vision import model


@dataclasses.dataclass
class QueenslandEnergexElectricityItem:
    pass


class QueenslandEnergexElectricity(model.WebData):

    demand_min = 0
    demand_max = 5500

    base_url = "https://www.energex.com.au"
    demand_url = f"{base_url}/static/Energex/Network%20Demand/networkdemand.txt"

    def initial_urls(self) -> typing.Iterable[str]:
        return [self.list_url]

    def parse_response(
        self, data: model.WebDataAvailable
    ) -> typing.Generator[typing.Union[str, model.IsDataclass], typing.Any, typing.Any]:
        pass
