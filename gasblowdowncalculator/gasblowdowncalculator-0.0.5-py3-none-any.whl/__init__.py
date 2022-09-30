# This file is part of GasBlowdownCalculator.

from . import calculation
from . import gas
from . import results
from . import ui

from . import dataModelCalculation
from . import gasblowdowncalculator
from . import simulation

__all__ = ['calculation',
           'gas',
           'results',
           'ui',
           'dataModelCalculation',
           'gasblowdowncalculator',
           'simulation',
           ]


def main():
    """Entry point for the application script"""
    print("Starting GasBlowdownCalculator from command line")
    gasblowdowncalculator.run()
