"""threed
Adds some amount of 3D rendering support, including a 3D
Sprite class, a 3D Group class, and some utilities like
rotation and screen location functions.

Classes
-------
Sprite3d
    A class for making a 3D sprite. Contains position,
    velocity, and size information.
Cube
    An implementation of the Sprite3D class that renders
    the sprite as a cube.
Group3d
    A group that properly handles the drawing of 3D sprites

Functions
---------
cam_rotate(axy, axz)
    Rotates the camera as muchas is specified, in radians
cam_reset_rotation()
    Resets the camera's rotation to (axy=0,axz=0)
get_angles()
    Returns the current camera angle.
twofromthree(x,y,z)
    Takes a point in 3D space and returns its 2D equivalent,
    taking into account the camera's rotation.
rotate(x,y,rad)
    A simple 2D rotation that lets the previous functions work
toscreenpos(x,y,z=0)
    Using twofromthree, returns the screen position of a 3D point.
line3d(surf, col, pos1, pos2)
    Draws a line in 3D space on the given surface in the given
    color. Pretty much the 3D version of pygame.draw.line.
rect3d(surf, col, p1, p2, p3, p4)
    Draws a rectangle in 3D space on the given surface in the given
    color. Pretty much the 3D version of pygame.draw.rect.
cube3d(surf, cols, tfl, tfr, tbl, tbr, bfl, bfr, bbl, bbr, order=None)
    Draws a cube on the screen, taking as arguments each corner and
    the 3 colors to make each of the sides.
highest(objects)
    Takes a list of objects and returns the highest (lowest Z) of them.
cam_pos()
    Returns the camera's position in 3D space. Used for deciding rendering
    order (closest to camera gets drawn last)
cam_dist(x,y,z)
    Gives the distance from a point to the camera, using cam_pos.
spr3d_cam_dist(spr3d)
    An implementation of cam_dist that gets the position from a 3D sprite.
order_closelast(objects)
    Returns a copy of the objects list that is sorted so that the furthest
    object from the camera is first, the next furthest is second, and so on.
"""

# Couldn't name it 3d.py since you can't start a name with a number

import pygame
from pygame import draw
from pygame.sprite import Sprite
from .utils import add, clamp, CustomGroup
from . import sceneman
import math
from typing import Tuple, List, Callable, Any

# Camera angles by scene
scene_angles = {}

# Screen size (for determining center)
SIZE = pygame.display.get_surface().get_size()

# Takes a point (2D) and rotates it the specified number of radians
def rotate(x, y, rad):
    """Rotates a 2D point by a given angle in radians
    
    Parameters
    ----------
    x: int
        The x coordinate of the point
    y: int
        The y coordinate of the point
    rad: float
        The amount of radians to rotate the point by
    """
    ca = math.cos(rad)
    sa = math.sin(rad)
    tx = x*ca - y*sa
    ty = x*sa + y*ca
    return (tx, ty)

def cam_rotate(axy, axz):
    """Rotates the camera by the given angles in radians

    Parameters
    ----------
    axy: float
        The angle to rotate by in the xy plane
    axz: float
        The angle to rotate by in the xz plane
    """
    angles = (0,0)
    if sceneman.curr_scene in scene_angles:
        angles = scene_angles[sceneman.curr_scene]
    scene_angles[sceneman.curr_scene] = add(angles, (axy, axz))
    
def cam_reset_rotation():
    """Resets the camera's rotation to (axy=0, axz=0)"""
    scene_angles[sceneman.curr_scene] = (0,0)

def get_angles():
    """Returns the camera's current angle"""
    angles = (0,0)
    if sceneman.curr_scene in scene_angles:
        angles = scene_angles[sceneman.curr_scene]
    return angles

# Takes a 3d point, rotates it, and determines its 2d equivalent
def twofromthree(x,y,z):
    """Returns a 2D projection of a 3D point.
    
    Parameters
    ----------
    x: int
        The x coordinate of the point
    y: int
        The y coordinate of the point
    z: int
        The z coordinate of the point
    """
    axy, axz = get_angles()
    tx, tz = rotate(x, z, axz)
    tx, ty = rotate(tx, y, axy)
    return (ty-tx, -(tx+ty)/2+tz)

# Simple enough, takes a point and returns its position on the screen
def toscreenpos(x, y, z=0):
    """Returns the screen position of a 3D point, using twofromthree.
    
    Parameters
    ----------
    x: int
        The x coordinate of the point
    y: int
        The y coordinate of the point
    z: int, optional
        The z coordinate of the point (defaults to 0)
    """
    # Going to call width, x, left side, depth, y, right side, and height, z, up
    twod = twofromthree(x,y,z)
    return [d+s/2 for d,s in zip(twod, SIZE)]

# Draws a line in 3d space onto the screen
def line3d(surf, col, pos1, pos2):
    """The 3D equivalent of pygame.draw.line

    Parameters
    ----------
    surf: pygame.Surface
        The surface to draw to
    col: pygame.Color
        The color to draw it in
    pos1, pos2: Tuple[int]
        The points to draw the line at
    """
    draw.line(surf, col, toscreenpos(*pos1), toscreenpos(*pos2))

# Draws a quadrilateral in 3d space
def rect3d(surf, col, p1, p2, p3, p4):
    """The 3D equivalent of pygame.draw.rect

    Parameters
    ----------
    surf: pygame.Surface
        The surface to draw to
    col: pygame.Color
        The color to draw it in
    p1, p2, p3, p4: Tuple[int]
        The points to draw the rect at
    """
    draw.polygon(surf, col, [toscreenpos(*p) for p in (p1, p2, p3, p4)])

# Draws a cube (or similar) in 3d space
def cube3d(surf, cols, tfl, tfr, tbl, tbr, bfl, bfr, bbl, bbr, order=None):
    """Draws a cube on the given surface in 3 colors

    Parameters
    ----------
    surf: pygame.Surface
        The surface to draw to
    cols: Tuple[pygame.Color]
        The three colors to draw the sides in
    tfl, tfr, tbl, tbr, bfl, bfr, bbl, bbr: Tuple[int]
        The corners of the cube (t=top, f=front, l=left and so on)
    """
    rects = [i for i in enumerate([
        # Back sides
        (tbl, bbl, bbr, tbr, cols[0]),
        (tfr, bfr, bbr, tbr, cols[1]),
        # Bottom
        (bfl, bfr, bbr, bbl, cols[2]),
        # Front sides
        (tfl, bfl, bfr, tfr, cols[0]),
        (tfl, bfl, bbl, tbl, cols[1]),
        # Top
        (tfl, tfr, tbr, tbl, cols[2])
    ])]
    get_dist = lambda r: min(cam_dist(*p) for p in r[1][:4])
    if order is not None:
        blocks = [rects[i] for i in order]
        for idx, (p1, p2, p3, p4, c) in blocks:
            rect3d(surf, c, p1, p2, p3, p4)
        return order
    else:
        o = []
        for idx, (p1, p2, p3, p4, c) in order_closelast(rects, get_dist)[3:]:
            o.append(idx)
            rect3d(surf, c, p1, p2, p3, p4)
        return o

# Basic 3d sprite class, works best in a Group3D
class Sprite3d(Sprite):
    """A subclass of pygame.sprite.Sprite that has 3D functionality

    Attributes
    ----------
    x, y, z: int
        The x, y, and z coordinates of the sprite's origin
    width, height, depth: int
        The width, height, and depth of the sprite's bounding box
    vel: Tuple[int]
        The sprite's velocity
    pos, size: Tuple[int], property
        The size and position of the sprite, in Tuples rather than as
        3 separate variables
    back_pos, center: Tuple[int], property
        The position of the corner opposite the origin, and the center point
        in the bounding box
    top_rect: pygame.Rect, property
        The rectangle you'd see if you looked at the bounding box from the top.

    Methods
    -------
    move3d(x, y, z=0)
        Moves the sprite by the requested amount
    dist_point()
        Returns the corner of the bounding box with the median camera
        distance. Don't ask why.
    """
    def __init__(self, x:int, y:int, z:int, w:int, h:int, d:int, vel:Tuple[int, int, int]):
        """
        Parameters
        ----------
        x, y, z: int
            The x, y, and z position of the sprite
        w, h, d: int
            The width, height, and depth of the sprite's
            bounding box
        vel: Tuple[int, int, int]
            The sprite's initial velocity
        """
        super().__init__()
        self.x, self.y, self.z = x,y,z
        self.width, self.height, self.depth = w,h,d
        self.vel = vel

    @property
    def pos(self) -> Tuple[int, int, int]:
        return (self.x, self.y, self.z)
    @pos.setter
    def pos(self, val: Tuple[int, int, int]):
        self.x, self.y, self.z = val

    @property
    def size(self) -> Tuple[int, int, int]:
        return (self.width, self.depth, self.height)
    @size.setter
    def size(self, val:Tuple[int, int, int]):
        self.width, self.depth, self.height = val

    @property
    def back_pos(self) -> Tuple[int, int, int]:
        return add(self.pos, self.size)

    @property
    def center(self) -> Tuple[int, int, int]:
        return add(self.pos, [s/2 for s in self.size])
    
    @property
    def top_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.depth)
    
    def move3d(self, x:int, y:int, z:int=0):
        """Moves the sprite the requested amount
        
        Parameters
        ----------
        x, y, z: int, z is optional
            The amounts to move the sprite by
        """
        self.x += x
        self.y += y
        self.z += z

    def update(self):
        self.move3d(*self.vel)

    def dist_point(self) -> Tuple[int, int, int]:
        """Returns the corner of the bounding box with the median camera
        distance. Don't ask why."""
        crd = [z for z in zip(self.back_pos, self.pos)]
        positions = [(x,y,z) for x in crd[0] for y in crd[1] for z in crd[2]]
        positions.sort(key=lambda p: cam_dist(*p))
        return positions[int((len(positions)+1)/2)]
        # It's the corner that has the median distance to the camera (roughly)

# A basic implementation of the Sprite3d class that renders the sprite as a cube.
# Nice for testing, and for subclassing to make a lot of other things.
class Cube(Sprite3d):
    """A subclass of Sprite3d that draws itself as a cube. Nice for testing.
    
    Attributes
    ----------
    color: pygame.Color
        The cube's base color, which is shaded a bit on each side
    side_select: dict[Tuple[int], list[int]]
        A dictionary of previously drawn sides at given camera angles
        that is checked when drawing for optimization purposes
    """
    def __init__(self, x:int, y:int, z:int, width:int, depth:int, height:int, color:pygame.Color, vel:Tuple[int, int, int]=(0,0,0)):
        """
        Parameters
        ----------
        x, y, z: int
            The x, y, and z position of the cube
        width, height, depth: int
            The width, height, and depth of the cube's
            bounding box
        vel: Tuple[int]
            The cube's initial velocity
        """
        super().__init__(x,y,z,width,height,depth,vel)
        self.color = color
        self.side_select = {}
    
    def draw(self, surf:pygame.Surface):
        # Colors
        unclamped_cols = (add(self.color,c) for c in (
            (-99,-99,-99), (-50, -50, -50), (0,0,0)
        ))
        cols = [[clamp(c, 0, 255) for c in col] for col in unclamped_cols]

        # Shorthand
        w, h, d = self.width, self.height, self.depth
        # Positions
        pos = [add(p, self.pos) for p in (
            (0,0,0), (w,0,0), (0,d,0), (w,d,0), (0,0,h), (w,0,h), (0,d,h), (w,d,h)
        )]

        # Draw the cube
        cam_angle = get_angles()
        sides = None if cam_angle not in self.side_select else self.side_select[cam_angle]
        new_order = cube3d(surf, cols, *pos, sides)
        self.side_select[cam_angle] = new_order

# Test which object is highest (least Z) in an array
def highest(objects:List[Sprite3d]) -> Sprite3d:
    """Returns the object in a list with the lowest z value

    Parameters
    ----------
    objects: list[Sprite3d]
        The list to look through
    """
    obj_copy = objects.copy()
    obj_copy.sort(key=lambda o: o.z)
    return obj_copy[0]

# Determines position of "camera" in 3d space
def cam_pos() -> Tuple[int, int, int]:
    """Returns the position of the camera in 3D space"""
    cdist = -5000
    axy, axz = get_angles()
    tx, ty = rotate(cdist,cdist,-axy)
    tx, tz = rotate(tx, cdist, -axz)
    return (tx, ty, tz)
    
# Not an exact distance measure, but it works well enough. I think.
# 45 degree angles might be a problem sometimes though.
def cam_dist(x:int,y:int,z:int) -> int:
    """Returns a point's distance to the camera, as decided by cam_pos()
    
    Parameters
    ----------
    x, y, z: int
        The coordinates of the point
    """
    # tx, tz = rotate(x, z, axz)
    # tx, ty = rotate(tx, y, axy)
    # return sum(c for c in (tx, ty, tz))
    return sum(abs(p-cp) for p,cp in zip((x,y,z), cam_pos()))

# Sprite implementation of the cam_dist function
def spr3d_cam_dist(spr3d:Sprite3d) -> int:
    """An implementation of cam_dist that gets its point from a sprite
    
    Parameters
    ----------
    spr3d: Sprite3d
        The sprite to get the position from
    """
    return cam_dist(*spr3d.dist_point())

# Given an array of sprites, returns a copy sorted by distance
def order_closelast(objects:List[Sprite3d], dist:Callable[[Any],int] = spr3d_cam_dist):
    """Returns a copy of a list of objects, sorted by distance to the camera
    
    Parameters
    ----------
    objects: list[Sprite3d]
        The list of objects to sort
    dist: (Any -> int), optional
        The function to use for camera distance. Defaults to spr3d_cam_dist
    """
    obj_copy = objects.copy()
    obj_copy.sort(key=lambda o: dist(o), reverse=True)
    return obj_copy

# Basic group for 3D sprites, uses order_closelast to draw
class Group3D(CustomGroup):
    """A subclass of pygame.sprite.Group that renders 3D sprites in the correct order."""
    def draw(self, surface, to_draw=None):
        for spr in order_closelast(self.sprites()):
            spr.draw(surface)
            
        self.lostsprites = []