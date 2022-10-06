import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def actuator_add(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 type: typing.Union[str, int] = '',
                 name: str = "",
                 object: str = ""):
    ''' Add an actuator to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Type of actuator to add
    :type type: typing.Union[str, int]
    :param name: Name, Name of the Actuator to add
    :type name: str
    :param object: Object, Name of the Object to add the Actuator to
    :type object: str
    '''

    pass


def actuator_move(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  actuator: str = "",
                  object: str = "",
                  direction: typing.Union[str, int] = 'UP'):
    ''' Move Actuator

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param actuator: Actuator, Name of the actuator to edit
    :type actuator: str
    :param object: Object, Name of the object the actuator belongs to
    :type object: str
    :param direction: Direction, Move Up or Down
    :type direction: typing.Union[str, int]
    '''

    pass


def actuator_remove(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    actuator: str = "",
                    object: str = ""):
    ''' Remove an actuator from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param actuator: Actuator, Name of the actuator to edit
    :type actuator: str
    :param object: Object, Name of the object the actuator belongs to
    :type object: str
    '''

    pass


def controller_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'LOGIC_AND',
                   name: str = "",
                   object: str = ""):
    ''' Add a controller to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Type of controller to add * LOGIC_AND And, Logic And. * LOGIC_OR Or, Logic Or. * LOGIC_NAND Nand, Logic Nand. * LOGIC_NOR Nor, Logic Nor. * LOGIC_XOR Xor, Logic Xor. * LOGIC_XNOR Xnor, Logic Xnor. * EXPRESSION Expression. * PYTHON Python.
    :type type: typing.Union[str, int]
    :param name: Name, Name of the Controller to add
    :type name: str
    :param object: Object, Name of the Object to add the Controller to
    :type object: str
    '''

    pass


def controller_move(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    controller: str = "",
                    object: str = "",
                    direction: typing.Union[str, int] = 'UP'):
    ''' Move Controller

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param controller: Controller, Name of the controller to edit
    :type controller: str
    :param object: Object, Name of the object the controller belongs to
    :type object: str
    :param direction: Direction, Move Up or Down
    :type direction: typing.Union[str, int]
    '''

    pass


def controller_remove(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      controller: str = "",
                      object: str = ""):
    ''' Remove a controller from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param controller: Controller, Name of the controller to edit
    :type controller: str
    :param object: Object, Name of the object the controller belongs to
    :type object: str
    '''

    pass


def links_cut(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              path: bpy.types.
              bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
              cursor: int = 9):
    ''' Remove logic brick connections

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param cursor: Cursor
    :type cursor: int
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


def sensor_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: typing.Union[str, int] = '',
               name: str = "",
               object: str = ""):
    ''' Add a sensor to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Type of sensor to add
    :type type: typing.Union[str, int]
    :param name: Name, Name of the Sensor to add
    :type name: str
    :param object: Object, Name of the Object to add the Sensor to
    :type object: str
    '''

    pass


def sensor_move(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                sensor: str = "",
                object: str = "",
                direction: typing.Union[str, int] = 'UP'):
    ''' Move Sensor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param sensor: Sensor, Name of the sensor to edit
    :type sensor: str
    :param object: Object, Name of the object the sensor belongs to
    :type object: str
    :param direction: Direction, Move Up or Down
    :type direction: typing.Union[str, int]
    '''

    pass


def sensor_remove(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  sensor: str = "",
                  object: str = ""):
    ''' Remove a sensor from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param sensor: Sensor, Name of the sensor to edit
    :type sensor: str
    :param object: Object, Name of the object the sensor belongs to
    :type object: str
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Resize view so you can see all logic bricks

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
