import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def ndof(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Use a 3D mouse device to pan/zoom the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def pan(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        deltax: int = 0,
        deltay: int = 0):
    ''' Pan the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    '''

    pass


def reset(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None):
    ''' Reset the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def scroll_down(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                deltax: int = 0,
                deltay: int = 0,
                page: bool = False):
    ''' Scroll the view down

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    :param page: Page, Scroll down one page
    :type page: bool
    '''

    pass


def scroll_left(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                deltax: int = 0,
                deltay: int = 0):
    ''' Scroll the view left

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    '''

    pass


def scroll_right(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 deltax: int = 0,
                 deltay: int = 0):
    ''' Scroll the view right

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    '''

    pass


def scroll_up(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              deltax: int = 0,
              deltay: int = 0,
              page: bool = False):
    ''' Scroll the view up

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    :param page: Page, Scroll up one page
    :type page: bool
    '''

    pass


def scroller_activate(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Scroll view by mouse click and drag

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def smoothview(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               gesture_mode: int = 0,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0):
    ''' Undocumented

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


def zoom(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         deltax: float = 0.0,
         deltay: float = 0.0):
    ''' Zoom in/out the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: float
    :param deltay: Delta Y
    :type deltay: float
    '''

    pass


def zoom_border(override_context: typing.
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


def zoom_in(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            zoomfacx: float = 0.0,
            zoomfacy: float = 0.0):
    ''' Zoom in the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: float
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: float
    '''

    pass


def zoom_out(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             zoomfacx: float = 0.0,
             zoomfacy: float = 0.0):
    ''' Zoom out the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: float
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: float
    '''

    pass
