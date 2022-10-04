# -*- coding: utf-8 -*-

# Author: Sebastian Avalos <sebastian.avalos@apmodtech.com>
#         Advanced Predictive Modeling Technology
#         www.apmodtech.com/pyAPMT/
#         Jun-2022
#
# License: MIT License


# All submodules and packages
from . import Geostatistics

# pyAPMT functions
from .Geostatistics.Drill_Holes import DrillHoles

__version__ = "0.0.10"

__requires__ = ['numpy','pandas', 'matplotlib', 'probscale', 'scipy', 'sklearn',
                'seaborn', 'pygeostat', 'pot']


#__all__ = ['Geostatistics', 'Contact_Analysis']