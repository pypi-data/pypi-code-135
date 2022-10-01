#!/usr/bin/env python
# coding: utf-8

# Copyright (c) seerai.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""


from ipywidgets import DOMWidget
from IPython import get_ipython
from traitlets import Dict, Unicode, Int
from ._frontend import module_name, module_version


def on_button_clicked(change):
    print('button clicked', change)


class ObjectWidget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('ObjectModel').tag(sync=True)
    _model_module = Unicode('geodesic_widgets').tag(sync=True)
    _view_name = Unicode('ObjectView').tag(sync=True)
    _view_module = Unicode('geodesic_widgets').tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    # Your widget state goes here. Make sure to update the corresponding
    # JavaScript widget state (defaultModelProperties) in widget.ts
    # value = Unicode('Jupyter').tag(sync=True)
    object_value = Dict().tag(sync=True)

    def __init__(self, object_value={}, text_box=None, **kwargs):
        super().__init__(**kwargs)
        self.object_value = dict(object_value)
        self.text_box = text_box    
        self.on_msg(self.on_button_click)

    def on_button_click(self, _, content, buffer):
        if self.text_box is not None:
            self.text_box.value = str(self.dataset['alias'])
