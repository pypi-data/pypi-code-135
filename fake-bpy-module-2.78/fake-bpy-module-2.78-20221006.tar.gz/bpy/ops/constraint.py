import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def childof_clear_inverse(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          constraint: str = "",
                          owner: typing.Union[str, int] = 'OBJECT'):
    ''' Clear inverse correction for ChildOf constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def childof_set_inverse(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        constraint: str = "",
                        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Set inverse correction for ChildOf constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Remove constraint from constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def followpath_path_animate(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            constraint: str = "",
                            owner: typing.Union[str, int] = 'OBJECT',
                            frame_start: int = 1,
                            length: int = 100):
    ''' Add default animation for path used by constraint if it isn't animated already

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param frame_start: Start Frame, First frame of path animation
    :type frame_start: int
    :param length: Length, Number of frames that path animation should take
    :type length: int
    '''

    pass


def limitdistance_reset(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        constraint: str = "",
                        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Reset limiting distance for Limit Distance Constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def move_down(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              constraint: str = "",
              owner: typing.Union[str, int] = 'OBJECT'):
    ''' Move constraint down in constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def move_up(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            constraint: str = "",
            owner: typing.Union[str, int] = 'OBJECT'):
    ''' Move constraint up in constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def objectsolver_clear_inverse(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        constraint: str = "",
        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Clear inverse correction for ObjectSolver constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def objectsolver_set_inverse(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             constraint: str = "",
                             owner: typing.Union[str, int] = 'OBJECT'):
    ''' Set inverse correction for ObjectSolver constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def stretchto_reset(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    constraint: str = "",
                    owner: typing.Union[str, int] = 'OBJECT'):
    ''' Reset original length of bone for Stretch To Constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object, Edit a constraint on the active object. * BONE Bone, Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass
