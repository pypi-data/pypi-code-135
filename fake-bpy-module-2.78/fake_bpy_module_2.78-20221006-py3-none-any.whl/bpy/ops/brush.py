import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def active_index_set(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mode: str = "",
                     index: int = 0):
    ''' Set active sculpt/paint brush from it's number

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, Paint mode to set brush for
    :type mode: str
    :param index: Number, Brush number
    :type index: int
    '''

    pass


def add(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Add brush by mode type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def curve_preset(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 shape: typing.Union[str, int] = 'SMOOTH'):
    ''' Set brush shape

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shape: Mode
    :type shape: typing.Union[str, int]
    '''

    pass


def reset(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None):
    ''' Return brush to defaults based on current tool

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def scale_size(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               scalar: float = 1.0):
    ''' Change brush size by a scalar

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param scalar: Scalar, Factor to scale brush size by
    :type scalar: float
    '''

    pass


def stencil_control(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    mode: typing.Union[str, int] = 'TRANSLATION',
                    texmode: typing.Union[str, int] = 'PRIMARY'):
    ''' Control the stencil brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Tool
    :type mode: typing.Union[str, int]
    :param texmode: Tool
    :type texmode: typing.Union[str, int]
    '''

    pass


def stencil_fit_image_aspect(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             use_repeat: bool = True,
                             use_scale: bool = True,
                             mask: bool = False):
    ''' When using an image texture, adjust the stencil size to fit the image aspect ratio

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_repeat: Use Repeat, Use repeat mapping values
    :type use_repeat: bool
    :param use_scale: Use Scale, Use texture scale values
    :type use_scale: bool
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool
    '''

    pass


def stencil_reset_transform(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            mask: bool = False):
    ''' Reset the stencil transformation to the default

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool
    '''

    pass


def uv_sculpt_tool_set(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       tool: typing.Union[str, int] = 'PINCH'):
    ''' Set the UV sculpt tool

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param tool: Tool * PINCH Pinch, Pinch UVs. * RELAX Relax, Relax UVs. * GRAB Grab, Grab UVs.
    :type tool: typing.Union[str, int]
    '''

    pass
