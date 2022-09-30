# This file is part of GasBlowdownCalculator.

"""
.. module:: gas.gasData
   :synopsis: Data for gas composition setup.

.. moduleauthor:: Michael Fischer
"""


# Constants
EPSSUM_GAS = 0.01
ID_STATUSGAS_OK = 0
ID_STATUSGAS_FRACTION_OUTRANGE = 1
ID_STATUSGAS_FRACTIONSUM_OUTRANGE = 2

# Data
dataTabGasComponents = {0: ["methane",   "#c91414"],
                        1: ["ethane",    "#5311d9"],
                        2: ["propane",   "#2fe70b"],
                        3: ["isobutane", "#d0d717"],
                        4: ["n-butane",  "#ec0fc5"],
                        5: ["isopentane", "#036a5f"],
                        6: ["n-pentane", "#8c87fb"],
                        7: ["n-hexane",  "#d187fb"],
                        8: ["n-heptane", "#8347b5"],
                        9: ["n-octane",  "#7b4f4f"],
                        10: ["n-nonane", "#616332"],
                        11: ["n-decane", "#6ab15c"],
                        12: ["hydrogen sulfide", "#8164bc"],
                        13: ["nitrogen", "#c83b15"],
                        14: ["oxygen",   "#38e1cf"],
                        15: ["hydrogen", "#f6ea87"],
                        16: ["carbon dioxide",   "#0c04ac"],
                        17: ["carbon monoxide",  "#534c4e"],
                        18: ["helium",   "#9f5091"],
                        19: ["argon",    "#332f3a"],
                        }

nDataTabGasComponents = len(dataTabGasComponents.keys())
