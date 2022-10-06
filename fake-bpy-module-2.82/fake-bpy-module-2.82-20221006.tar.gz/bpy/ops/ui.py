import sys
import typing
import bpy.types
import mathutils

GenericType = typing.TypeVar("GenericType")


def assign_default_button(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Set this property's current value as the new default

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def button_execute(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   skip_depressed: bool = False):
    ''' Presses active button

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param skip_depressed: Skip Depressed
    :type skip_depressed: bool
    '''

    pass


def button_string_clear(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Unsets the text of the active button

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def copy_as_driver_button(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Create a new driver with this property as input, and copy it to the clipboard. Use Paste Driver to add it to the target property, or Paste Driver Variables to extend an existing driver

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def copy_data_path_button(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          full_path: bool = False):
    ''' Copy the RNA data path for this property to the clipboard

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param full_path: full_path, Copy full data path
    :type full_path: bool
    '''

    pass


def copy_python_command_button(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Copy the Python command matching this button

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def copy_to_selected_button(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            all: bool = True):
    ''' Copy property from this object to selected objects or bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All, Copy to selected all elements of the array
    :type all: bool
    '''

    pass


def drop_color(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        color: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        gamma: bool = False):
    ''' Drop colors to buttons

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param color: Color, Source color
    :type color: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param gamma: Gamma Corrected, The source color is gamma corrected
    :type gamma: bool
    '''

    pass


def editsource(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Edit UI source code of the active button

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def edittranslation_init(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Edit i18n in current language for the active button

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def eyedropper_color(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     use_accumulate: bool = True):
    ''' Sample a color from the Blender window to store in a property

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_accumulate: Accumulate
    :type use_accumulate: bool
    '''

    pass


def eyedropper_colorramp(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Sample a color band

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def eyedropper_colorramp_point(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Point-sample a color band

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def eyedropper_depth(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Sample depth from the 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def eyedropper_driver(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      mapping_type: typing.Union[str, int] = 'SINGLE_MANY'):
    ''' Pick a property to use as a driver target

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mapping_type: Mapping Type, Method used to match target and driven properties * SINGLE_MANY All from Target, Drive all components of this property using the target picked. * DIRECT Single from Target, Drive this component of this property using the target picked. * MATCH Match Indices, Create drivers for each pair of corresponding elements. * NONE_ALL Manually Create Later, Create drivers for all properties without assigning any targets yet. * NONE_SINGLE Manually Create Later (Single), Create driver for this property only and without assigning any targets yet.
    :type mapping_type: typing.Union[str, int]
    '''

    pass


def eyedropper_gpencil_color(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Sample a color from the Blender Window and create Grease Pencil material

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def eyedropper_id(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Sample a data-block from the 3D View to store in a property

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def jump_to_target_button(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Switch to the target object or bone

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def override_remove_button(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           all: bool = True):
    ''' Remove an override operation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All, Reset to default values all elements of the array
    :type all: bool
    '''

    pass


def override_type_set_button(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             all: bool = True,
                             type: typing.Union[str, int] = 'REPLACE'):
    ''' Create an override operation, or set the type of an existing one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All, Reset to default values all elements of the array
    :type all: bool
    :param type: Type, Type of override operation * NOOP NoOp, 'No-Operation', place holder preventing automatic override to ever affect the property. * REPLACE Replace, Completely replace value from linked data by local one. * DIFFERENCE Difference, Store difference to linked data value. * FACTOR Factor, Store factor to linked data value (useful e.g. for scale).
    :type type: typing.Union[str, int]
    '''

    pass


def reloadtranslation(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Force a full reload of UI translation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def reset_default_button(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         all: bool = True):
    ''' Reset this property's value to its default value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All, Reset to default values all elements of the array
    :type all: bool
    '''

    pass


def unset_property_button(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Clear the property and use default or generated value in operators

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
