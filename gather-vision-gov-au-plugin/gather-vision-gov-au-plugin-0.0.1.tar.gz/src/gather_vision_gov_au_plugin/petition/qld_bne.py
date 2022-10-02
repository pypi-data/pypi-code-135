import dataclasses

import typing
from gather_vision import model


@dataclasses.dataclass
class BrisbaneCityCouncilPetitionItem:
    pass


class BrisbaneCityCouncilPetitions(model.WebData):

    list_url = "https://www.epetitions.brisbane.qld.gov.au"
    # table.petitions
    # tbody.tr.th (headers)
    # tbody.tr.td (cells)

    item_url = f"{list_url}/petition/view/pid/${{item_id}}"

    # title: .page-title h1

    # content: #petition-page
    # table .petition-details (td.heading (headers),  td (no class) (values))

    # body: .petition-details

    def initial_urls(self) -> typing.Iterable[str]:
        return [self.list_url]

    def parse_response(
        self, data: model.WebDataAvailable
    ) -> typing.Generator[typing.Union[str, model.IsDataclass], typing.Any, typing.Any]:
        pass

        # Options (pick one):
        # - return BrisbaneCityCouncilPetitionItem
        # - return a list of urls to get and parse
