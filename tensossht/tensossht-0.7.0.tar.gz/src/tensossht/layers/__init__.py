"""
**************************
TensoSSHT Layers for Keras
**************************

This module provides thin wrappers around the harmonic transforms to make them
`keras <https://www.tensorflow.org/api_docs/python/tf/keras>`__  layers.

.. automodule:: tensossht.layers.harmonic_transforms
.. automodule:: tensossht.layers.wigner
.. automodule:: tensossht.layers.memory_layout

API
===

.. autoclass:: tensossht.layers.harmonic_transforms.ForwardLayer
    :members:

.. autoclass:: tensossht.layers.harmonic_transforms.ForwardSpinLayer
    :members:

.. autoclass:: tensossht.layers.harmonic_transforms.InverseLayer
    :members:

.. autoclass:: tensossht.layers.harmonic_transforms.InverseSpinLayer
    :members:

.. autofunction:: tensossht.layers.wigner.wigner_layer

.. autoclass:: tensossht.layers.wigner.ForwardWignerLayer
    :members:

.. autoclass:: tensossht.layers.wigner.InverseWignerLayer
    :members:

.. autoclass:: tensossht.layers.wigner.FourierLayer
    :members:

.. autoclass:: tensossht.layers.memory_layout.PackingLayer
    :members:

.. autoclass:: tensossht.layers.memory_layout.UnpackingLayer
    :members:
"""

from tensossht.layers.harmonic_transforms import (
    ForwardLayer,
    ForwardSpinLayer,
    InverseLayer,
    InverseSpinLayer,
)
from tensossht.layers.memory_layout import PackingLayer, UnpackingLayer
from tensossht.layers.wigner import wigner_layer

__all__ = [
    "ForwardLayer",
    "ForwardSpinLayer",
    "InverseLayer",
    "InverseSpinLayer",
    "PackingLayer",
    "UnpackingLayer",
    "wigner_layer",
]
