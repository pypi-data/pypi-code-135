import sys
import typing
from . import dpaint
from . import render
from . import workspace
from . import info
from . import fluid
from . import texture
from . import outliner
from . import text
from . import collection
from . import import_scene
from . import import_anim
from . import palette
from . import import_mesh
from . import node
from . import material
from . import screen
from . import paintcurve
from . import cycles
from . import mask
from . import font
from . import file
from . import view2d
from . import curve
from . import script
from . import sound
from . import brush
from . import constraint
from . import gizmogroup
from . import camera
from . import ui
from . import action
from . import export_anim
from . import world
from . import marker
from . import cloth
from . import image
from . import lattice
from . import wm
from . import console
from . import buttons
from . import mball
from . import surface
from . import ptcache
from . import safe_areas
from . import ed
from . import transform
from . import paint
from . import gpencil
from . import anim
from . import view3d
from . import nla
from . import pose
from . import preferences
from . import graph
from . import scene
from . import import_curve
from . import boid
from . import armature
from . import sequencer
from . import poselib
from . import particle
from . import sculpt
from . import mesh
from . import clip
from . import uv
from . import object
from . import export_scene
from . import rigidbody
from . import cachefile
from . import export_mesh

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
