import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def brush_stroke(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 stroke: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorStrokeElement'] = None,
                 mode: typing.Union[str, int] = 'NORMAL'):
    ''' Sculpt curves using a brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular -- Apply brush normally. * INVERT Invert -- Invert action of brush for duration of stroke. * SMOOTH Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[str, int]
    '''

    pass
