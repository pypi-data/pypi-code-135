import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def addon_disable(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  module: str = ""):
    ''' Disable an add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param module: Module, Module name of the add-on to disable
    :type module: str
    '''

    pass


def addon_enable(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 module: str = ""):
    ''' Enable an add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param module: Module, Module name of the add-on to enable
    :type module: str
    '''

    pass


def addon_expand(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 module: str = ""):
    ''' Display information and preferences for this add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param module: Module, Module name of the add-on to expand
    :type module: str
    '''

    pass


def addon_install(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  overwrite: bool = True,
                  target: typing.Union[str, int] = 'DEFAULT',
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_python: bool = True,
                  filter_glob: str = "*.py;*.zip"):
    ''' Install an add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param overwrite: Overwrite, Remove existing add-ons with the same ID
    :type overwrite: bool
    :param target: Target Path
    :type target: typing.Union[str, int]
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_python: Filter python
    :type filter_python: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    '''

    pass


def addon_refresh(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Scan add-on directories for new modules :file: startup/bl_operators/userpref.py\:569 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/userpref.py$569> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def addon_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 module: str = ""):
    ''' Delete the add-on from the file system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param module: Module, Module name of the add-on to remove
    :type module: str
    '''

    pass


def addon_show(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               module: str = ""):
    ''' Show add-on preferences

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param module: Module, Module name of the add-on to expand
    :type module: str
    '''

    pass


def app_template_install(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         overwrite: bool = True,
                         filepath: str = "",
                         filter_folder: bool = True,
                         filter_glob: str = "*.zip"):
    ''' Install an application-template

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param overwrite: Overwrite, Remove existing template with the same ID
    :type overwrite: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    '''

    pass


def copy_prev(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Copy settings from previous version :file: startup/bl_operators/userpref.py\:152 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/userpref.py$152> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def keyconfig_activate(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       filepath: str = ""):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: filepath
    :type filepath: str
    '''

    pass


def keyconfig_export(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     all: bool = False,
                     filepath: str = "keymap.py",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True):
    ''' Export key configuration to a python script

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All Keymaps, Write all keymaps (not just user modified)
    :type all: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_text: Filter text
    :type filter_text: bool
    :param filter_python: Filter python
    :type filter_python: bool
    '''

    pass


def keyconfig_import(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     filepath: str = "keymap.py",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True,
                     keep_original: bool = True):
    ''' Import key configuration from a python script

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_text: Filter text
    :type filter_text: bool
    :param filter_python: Filter python
    :type filter_python: bool
    :param keep_original: Keep original, Keep original file after copying to configuration folder
    :type keep_original: bool
    '''

    pass


def keyconfig_remove(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Remove key config :file: startup/bl_operators/userpref.py\:417 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/userpref.py$417> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def keyconfig_test(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Test key-config for conflicts :file: startup/bl_operators/userpref.py\:176 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/userpref.py$176> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def keyitem_add(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Add key map item :file: startup/bl_operators/userpref.py\:365 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/userpref.py$365> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def keyitem_remove(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   item_id: int = 0):
    ''' Remove key map item

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: int
    '''

    pass


def keyitem_restore(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    item_id: int = 0):
    ''' Restore key map item

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: int
    '''

    pass


def keymap_restore(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   all: bool = False):
    ''' Restore key map(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All Keymaps, Restore all keymaps to default
    :type all: bool
    '''

    pass


def reset_default_theme(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Reset to the default theme colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def studiolight_copy_settings(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None,
                              *,
                              index: int = 0):
    ''' Copy Studio Light settings to the Studio light editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param index: index
    :type index: int
    '''

    pass


def studiolight_install(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        directory: str = "",
        filter_folder: bool = True,
        filter_glob: str = "*.png;*.jpg;*.hdr;*.exr",
        type: typing.Union[str, int] = 'MATCAP'):
    ''' Install a user defined studio light

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param files: File Path
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param directory: directory
    :type directory: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param type: type
    :type type: typing.Union[str, int]
    '''

    pass


def studiolight_new(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    filename: str = "StudioLight"):
    ''' Save custom studio light from the studio light editor settings

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filename: Name
    :type filename: str
    '''

    pass


def studiolight_show(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Show light preferences :file: startup/bl_operators/userpref.py\:1123 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/userpref.py$1123> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def studiolight_uninstall(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          index: int = 0):
    ''' Delete Studio Light

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param index: index
    :type index: int
    '''

    pass


def theme_install(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  overwrite: bool = True,
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_glob: str = "*.xml"):
    ''' Load and apply a Blender XML theme file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param overwrite: Overwrite, Remove existing theme file if exists
    :type overwrite: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    '''

    pass
