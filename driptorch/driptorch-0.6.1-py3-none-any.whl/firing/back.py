"""
Pattern generator for backing fire
"""

# Core imports
import warnings

# Internal imports
from ._base import FiringBase
from ..unit import BurnUnit
from ..personnel import IgnitionCrew
from ..pattern import Pattern
from ..warnings import CrewSizeWarning


class Back(FiringBase):

    def __init__(self, burn_unit: BurnUnit, ignition_crew: IgnitionCrew):

        # Check number of igniters
        if len(ignition_crew) > 1:
            ignition_crew = IgnitionCrew.from_list([ignition_crew[0]])
            warnings.warn(CrewSizeWarning.only_using_one)

        # Initialize the base class
        super().__init__(burn_unit, ignition_crew)

    def generate_pattern(self, offset: float) -> Pattern:
        """Generate backing fire ignition pattern

        Args:
            offset (float): Offset distance in meters from the unit boundary

        Returns:
            Pattern: Spatiotemporal ignition pattern
        """

        return self._generate_pattern(offset=offset, align=False)

    def _init_paths(self, paths: dict, **kwargs) -> dict:
        """Initialize spatial part of the ignition paths.

        Notes:
            Overrides the `_init_paths()` method in the base class

        Args:
            paths (dict): Empty pattern path dictionary

        Returns:
            dict: Pattern path dictionary with initial untimed paths
        """

        # Buffer the unit by the specified offset
        firing_area = self._burn_unit.buffer_control_line(
            kwargs.get('offset', 0))

        # Extract the fore line from the boundary segments object
        fore_line = firing_area.polygon_segments.fore

        # Only one heat and one igniter
        paths['heat'] = [0]
        paths['igniter'] = [0]
        paths['leg'] = [0]
        paths['geometry'] = [fore_line]

        return paths
