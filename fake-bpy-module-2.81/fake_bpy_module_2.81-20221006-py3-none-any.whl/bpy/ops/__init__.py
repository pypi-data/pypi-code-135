import sys
import typing
from . import paintcurve
from . import collection
from . import palette
from . import export_anim
from . import buttons
from . import action
from . import info
from . import dpaint
from . import gpencil
from . import font
from . import lattice
from . import mesh
from . import cycles
from . import import_curve
from . import clip
from . import surface
from . import sound
from . import import_anim
from . import brush
from . import sculpt
from . import ui
from . import graph
from . import scene
from . import file
from . import workspace
from . import import_mesh
from . import curve
from . import pose
from . import paint
from . import world
from . import console
from . import mball
from . import wm
from . import script
from . import camera
from . import view2d
from . import ptcache
from . import gizmogroup
from . import export_scene
from . import constraint
from . import armature
from . import cachefile
from . import node
from . import import_scene
from . import boid
from . import marker
from . import view3d
from . import sequencer
from . import text
from . import fluid
from . import preferences
from . import texture
from . import uv
from . import transform
from . import outliner
from . import mask
from . import material
from . import ed
from . import render
from . import safe_areas
from . import cloth
from . import particle
from . import rigidbody
from . import poselib
from . import nla
from . import anim
from . import object
from . import export_mesh
from . import screen
from . import image

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
