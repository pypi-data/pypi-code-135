import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def envmap_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Discard the environment map and free it from memory

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def envmap_clear_all(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Discard all environment maps in the .blend file and free them from memory

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def envmap_save(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        layout: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float, float, float, float, float, float,
                    float, float, float, float], 'mathutils.Vector'] = (
                        0.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.0,
                        1.0),
        filepath: str = "",
        check_existing: bool = True,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = True,
        filter_movie: bool = True,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        show_multiview: bool = False,
        use_multiview: bool = False,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA'):
    ''' Save the current generated Environment map to an image file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param layout: File layout, Flat array describing the X,Y position of each cube face in the output image, where 1 is the size of a face - order is [+Z -Z +Y -X -Y +X] (use -1 to skip a face)
    :type layout: typing.Union[typing.List[float], typing.Tuple[float, float, float, float, float, float, float, float, float, float, float, float], 'mathutils.Vector']
    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param show_multiview: Enable Multi-View
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
    :type use_multiview: bool
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    '''

    pass


def new(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Add a new texture

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def slot_copy(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Copy the material texture settings and nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def slot_move(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              type: typing.Union[str, int] = 'UP'):
    ''' Move texture slots up and down

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def slot_paste(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Copy the texture settings and nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
