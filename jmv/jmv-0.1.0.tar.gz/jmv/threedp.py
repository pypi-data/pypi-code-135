#!/usr/bin/env python
# coding: utf-8

# Copyright (c) KaivnD.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""
from typing import Any
from traitlets import Unicode, CInt, List, Dict
from ipywidgets import DOMWidget
from traitlets import Unicode
from ._frontend import module_name, module_version

_hidden_element = []

def hide(*args):
    for item in args:
        _hidden_element.append(item)

class DisplayPortal(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('DisplayPortalModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('DisplayPortalView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    _width = CInt(200).tag(sync=True)
    _height = CInt(200).tag(sync=True)

    meshbuffers = List().tag(sync=True)
    wirebuffers = List().tag(sync=True)
    options = Dict().tag(sync=True)

    def __init__(self, height=200, _option={}, **kwargs):
        super(DisplayPortal, self).__init__(**kwargs)
        self._height = height
        self.options = _option

        mbuffers = []
        wbuffers = []

        import inspect
        frame = inspect.currentframe()
        try:
            elements = []

            for val in frame.f_back.f_locals.values():
                if val in _hidden_element:
                    continue

                if "__display__" in dir(val) and not inspect.isclass(val):
                    tmp = val.__display__()
                    tmp = tmp if isinstance(tmp, list) else [tmp]
                    for item in tmp:
                        elements.append(item)
                else:
                    if isinstance(val, list):
                        elements += val
                    else:
                        elements.append(val)

            for val in elements:
                if "_repr_3dp_" in dir(val) and not inspect.isclass(val):
                    meshes, wires = val._repr_3dp_()
                    mbuffers += meshes
                    wbuffers += wires

        finally:
            del frame

        self.meshbuffers = list(self.meshbuffers) + mbuffers
        self.wirebuffers = list(self.wirebuffers) + wbuffers

    def appendWire(self, wires: Any) -> None:
        self.wirebuffers = list(self.wirebuffers) + [wires]

    def appendBuffers(self, buffers: list) -> None:
        self.meshbuffers = list(self.meshbuffers) + [buffers]