import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def bend(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         value: typing.Union[typing.List[float], typing.
                             Tuple[float], 'mathutils.Vector'] = (0.0),
         mirror: bool = False,
         proportional: typing.Union[str, int] = 'DISABLED',
         proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
         proportional_size: float = 1.0,
         snap: bool = False,
         snap_target: typing.Union[str, int] = 'CLOSEST',
         snap_point: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         snap_align: bool = False,
         snap_normal: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         gpencil_strokes: bool = False,
         release_confirm: bool = False,
         use_accurate: bool = False):
    ''' Bend selected items between the 3D cursor and the mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: typing.Union[typing.List[float], typing.Tuple[float], 'mathutils.Vector']
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def create_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       name: str = "",
                       use_view: bool = False,
                       use: bool = False,
                       overwrite: bool = False):
    ''' Create transformation orientation from selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the new custom orientation
    :type name: str
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
    :type use_view: bool
    :param use: Use after creation, Select orientation after its creation
    :type use: bool
    :param overwrite: Overwrite previous, Overwrite previously created orientation with same name
    :type overwrite: bool
    '''

    pass


def delete_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Delete transformation orientation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def edge_bevelweight(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Change the bevel weight of edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def edge_crease(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Change the crease of edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def edge_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        single_side: bool = False,
        use_even: bool = False,
        flipped: bool = False,
        use_clamp: bool = True,
        mirror: bool = False,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        correct_uv: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Slide an edge loop along a mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param single_side: Single Side
    :type single_side: bool
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: bool
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: bool
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def mirror(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           constraint_axis: typing.List[bool] = (False, False, False),
           constraint_orientation: typing.Union[str, int] = 'GLOBAL',
           proportional: typing.Union[str, int] = 'DISABLED',
           proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
           proportional_size: float = 1.0,
           gpencil_strokes: bool = False,
           release_confirm: bool = False,
           use_accurate: bool = False):
    ''' Mirror selected items around one or more axes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int]
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def push_pull(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Push/Pull selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Distance
    :type value: float
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def resize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                1.0, 1.0, 1.0),
        constraint_axis: typing.List[bool] = (False, False, False),
        constraint_orientation: typing.Union[str, int] = 'GLOBAL',
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        texture_space: bool = False,
        remove_on_cancel: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Scale (resize) selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Vector
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param texture_space: Edit Texture Space, Edit Object data texture space
    :type texture_space: bool
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def rotate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        axis: typing.Union[typing.List[float], typing.
                           Tuple[float, float, float], 'mathutils.Vector'] = (
                               0.0, 0.0, 0.0),
        constraint_axis: typing.List[bool] = (False, False, False),
        constraint_orientation: typing.Union[str, int] = 'GLOBAL',
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Rotate selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: float
    :param axis: Axis, The axis around which the transformation occurs
    :type axis: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def select_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       orientation: typing.Union[str, int] = 'GLOBAL'):
    ''' Select transformation orientation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param orientation: Orientation, Transformation orientation
    :type orientation: typing.Union[str, int]
    '''

    pass


def seq_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0),
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Slide a sequence strip in time

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Vector
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def shear(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          value: float = 0.0,
          mirror: bool = False,
          proportional: typing.Union[str, int] = 'DISABLED',
          proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
          proportional_size: float = 1.0,
          snap: bool = False,
          snap_target: typing.Union[str, int] = 'CLOSEST',
          snap_point: typing.
          Union[typing.List[float], typing.
                Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                   0.0),
          snap_align: bool = False,
          snap_normal: typing.
          Union[typing.List[float], typing.
                Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                   0.0),
          gpencil_strokes: bool = False,
          release_confirm: bool = False,
          use_accurate: bool = False):
    ''' Shear selected items along the horizontal screen axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Offset
    :type value: float
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def shrink_fatten(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        use_even_offset: bool = True,
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Shrink/fatten selected vertices along normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Offset
    :type value: float
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def skin_resize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                1.0, 1.0, 1.0),
        constraint_axis: typing.List[bool] = (False, False, False),
        constraint_orientation: typing.Union[str, int] = 'GLOBAL',
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Scale selected vertices' skin radii

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Vector
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def tilt(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         value: float = 0.0,
         mirror: bool = False,
         proportional: typing.Union[str, int] = 'DISABLED',
         proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
         proportional_size: float = 1.0,
         snap: bool = False,
         snap_target: typing.Union[str, int] = 'CLOSEST',
         snap_point: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         snap_align: bool = False,
         snap_normal: typing.
         Union[typing.List[float], typing.
               Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                  0.0),
         release_confirm: bool = False,
         use_accurate: bool = False):
    ''' Tilt selected control vertices of 3D curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: float
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def tosphere(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             value: float = 0.0,
             mirror: bool = False,
             proportional: typing.Union[str, int] = 'DISABLED',
             proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
             proportional_size: float = 1.0,
             snap: bool = False,
             snap_target: typing.Union[str, int] = 'CLOSEST',
             snap_point: typing.
             Union[typing.List[float], typing.
                   Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                      0.0),
             snap_align: bool = False,
             snap_normal: typing.
             Union[typing.List[float], typing.
                   Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                      0.0),
             gpencil_strokes: bool = False,
             release_confirm: bool = False,
             use_accurate: bool = False):
    ''' Move selected vertices outward in a spherical shape around mesh center

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def trackball(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0),
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Trackball style rotation of selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Angle
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def transform(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mode: typing.Union[str, int] = 'TRANSLATION',
        value: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0,
                                                                        0.0,
                                                                        0.0),
        axis: typing.Union[typing.List[float], typing.
                           Tuple[float, float, float], 'mathutils.Vector'] = (
                               0.0, 0.0, 0.0),
        constraint_axis: typing.List[bool] = (False, False, False),
        constraint_orientation: typing.Union[str, int] = 'GLOBAL',
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Transform selected items by mode type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param value: Values
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float, float], 'mathutils.Vector']
    :param axis: Axis, The axis around which the transformation occurs
    :type axis: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def translate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        constraint_axis: typing.List[bool] = (False, False, False),
        constraint_orientation: typing.Union[str, int] = 'GLOBAL',
        mirror: bool = False,
        proportional: typing.Union[str, int] = 'DISABLED',
        proportional_edit_falloff: typing.Union[str, int] = 'SMOOTH',
        proportional_size: float = 1.0,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        gpencil_strokes: bool = False,
        texture_space: bool = False,
        remove_on_cancel: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Translate (move) selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Vector
    :type value: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.List[bool]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int]
    :param mirror: Mirror Editing
    :type mirror: bool
    :param proportional: Proportional Editing * DISABLED Disable, Proportional Editing disabled. * ENABLED Enable, Proportional Editing enabled. * PROJECTED Projected (2D), Proportional Editing using screen space locations. * CONNECTED Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Union[str, int]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * SMOOTH Smooth, Smooth falloff. * SPHERE Sphere, Spherical falloff. * ROOT Root, Root falloff. * INVERSE_SQUARE Inverse Square, Inverse Square falloff. * SHARP Sharp, Sharp falloff. * LINEAR Linear, Linear falloff. * CONSTANT Constant, Constant falloff. * RANDOM Random, Random falloff.
    :type proportional_edit_falloff: typing.Union[str, int]
    :param proportional_size: Proportional Size
    :type proportional_size: float
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: bool
    :param texture_space: Edit Texture Space, Edit Object data texture space
    :type texture_space: bool
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def vert_slide(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        value: float = 0.0,
        use_even: bool = False,
        flipped: bool = False,
        use_clamp: bool = True,
        mirror: bool = False,
        snap: bool = False,
        snap_target: typing.Union[str, int] = 'CLOSEST',
        snap_point: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        snap_align: bool = False,
        snap_normal: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        correct_uv: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False):
    ''' Slide a vertex along a mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param value: Factor
    :type value: float
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: bool
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: bool
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: bool
    :param mirror: Mirror Editing
    :type mirror: bool
    :param snap: Use Snapping Options
    :type snap: bool
    :param snap_target: Target * CLOSEST Closest, Snap closest point onto target. * CENTER Center, Snap center onto target. * MEDIAN Median, Snap median onto target. * ACTIVE Active, Snap active onto target.
    :type snap_target: typing.Union[str, int]
    :param snap_point: Point
    :type snap_point: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param snap_align: Align with Point Normal
    :type snap_align: bool
    :param snap_normal: Normal
    :type snap_normal: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    '''

    pass


def vertex_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  offset: float = 0.1,
                  uniform: float = 0.0,
                  normal: float = 0.0,
                  seed: int = 0):
    ''' Randomize vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Amount, Distance to offset
    :type offset: float
    :param uniform: Uniform, Increase for uniform offset distance
    :type uniform: float
    :param normal: normal, Align offset direction to normals
    :type normal: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    '''

    pass


def vertex_warp(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        warp_angle: float = 6.28319,
        offset_angle: float = 0.0,
        min: float = -1,
        max: float = 1.0,
        viewmat: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float, float, float, float, float, float,
                    float, float, float, float, float, float, float, float],
              'mathutils.Vector'] = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        center: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0)):
    ''' Warp vertices around the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param warp_angle: Warp Angle, Amount to warp about the cursor
    :type warp_angle: float
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
    :type offset_angle: float
    :param min: Min
    :type min: float
    :param max: Max
    :type max: float
    :param viewmat: Matrix
    :type viewmat: typing.Union[typing.List[float], typing.Tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float], 'mathutils.Vector']
    :param center: Center
    :type center: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass
