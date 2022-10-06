import sys
import typing
from . import gizmogroup
from . import import_scene
from . import import_mesh
from . import material
from . import ptcache
from . import curve
from . import boid
from . import pose
from . import brush
from . import node
from . import surface
from . import nla
from . import font
from . import scene
from . import file
from . import gpencil
from . import mball
from . import anim
from . import import_anim
from . import texture
from . import export_scene
from . import transform
from . import graph
from . import console
from . import text
from . import collection
from . import info
from . import fluid
from . import ui
from . import poselib
from . import clip
from . import view3d
from . import mask
from . import screen
from . import world
from . import particle
from . import export_mesh
from . import wm
from . import marker
from . import sculpt
from . import ed
from . import cloth
from . import palette
from . import script
from . import outliner
from . import render
from . import object
from . import cachefile
from . import image
from . import uv
from . import safe_areas
from . import import_curve
from . import action
from . import workspace
from . import mesh
from . import lattice
from . import armature
from . import paint
from . import paintcurve
from . import export_anim
from . import dpaint
from . import sound
from . import preferences
from . import view2d
from . import buttons
from . import rigidbody
from . import sequencer
from . import constraint
from . import camera
from . import cycles

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
