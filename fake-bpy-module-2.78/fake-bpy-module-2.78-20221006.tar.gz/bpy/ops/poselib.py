import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def action_sanitize(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Make action suitable for use as a Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def apply_pose(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               pose_index: int = -1):
    ''' Apply specified Pose Library pose to the rig

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def browse_interactive(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       pose_index: int = -1):
    ''' Interactively browse poses in 3D-View

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def new(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Add New Pose Library to active Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def pose_add(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             frame: int = 1,
             name: str = "Pose"):
    ''' Add the current Pose to the active Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame, Frame to store pose on
    :type frame: int
    :param name: Pose Name, Name of newly added Pose
    :type name: str
    '''

    pass


def pose_remove(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                pose: typing.Union[str, int] = ''):
    ''' Remove nth pose from the active Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose: Pose, The pose to remove
    :type pose: typing.Union[str, int]
    '''

    pass


def pose_rename(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                name: str = "RenamedPose",
                pose: typing.Union[str, int] = ''):
    ''' Rename specified pose from the active Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: New Pose Name, New name for pose
    :type name: str
    :param pose: Pose, The pose to rename
    :type pose: typing.Union[str, int]
    '''

    pass


def unlink(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Remove Pose Library from active Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
