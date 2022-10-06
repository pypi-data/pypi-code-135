"""
An example script for building a MultiLayerPerceptron using a yaml config file
"""
"""
Author: vickyparmar
File: building_mlp.py
Created on: 05-10-2022, Wed, 18:35:35

Last modified by: vickyparmar
Last modified on: 05-10-2022, Wed, 18:35:37
"""

# Imports
from core_of_theaisphere.utils.build_sequential_mlp import SequentialMLP

# Config file
config_file = "core_of_theaisphere/examples/mlp_config.yaml"

# Builder
builder = SequentialMLP(config_file)
mlp = builder.get_mlp()
mlp.summary()
