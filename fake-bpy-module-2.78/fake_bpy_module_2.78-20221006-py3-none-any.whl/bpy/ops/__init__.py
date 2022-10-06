import sys
import typing
from . import transform
from . import logic
from . import clip
from . import action
from . import anim
from . import nla
from . import object
from . import lattice
from . import cycles
from . import graph
from . import ptcache
from . import paintcurve
from . import font
from . import rigidbody
from . import curve
from . import export_anim
from . import node
from . import time
from . import scene
from . import armature
from . import palette
from . import render
from . import import_anim
from . import ui
from . import image
from . import sculpt
from . import mask
from . import sketch
from . import material
from . import export_scene
from . import mesh
from . import sequencer
from . import pose
from . import constraint
from . import ed
from . import marker
from . import cloth
from . import info
from . import safe_areas
from . import brush
from . import paint
from . import group
from . import poselib
from . import texture
from . import particle
from . import export_mesh
from . import view3d
from . import console
from . import buttons
from . import import_mesh
from . import outliner
from . import screen
from . import file
from . import cachefile
from . import sound
from . import world
from . import view2d
from . import import_scene
from . import dpaint
from . import wm
from . import fluid
from . import lamp
from . import text
from . import import_curve
from . import boid
from . import mball
from . import surface
from . import camera
from . import uv
from . import gpencil
from . import script

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
