"""This module provides inductance support.

Copyright 2021 Michael Hayes, UCECE

"""
from .cexpr import cexpr
from .units import u as uu

def inductance(arg, **assumptions):

    expr1 = cexpr(arg, **assumptions)
    expr1.units = uu.henry

    return expr1
