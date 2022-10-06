from collections.abc import Iterable
from typing import Type

from dar_etl.parsing.parser import DarParser
from dar_etl.schemas.address import Adresse
from dar_etl.schemas.address_point import AddressPoint
from dar_etl.schemas.base_model import DarBaseModel
from dar_etl.schemas.house_number import HouseNumber
from dar_etl.schemas.named_road import NamedRoad
from dar_etl.schemas.named_road_municipal_district import NamedRoadMunicipalDistrict
from dar_etl.schemas.named_road_postal_code import NamedRoadPostalCode
from dar_etl.schemas.named_road_supplementary_city_name import NamedRoadSupplementaryCityName
from dar_etl.schemas.postal_code import PostalCode
from dar_etl.schemas.root_keys import Root
from dar_etl.schemas.supplementary_city_name import SupplementaryCityName


class ParserFactory:
    _registry: dict[Root, Type[DarBaseModel]] = {
        Root.addresses: Adresse,
        Root.address_points: AddressPoint,
        Root.house_numbers: HouseNumber,
        Root.named_roads: NamedRoad,
        Root.named_road_municipal_parts: NamedRoadMunicipalDistrict,
        Root.named_road_postal_codes: NamedRoadPostalCode,
        Root.named_road_supplementary_city_names: NamedRoadSupplementaryCityName,
        Root.postal_codes: PostalCode,
        Root.supplementary_city_names: SupplementaryCityName,
    }

    @classmethod
    def create(cls, root: Root) -> DarParser:
        return DarParser(
            parsing_type=cls._registry[root],
            root=root,
        )

    @classmethod
    def create_all(cls) -> Iterable[DarParser]:
        yield from (
            DarParser(
                parsing_type=parsing_type,
                root=root,
            )
            for root, parsing_type in cls._registry.items()
        )
