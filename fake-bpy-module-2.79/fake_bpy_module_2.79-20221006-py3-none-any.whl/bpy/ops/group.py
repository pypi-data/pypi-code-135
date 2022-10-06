import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def create(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           name: str = "Group"):
    ''' Create an object group from selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the new group
    :type name: str
    '''

    pass


def objects_add_active(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       group: typing.Union[str, int] = ''):
    ''' Add the object to an object group that contains the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group: Group, The group to add other selected objects to
    :type group: typing.Union[str, int]
    '''

    pass


def objects_remove(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   group: typing.Union[str, int] = ''):
    ''' Remove selected objects from a group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group: Group, The group to remove this object from
    :type group: typing.Union[str, int]
    '''

    pass


def objects_remove_active(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          group: typing.Union[str, int] = ''):
    ''' Remove the object from an object group that contains the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group: Group, The group to remove other selected objects from
    :type group: typing.Union[str, int]
    '''

    pass


def objects_remove_all(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Remove selected objects from all groups

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
