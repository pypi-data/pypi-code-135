import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def add_aov(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None):
    ''' Add an AOV pass :file: addons/cycles/operators.py\:52 <https://developer.blender.org/diffusion/BA/addons/cycles/operators.py$52> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def denoise_animation(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      input_filepath: str = "",
                      output_filepath: str = ""):
    ''' Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param input_filepath: Input Filepath, File path for image to denoise. If not specified, uses the render file path and frame range from the scene
    :type input_filepath: str
    :param output_filepath: Output Filepath, If not specified, renders will be denoised in-place
    :type output_filepath: str
    '''

    pass


def merge_images(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 input_filepath1: str = "",
                 input_filepath2: str = "",
                 output_filepath: str = ""):
    ''' Combine OpenEXR multilayer images rendered with different sample ranges into one image with reduced noise

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param input_filepath1: Input Filepath, File path for image to merge
    :type input_filepath1: str
    :param input_filepath2: Input Filepath, File path for image to merge
    :type input_filepath2: str
    :param output_filepath: Output Filepath, File path for merged image
    :type output_filepath: str
    '''

    pass


def remove_aov(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Remove an AOV pass :file: addons/cycles/operators.py\:67 <https://developer.blender.org/diffusion/BA/addons/cycles/operators.py$67> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def use_shading_nodes(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Enable nodes on a material, world or light :file: addons/cycles/operators.py\:36 <https://developer.blender.org/diffusion/BA/addons/cycles/operators.py$36> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
