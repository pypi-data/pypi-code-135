import sys
import typing
from . import brush
from . import lattice
from . import surface
from . import buttons
from . import outliner
from . import collection
from . import sound
from . import rigidbody
from . import palette
from . import transform
from . import anim
from . import boid
from . import import_scene
from . import cachefile
from . import cloth
from . import poselib
from . import export_anim
from . import armature
from . import camera
from . import ptcache
from . import material
from . import sculpt
from . import constraint
from . import safe_areas
from . import object
from . import dpaint
from . import curve
from . import render
from . import ed
from . import wm
from . import world
from . import info
from . import view2d
from . import screen
from . import paintcurve
from . import ui
from . import texture
from . import gpencil
from . import sequencer
from . import text
from . import export_scene
from . import node
from . import export_mesh
from . import particle
from . import view3d
from . import action
from . import marker
from . import clip
from . import import_anim
from . import font
from . import paint
from . import gizmogroup
from . import uv
from . import scene
from . import script
from . import workspace
from . import import_mesh
from . import cycles
from . import graph
from . import image
from . import pose
from . import fluid
from . import import_curve
from . import console
from . import nla
from . import mask
from . import mesh
from . import mball
from . import preferences
from . import file

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
