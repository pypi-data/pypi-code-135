import sys
import typing
import bpy.types
import bpy.ops.transform
import mathutils

GenericType = typing.TypeVar("GenericType")


def change_effect_input(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        swap: typing.Union[str, int] = 'A_B'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param swap: Swap, The effect inputs to swap
    :type swap: typing.Union[str, int]
    '''

    pass


def change_effect_type(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       type: typing.Union[str, int] = 'CROSS'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Sequencer effect type * CROSS Crossfade, Crossfade effect strip type. * ADD Add, Add effect strip type. * SUBTRACT Subtract, Subtract effect strip type. * ALPHA_OVER Alpha Over, Alpha Over effect strip type. * ALPHA_UNDER Alpha Under, Alpha Under effect strip type. * GAMMA_CROSS Gamma Cross, Gamma Cross effect strip type. * MULTIPLY Multiply, Multiply effect strip type. * OVER_DROP Alpha Over Drop, Alpha Over Drop effect strip type. * WIPE Wipe, Wipe effect strip type. * GLOW Glow, Glow effect strip type. * TRANSFORM Transform, Transform effect strip type. * COLOR Color, Color effect strip type. * SPEED Speed, Color effect strip type. * MULTICAM Multicam Selector. * ADJUSTMENT Adjustment Layer. * GAUSSIAN_BLUR Gaussian Blur. * TEXT Text.
    :type type: typing.Union[str, int]
    '''

    pass


def change_path(
        override_context: typing.Union[typing.
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
        filter_image: bool = False,
        filter_movie: bool = False,
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
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
        use_placeholders: bool = False):
    ''' Undocumented

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
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    :type use_placeholders: bool
    '''

    pass


def copy(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def crossfade_sounds(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Do cross-fading volume animation of two selected sound strips :file: startup/bl_operators/sequencer.py\:41 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/sequencer.py$41> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def cut(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        frame: int = 0,
        type: typing.Union[str, int] = 'SOFT',
        side: typing.Union[str, int] = 'BOTH'):
    ''' Cut the selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame, Frame where selected strips will be cut
    :type frame: int
    :param type: Type, The type of cut operation to perform on strips
    :type type: typing.Union[str, int]
    :param side: Side, The side that remains selected after cutting
    :type side: typing.Union[str, int]
    '''

    pass


def cut_multicam(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 camera: int = 1):
    ''' Cut multi-cam strip and select camera

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param camera: Camera
    :type camera: int
    '''

    pass


def deinterlace_selected_movies(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Deinterlace all selected movie sources :file: startup/bl_operators/sequencer.py\:131 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/sequencer.py$131> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Erase selected strips from the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              mode: typing.Union[str, int] = 'TRANSLATION'):
    ''' Duplicate the selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def duplicate_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        SEQUENCER_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_seq_slide: 'bpy.ops.transform.seq_slide' = None):
    ''' Duplicate selected strips and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: 'bpy.ops.transform.seq_slide'
    '''

    pass


def effect_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        frame_start: int = 0,
        frame_end: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        type: typing.Union[str, int] = 'CROSS',
        color: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an effect to the sequencer, most are applied on top of existing strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param type: Type, Sequencer effect type * CROSS Crossfade, Crossfade effect strip type. * ADD Add, Add effect strip type. * SUBTRACT Subtract, Subtract effect strip type. * ALPHA_OVER Alpha Over, Alpha Over effect strip type. * ALPHA_UNDER Alpha Under, Alpha Under effect strip type. * GAMMA_CROSS Gamma Cross, Gamma Cross effect strip type. * MULTIPLY Multiply, Multiply effect strip type. * OVER_DROP Alpha Over Drop, Alpha Over Drop effect strip type. * WIPE Wipe, Wipe effect strip type. * GLOW Glow, Glow effect strip type. * TRANSFORM Transform, Transform effect strip type. * COLOR Color, Color effect strip type. * SPEED Speed, Color effect strip type. * MULTICAM Multicam Selector. * ADJUSTMENT Adjustment Layer. * GAUSSIAN_BLUR Gaussian Blur. * TEXT Text.
    :type type: typing.Union[str, int]
    :param color: Color, Initialize the strip with this color (only used when type='COLOR')
    :type color: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def enable_proxies(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   proxy_25: bool = False,
                   proxy_50: bool = False,
                   proxy_75: bool = False,
                   proxy_100: bool = False,
                   overwrite: bool = False):
    ''' Enable selected proxies on all selected Movie strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param proxy_25: 25%
    :type proxy_25: bool
    :param proxy_50: 50%
    :type proxy_50: bool
    :param proxy_75: 75%
    :type proxy_75: bool
    :param proxy_100: 100%
    :type proxy_100: bool
    :param overwrite: Overwrite
    :type overwrite: bool
    '''

    pass


def export_subtitles(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     filepath: str = "",
                     check_existing: bool = True,
                     filter_blender: bool = False,
                     filter_backup: bool = False,
                     filter_image: bool = False,
                     filter_movie: bool = False,
                     filter_python: bool = False,
                     filter_font: bool = False,
                     filter_sound: bool = False,
                     filter_text: bool = False,
                     filter_btx: bool = False,
                     filter_collada: bool = False,
                     filter_alembic: bool = False,
                     filter_folder: bool = True,
                     filter_blenlib: bool = False,
                     filemode: int = 8,
                     display_type: typing.Union[str, int] = 'DEFAULT',
                     sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA'):
    ''' Export .srt file containing text strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
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
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    '''

    pass


def gap_insert(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               frames: int = 10):
    ''' Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frames: Frames, Frames to insert after current strip
    :type frames: int
    '''

    pass


def gap_remove(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               all: bool = False):
    ''' Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All Gaps, Do all gaps to right of current frame
    :type all: bool
    '''

    pass


def image_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        directory: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = True,
        filter_movie: bool = False,
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
        frame_start: int = 0,
        frame_end: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        use_placeholders: bool = False):
    ''' Add an image or image sequence to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
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
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
    :type use_placeholders: bool
    '''

    pass


def images_separate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    length: int = 1):
    ''' On image sequence strips, it returns a strip for each image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param length: Length, Length of each frame
    :type length: int
    '''

    pass


def lock(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Lock the active strip so that it can't be transformed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def mask_strip_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   frame_start: int = 0,
                   channel: int = 1,
                   replace_sel: bool = True,
                   overlap: bool = False,
                   mask: typing.Union[str, int] = ''):
    ''' Add a mask strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param mask: Mask
    :type mask: typing.Union[str, int]
    '''

    pass


def meta_make(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Group selected strips into a metastrip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def meta_separate(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Put the contents of a metastrip back in the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def meta_toggle(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Toggle a metastrip (to edit enclosed strips)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def movie_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
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
        frame_start: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        sound: bool = True,
        use_framerate: bool = True):
    ''' Add a movie strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
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
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param sound: Sound, Load sound with the movie
    :type sound: bool
    :param use_framerate: Use Movie Framerate, Use framerate from the movie to keep sound and video in sync
    :type use_framerate: bool
    '''

    pass


def movieclip_strip_add(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        frame_start: int = 0,
                        channel: int = 1,
                        replace_sel: bool = True,
                        overlap: bool = False,
                        clip: typing.Union[str, int] = ''):
    ''' Add a movieclip strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param clip: Clip
    :type clip: typing.Union[str, int]
    '''

    pass


def mute(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         unselected: bool = False):
    ''' Mute (un)selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Mute unselected rather than selected strips
    :type unselected: bool
    '''

    pass


def offset_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Clear strip offsets from the start and end frames

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def paste(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None):
    ''' Undocumented

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


def reassign_inputs(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Reassign the inputs for the effect strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def rebuild_proxy(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Rebuild all selected proxies and timecode indices using the job system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def refresh_all(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Refresh the sequencer editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def reload(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           adjust_length: bool = False):
    ''' Reload strips in the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param adjust_length: Adjust Length, Adjust length of strips to their data length
    :type adjust_length: bool
    '''

    pass


def rendersize(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Set render size and aspect from active sequence

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def sample(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Use mouse to sample color in current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def scene_strip_add(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    frame_start: int = 0,
                    channel: int = 1,
                    replace_sel: bool = True,
                    overlap: bool = False,
                    scene: typing.Union[str, int] = ''):
    ''' Add a strip to the sequencer using a blender scene as a source

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param scene: Scene
    :type scene: typing.Union[str, int]
    '''

    pass


def select(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           extend: bool = False,
           linked_handle: bool = False,
           left_right: typing.Union[str, int] = 'NONE',
           linked_time: bool = False):
    ''' Select a strip (last selected becomes the "active strip")

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    :param linked_handle: Linked Handle, Select handles next to the active strip
    :type linked_handle: bool
    :param left_right: Left/Right, Select based on the current frame side the cursor is on * NONE None, Don't do left-right selection. * MOUSE Mouse, Use mouse position for selection. * LEFT Left, Select left. * RIGHT Right, Select right.
    :type left_right: typing.Union[str, int]
    :param linked_time: Linked Time, Select other strips at the same time
    :type linked_time: bool
    '''

    pass


def select_active_side(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       side: typing.Union[str, int] = 'BOTH'):
    ''' Select strips on the nominated side of the active strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param side: Side, The side of the handle that is selected
    :type side: typing.Union[str, int]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' Select or deselect all strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle, Toggle selection for all elements. * SELECT Select, Select all elements. * DESELECT Deselect, Deselect all elements. * INVERT Invert, Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_border(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  gesture_mode: int = 0,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  extend: bool = True):
    ''' Select strips using border selection

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
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'TYPE',
                   extend: bool = False,
                   use_active_channel: bool = False):
    ''' Select all strips grouped by various properties

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * TYPE Type, Shared strip type. * TYPE_BASIC Global Type, All strips of same basic type (Graphical or Sound). * TYPE_EFFECT Effect Type, Shared strip effect type (if active strip is not an effect one, select all non-effect strips). * DATA Data, Shared data (scene, image, sound, etc.). * EFFECT Effect, Shared effects. * EFFECT_LINK Effect/Linked, Other strips affected by the active one (sharing some time, and below or effect-assigned). * OVERLAP Overlap, Overlapping time.
    :type type: typing.Union[str, int]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one
    :type use_active_channel: bool
    '''

    pass


def select_handles(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   side: typing.Union[str, int] = 'BOTH'):
    ''' Select manipulator handles on the sides of the selected strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param side: Side, The side of the handle that is selected
    :type side: typing.Union[str, int]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Shrink the current selection of adjacent selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Select all strips adjacent to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       extend: bool = False):
    ''' Select a chain of linked strips nearest to the mouse pointer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Select more strips adjacent to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def slip(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         offset: int = 0):
    ''' Trim the contents of the active strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Offset, Offset to the data of the strip
    :type offset: int
    '''

    pass


def snap(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         frame: int = 0):
    ''' Frame where selected strips will be snapped

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame, Frame where selected strips will be snapped
    :type frame: int
    '''

    pass


def sound_strip_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = True,
        filter_text: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
        frame_start: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        cache: bool = False,
        mono: bool = False):
    ''' Add a sound strip to the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
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
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param frame_start: Start Frame, Start frame of the sequence strip
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
    :type overlap: bool
    :param cache: Cache, Cache the sound in memory
    :type cache: bool
    :param mono: Mono, Merge all the sound's channels into one
    :type mono: bool
    '''

    pass


def strip_jump(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               next: bool = True,
               center: bool = True):
    ''' Move frame to previous edit point

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param next: Next Strip
    :type next: bool
    :param center: Use strip center
    :type center: bool
    '''

    pass


def strip_modifier_add(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       type: typing.Union[str, int] = 'COLOR_BALANCE'):
    ''' Add a modifier to the strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def strip_modifier_copy(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        type: typing.Union[str, int] = 'REPLACE'):
    ''' Copy modifiers of the active strip to all selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * REPLACE Replace, Replace modifiers in destination. * APPEND Append, Append active modifiers to selected strips.
    :type type: typing.Union[str, int]
    '''

    pass


def strip_modifier_move(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        name: str = "Name",
                        direction: typing.Union[str, int] = 'UP'):
    ''' Move modifier up and down in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of modifier to remove
    :type name: str
    :param direction: Type * UP Up, Move modifier up in the stack. * DOWN Down, Move modifier down in the stack.
    :type direction: typing.Union[str, int]
    '''

    pass


def strip_modifier_remove(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          name: str = "Name"):
    ''' Remove a modifier from the strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of modifier to remove
    :type name: str
    '''

    pass


def swap(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         side: typing.Union[str, int] = 'RIGHT'):
    ''' Swap active strip with strip to the right or left

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param side: Side, Side of the strip to swap
    :type side: typing.Union[str, int]
    '''

    pass


def swap_data(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Swap 2 sequencer strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def swap_inputs(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Swap the first two inputs for the effect strip

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def unlock(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Unlock the active strip so that it can't be transformed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def unmute(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           unselected: bool = False):
    ''' Unmute (un)selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Unmute unselected rather than selected strips
    :type unselected: bool
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' View all the strips in the sequencer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_all_preview(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Zoom preview to fit in the area

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_frame(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Reset viewable area to show range around current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_ghost_border(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      gesture_mode: int = 0,
                      xmin: int = 0,
                      xmax: int = 0,
                      ymin: int = 0,
                      ymax: int = 0):
    ''' Set the boundaries of the border used for offset-view

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


def view_selected(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Zoom the sequencer on the selected strips

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_toggle(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Toggle between sequencer views (sequence, preview, both)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_zoom_ratio(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    ratio: float = 1.0):
    ''' Change zoom ratio of sequencer preview

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    :type ratio: float
    '''

    pass
