from .coordinate import Coordinate
from .resource import Resource


class Well(Resource):
  """ Base class for Well resources.

  Note that in regular use these will be automatically generated by the
  :class:`pylabrobot.liquid_handling.resources.abstract.Plate` class.
  """

  def __init__(self, name: str, size_x: float, size_y: float, size_z: float = 9,
    location: Coordinate = Coordinate(None, None, None), category: str = "well"):
    super().__init__(name, size_x=size_x, size_y=size_y, size_z=size_z,
      location=location, category="well")
    # TODO: max_volume: float,
    # self.max_volume = max_volume
