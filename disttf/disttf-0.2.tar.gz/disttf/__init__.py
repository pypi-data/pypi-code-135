from .activate import ActivateLayer as GaussianRealisation
from .asym_activate import AsymActivateLayer as BiasedRealisation
from .box_activate import BoxyActivateLayer as BoxRealisation

from .mixture import MixtureLayer
from .motio import MotioLayer
from .scale import ScaleLayer
from .split import SplitLayer

from .nonlinearity import NonlinearityLayer
from .seperate import SeperateLayer
from .recombine import RecombineLayer

def pdense(x):
    x=MixtureLayer()(x)
    x=NonlinearityLayer()(x)
    return x

