import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def attribute_add(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  name: str = "Attribute",
                  domain: typing.Union[str, int] = 'POINT',
                  data_type: typing.Union[str, int] = 'FLOAT'):
    ''' Add attribute to geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of new attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on * POINT Point -- Attribute on point. * EDGE Edge -- Attribute on mesh edge. * FACE Face -- Attribute on mesh faces. * CORNER Face Corner -- Attribute on mesh face corner. * CURVE Spline -- Attribute on spline. * INSTANCE Instance -- Attribute on instance.
    :type domain: typing.Union[str, int]
    :param data_type: Data Type, Type of data stored in attribute * FLOAT Float -- Floating-point value. * INT Integer -- 32-bit integer. * FLOAT_VECTOR Vector -- 3D vector with floating-point values. * FLOAT_COLOR Color -- RGBA color with floating-point values. * BYTE_COLOR Byte Color -- RGBA color with 8-bit values. * STRING String -- Text string. * BOOLEAN Boolean -- True or false. * FLOAT2 2D Vector -- 2D vector with floating-point values.
    :type data_type: typing.Union[str, int]
    '''

    pass


def attribute_convert(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      mode: typing.Union[str, int] = 'GENERIC',
                      domain: typing.Union[str, int] = 'POINT',
                      data_type: typing.Union[str, int] = 'FLOAT'):
    ''' Change how the attribute is stored

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param domain: Domain, Which geometry element to move the attribute to * POINT Point -- Attribute on point. * EDGE Edge -- Attribute on mesh edge. * FACE Face -- Attribute on mesh faces. * CORNER Face Corner -- Attribute on mesh face corner. * CURVE Spline -- Attribute on spline. * INSTANCE Instance -- Attribute on instance.
    :type domain: typing.Union[str, int]
    :param data_type: Data Type * FLOAT Float -- Floating-point value. * INT Integer -- 32-bit integer. * FLOAT_VECTOR Vector -- 3D vector with floating-point values. * FLOAT_COLOR Color -- RGBA color with floating-point values. * BYTE_COLOR Byte Color -- RGBA color with 8-bit values. * STRING String -- Text string. * BOOLEAN Boolean -- True or false. * FLOAT2 2D Vector -- 2D vector with floating-point values.
    :type data_type: typing.Union[str, int]
    '''

    pass


def attribute_remove(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Remove attribute from geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
