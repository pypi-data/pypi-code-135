import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def change_frame(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 frame: int = 0):
    ''' Interactively change the current frame number

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame
    :type frame: int
    '''

    pass


def clear_render_border(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Clear the boundaries of the border render and disable border render

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def curves_point_set(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     point: typing.Union[str, int] = 'BLACK_POINT'):
    ''' Set black point or white point for curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param point: Point, Set black point or white point for curves
    :type point: typing.Union[str, int]
    '''

    pass


def cycle_render_slot(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      reverse: bool = False):
    ''' Cycle through all non-void render slots

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param reverse: Cycle in Reverse
    :type reverse: bool
    '''

    pass


def external_edit(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  filepath: str = ""):
    ''' Edit image in an external application

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: filepath
    :type filepath: str
    '''

    pass


def invert(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           invert_r: bool = False,
           invert_g: bool = False,
           invert_b: bool = False,
           invert_a: bool = False):
    ''' Invert image's channels

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param invert_r: Red, Invert Red Channel
    :type invert_r: bool
    :param invert_g: Green, Invert Green Channel
    :type invert_g: bool
    :param invert_b: Blue, Invert Blue Channel
    :type invert_b: bool
    :param invert_a: Alpha, Invert Alpha Channel
    :type invert_a: bool
    '''

    pass


def match_movie_length(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Set image's user's length to the one of this video

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def new(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "Untitled",
        width: int = 1024,
        height: int = 1024,
        color: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float, float], 'mathutils.Vector'] = (0.0,
                                                                        0.0,
                                                                        0.0,
                                                                        1.0),
        alpha: bool = True,
        generated_type: typing.Union[str, int] = 'BLANK',
        float: bool = False,
        gen_context: typing.Union[str, int] = 'NONE',
        use_stereo_3d: bool = False):
    ''' Create a new image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Image data-block name
    :type name: str
    :param width: Width, Image width
    :type width: int
    :param height: Height, Image height
    :type height: int
    :param color: Color, Default fill color
    :type color: typing.Union[typing.List[float], typing.Tuple[float, float, float, float], 'mathutils.Vector']
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing * BLANK Blank, Generate a blank image. * UV_GRID UV Grid, Generated grid to test UV mappings. * COLOR_GRID Color Grid, Generated improved UV grid to test UV mappings.
    :type generated_type: typing.Union[str, int]
    :param float: 32 bit Float, Create image with 32 bit floating point bit depth
    :type float: bool
    :param gen_context: Gen Context, Generation context
    :type gen_context: typing.Union[str, int]
    :param use_stereo_3d: Stereo 3D, Create an image with left and right views
    :type use_stereo_3d: bool
    '''

    pass


def open(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         filepath: str = "",
         directory: str = "",
         files: bpy.types.
         bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
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
         relative_path: bool = True,
         show_multiview: bool = False,
         use_multiview: bool = False,
         display_type: typing.Union[str, int] = 'DEFAULT',
         sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
         use_sequence_detection: bool = True):
    ''' Open image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
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
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param show_multiview: Enable Multi-View
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
    :type use_multiview: bool
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names)
    :type use_sequence_detection: bool
    '''

    pass


def pack(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         as_png: bool = False):
    ''' Pack an image as embedded data into the .blend file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param as_png: Pack As PNG, Pack image as lossless PNG
    :type as_png: bool
    '''

    pass


def project_apply(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Project edited image back onto the object :file: startup/bl_operators/image.py\:230 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/image.py$230> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def project_edit(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Edit a snapshot of the view-port in an external image editor :file: startup/bl_operators/image.py\:159 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/image.py$159> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def properties(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Toggle the properties region visibility

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def read_renderlayers(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Read all the current scene's render layers from cache, as needed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def reload(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Reload current image from disk

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def render_border(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0):
    ''' Set the boundaries of the border render and enable border render

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    '''

    pass


def replace(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            filepath: str = "",
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
            relative_path: bool = True,
            show_multiview: bool = False,
            use_multiview: bool = False,
            display_type: typing.Union[str, int] = 'DEFAULT',
            sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA'):
    ''' Replace current image by another one from disk

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
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
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
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


def sample(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Use mouse to sample a color in current image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def sample_line(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                xstart: int = 0,
                xend: int = 0,
                ystart: int = 0,
                yend: int = 0,
                cursor: int = 1002):
    ''' Sample a line and show it in Scope panels

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xstart: X Start
    :type xstart: int
    :param xend: X End
    :type xend: int
    :param ystart: Y Start
    :type ystart: int
    :param yend: Y End
    :type yend: int
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int
    '''

    pass


def save(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Save the image with current name and settings

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def save_as(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            save_as_render: bool = False,
            copy: bool = False,
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
            relative_path: bool = True,
            show_multiview: bool = False,
            use_multiview: bool = False,
            display_type: typing.Union[str, int] = 'DEFAULT',
            sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA'):
    ''' Save the image with another name and/or settings

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param save_as_render: Save As Render, Apply render part of display transform when saving byte image
    :type save_as_render: bool
    :param copy: Copy, Create a new image file without modifying the current image in blender
    :type copy: bool
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
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
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


def save_dirty(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Save all modified textures :file: startup/bl_operators/image.py\:124 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/image.py$124> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def save_sequence(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Save a sequence of images

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def toolshelf(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Toggles tool shelf display

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def unpack(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           method: typing.Union[str, int] = 'USE_LOCAL',
           id: str = ""):
    ''' Save an image packed in the .blend file to disk

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param method: Method, How to unpack
    :type method: typing.Union[str, int]
    :param id: Image Name, Image data-block name to unpack
    :type id: str
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             fit_view: bool = False):
    ''' View the entire image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param fit_view: Fit View, Fit frame to the viewport
    :type fit_view: bool
    '''

    pass


def view_ndof(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Use a 3D mouse device to pan/zoom the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_pan(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        offset: typing.Union[typing.List[float], typing.
                             Tuple[float, float], 'mathutils.Vector'] = (0.0,
                                                                         0.0)):
    ''' Pan the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Offset, Offset in floating point units, 1.0 is the width and height of the image
    :type offset: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    '''

    pass


def view_selected(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' View all selected UVs

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_zoom(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              factor: float = 0.0):
    ''' Zoom in/out the image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
    :type factor: float
    '''

    pass


def view_zoom_border(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     gesture_mode: int = 0,
                     xmin: int = 0,
                     xmax: int = 0,
                     ymin: int = 0,
                     ymax: int = 0):
    ''' Zoom in the view to the nearest item contained in the border

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param gesture_mode: Gesture Mode
    :type gesture_mode: int
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    '''

    pass


def view_zoom_in(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        location: typing.Union[typing.List[float], typing.
                               Tuple[float, float], 'mathutils.Vector'] = (
                                   0.0, 0.0)):
    ''' Zoom in the image (centered around 2D cursor)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param location: Location, Cursor location in screen coordinates
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    '''

    pass


def view_zoom_out(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        location: typing.Union[typing.List[float], typing.
                               Tuple[float, float], 'mathutils.Vector'] = (
                                   0.0, 0.0)):
    ''' Zoom out the image (centered around 2D cursor)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param location: Location, Cursor location in screen coordinates
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    '''

    pass


def view_zoom_ratio(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    ratio: float = 0.0):
    ''' Set zoom ratio of the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    :type ratio: float
    '''

    pass
