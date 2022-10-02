import logging

from gather_vision import model
from gather_vision.plugin import Entry

from gather_vision_gov_au_plugin.air.qld import QueenslandAir
from gather_vision_gov_au_plugin.election.national import AustraliaElection
from gather_vision_gov_au_plugin.electricity.qld_energex import (
    QueenslandEnergexElectricity,
)
from gather_vision_gov_au_plugin.electricity.qld_ergon_energy import (
    QueenslandErgonEnergyElectricity,
)
from gather_vision_gov_au_plugin.petition.national import AustralianGovernmentPetitions
from gather_vision_gov_au_plugin.petition.qld import QueenslandGovernmentPetitions
from gather_vision_gov_au_plugin.petition.qld_bne import BrisbaneCityCouncilPetitions
from gather_vision_gov_au_plugin.transport.qld_fuel import QueenslandFuel

logger = logging.getLogger(__name__)


class PluginEntry(Entry):
    """The entry class for the plugin."""

    name = "gov_au"

    _data_sources = [
        # air
        QueenslandAir,
        # election
        AustraliaElection,
        # electricity
        QueenslandEnergexElectricity,
        QueenslandErgonEnergyElectricity,
        # government
        # petition
        AustralianGovernmentPetitions,
        QueenslandGovernmentPetitions,
        BrisbaneCityCouncilPetitions,
        # transport
        QueenslandFuel,
        # water
    ]

    def update(self, args: model.UpdateArgs) -> model.UpdateResult:
        logger.info(f"Update {self.name}")
        return model.UpdateResult()

    def list(self, args: model.ListArgs) -> model.ListResult:
        logger.info(f"List {self.name}")
        data_source_names = sorted(
            [
                f"{'.'.join(i.__module__.split('.')[1:])}.{i.__name__}"
                for i in self._data_sources
            ]
        )
        return model.ListResult({self.name: data_source_names})
