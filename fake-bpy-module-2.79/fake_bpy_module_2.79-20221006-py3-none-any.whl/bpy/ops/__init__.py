import sys
import typing
from . import scene
from . import sketch
from . import clip
from . import action
from . import render
from . import poselib
from . import group
from . import camera
from . import time
from . import nla
from . import palette
from . import paint
from . import info
from . import image
from . import paintcurve
from . import import_anim
from . import boid
from . import ptcache
from . import font
from . import screen
from . import import_scene
from . import logic
from . import brush
from . import import_curve
from . import object
from . import view3d
from . import node
from . import dpaint
from . import sound
from . import cycles
from . import export_mesh
from . import armature
from . import ui
from . import anim
from . import export_scene
from . import rigidbody
from . import pose
from . import buttons
from . import file
from . import uv
from . import sculpt
from . import import_mesh
from . import wm
from . import console
from . import fluid
from . import sequencer
from . import cachefile
from . import constraint
from . import particle
from . import curve
from . import world
from . import outliner
from . import cloth
from . import text
from . import surface
from . import graph
from . import transform
from . import safe_areas
from . import gpencil
from . import lamp
from . import material
from . import view2d
from . import mball
from . import mesh
from . import lattice
from . import mask
from . import ed
from . import marker
from . import script
from . import texture
from . import export_anim

GenericType = typing.TypeVar("GenericType")


class BPyOps:
    pass


class BPyOpsSubMod:
    pass


class BPyOpsSubModOp:
    def get_instance(self):
        ''' 

        '''
        pass

    def get_rna(self):
        ''' 

        '''
        pass

    def idname(self):
        ''' 

        '''
        pass

    def idname_py(self):
        ''' 

        '''
        pass

    def poll(self, args):
        ''' 

        '''
        pass
