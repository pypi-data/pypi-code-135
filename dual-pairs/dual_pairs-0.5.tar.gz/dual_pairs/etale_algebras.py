# -*- coding: utf-8 -*-
r"""
Étale algebras over :math:`\mathbf{Q}.
"""

from __future__ import absolute_import

from sage.categories.algebras import Algebras
from sage.categories.cartesian_product import cartesian_product

class EtaleAlgebras(Category):
    def super_categories(self):
        return [Algebras(QQ).Commutative().CartesianProducts()]

    class ParentMethods:
        def __init_extra__(self):
            pass

    def ideal_monoid(self):
        pass
