import sys
import typing
from . import gpencil
from . import workspace
from . import script
from . import import_mesh
from . import safe_areas
from . import boid
from . import text
from . import buttons
from . import info
from . import armature
from . import palette
from . import surface
from . import object
from . import brush
from . import particle
from . import preferences
from . import marker
from . import cycles
from . import scene
from . import file
from . import outliner
from . import camera
from . import rigidbody
from . import curve
from . import sculpt
from . import import_anim
from . import view3d
from . import clip
from . import transform
from . import export_anim
from . import render
from . import paintcurve
from . import paint
from . import export_mesh
from . import export_scene
from . import mask
from . import mball
from . import material
from . import collection
from . import uv
from . import wm
from . import import_curve
from . import dpaint
from . import mesh
from . import constraint
from . import action
from . import font
from . import nla
from . import fluid
from . import world
from . import lattice
from . import ui
from . import gizmogroup
from . import console
from . import image
from . import cloth
from . import poselib
from . import view2d
from . import screen
from . import ed
from . import pose
from . import import_scene
from . import ptcache
from . import simulation
from . import cachefile
from . import anim
from . import sound
from . import node
from . import graph
from . import sequencer
from . import texture

GenericType = typing.TypeVar("GenericType")


class BPyOps:
    pass


class BPyOpsSubMod:
    pass


class BPyOpsSubModOp:
    def get_rna_type(self):
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
