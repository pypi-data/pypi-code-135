"""
Interface to Ekster.
"""

from amuse.units import nbody_system, units
from amuse.community import (
    # CodeInterface,
    LegacyFunctionSpecification,
    legacy_function,
    LiteratureReferencesMixIn,
)

from amuse.community.interface.gd import (
    GravitationalDynamicsInterface,
    GravitationalDynamics,
    # GravityFieldInterface,
    GravityFieldCode,
)
from amuse.community.interface.se import (
    StellarEvolutionInterface,
    StellarEvolution,
)

from amuse.community.interface.stopping_conditions import (
    StoppingConditionInterface,
    StoppingConditions,
)
from ekster.run import ClusterInPotential


# class EksterInterface(
#     # CodeInterface,
#     LiteratureReferencesMixIn,
#     GravitationalDynamicsInterface,
#     StellarEvolutionInterface,
#     StoppingConditionInterface,
#     ClusterInPotential,
# ):
#     def __init__(self, **options):
#         ClusterInPotential.__init__(
#             self,
#             **options
#         )
# 

class Ekster(
    # EksterInterface,
    LiteratureReferencesMixIn,
    GravitationalDynamics,
    StellarEvolution,
):
    """
    Ekster is an AMUSE-based method for simulating embedded star clusters.

    References:
        .. [#] Rieder, Steven et al. [2022MNRAS.509.6155R]

        Grouped star formation:
        .. [#] Liow, Kong You et al. [2022MNRAS.510.2657L]
    """
    def __init__(self, **options):
        # EksterInterface.__init__(self, **options)
        LiteratureReferencesMixIn.__init__(self)
        self.__code = ClusterInPotential()

    
