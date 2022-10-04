"""utils
Adds various utility functions/classes, some of which are used in this module.

Classes
-------
CustomSprite
    A subclass of pygame.sprite.Sprite that has a custom draw() function
    rather than using a sprite. It's slower, but it's more customizable.
CustomGroup
    A group to hold CustomSprite instances and call their draw() functions.
TextBox
    A class that draws several images to the screen as a textbox.
Button
    A CustomSprite that acts like a button should.
    
Functions
---------
add(*tups)
    Adds each element in a set of tuples together, i.e. add((1,2,3),(4,5,6))
    would return (1+4, 2+5, 3+6), or (5,7,9).
clamp(n, smallest, largest)
    Returns n as long as it's within the bounds set by smallest and largest.
    Otherwise, it returns whichever bound it's closest to.
just_pressed()
    Returns any keys that have appeared in pygame.key.get_pressed() since it
    was last called.
make_txtbox(objs, bg, obj_to_img, obj_change, **rect_kwargs)
    Returns a TextBox object based on the given arguments. standard_textbox
    is a bit better, though.
standard_textbox(objs, bg, font, font_args, **pos_args)
    Returns a TextBox object through a similar process to make_txtbox, but
    is more user-friendly about it.
rect_collision(r1, r2)
    Returns the overlap rectangle between two pygame.Rect s, or None if they
    don't overlap.
"""

import pygame
from pygame.sprite import Group, Sprite
from pygame.key import get_pressed
from typing import Any, Callable, Dict, List, Tuple

def add(*tups: tuple) -> tuple:
    """Adds each element of a set of tuples together.
    add((1,2,3),(4,5,6)) would return (1+4, 2+5, 3+6), or (5,7,9).
    
    Parameters
    ----------
    tups: list[tuple]
        The tuples to sum
    """
    return tuple([sum(itms) for itms in zip(*tups)])

def clamp(n:int, smallest:int, largest:int) -> int:
    """Clamps n to the bounds provided.
    
    Parameters
    ----------
    n: int
        The number to clamp
    smallest, largest: int
        The bounds to clamp n between. smallest <= largest
    """
    return max(smallest, min(n, largest))

# Have to do it like this rather than a list comp
# since get_pressed() doesn't return a straight list
class __j_pressed:
    def __init__(self, first):
        self.last = first
        self.now = first
    def __getitem__(self, val):
        return (not self.last[val]) and self.now[val]
    def update(self, new_vals):
        self.last = self.now
        self.now = new_vals
press_mem = None
# Returns the instance of __j_pressed, with updated keys
# Could have used events for this but I didn't know at the time
def just_pressed() -> Dict[int, bool]:
    """Detects which keys have been pressed since the last time this was called"""
    global press_mem
    if press_mem == None:
        press_mem = __j_pressed(get_pressed())
    press_mem.update(get_pressed())
    return press_mem   

class CustomSprite(Sprite):
    """A sprite that renders with a custom draw() function instead of an image
    
    Attributes
    ----------
    x, y: The position of the sprite. Do what you will with them.

    Methods
    -------
    draw(surf)
        Draws the sprite to the given surface
    alert(event, data)
        A utility function that allows the sprite to handle events
    """
    x:int = 0
    y:int = 0
    def alert(self, event: str, data:Dict[str, Any]=None):
        """A utility function that allows the sprite to handle events.
        
        Parameters
        ----------
        event: str
            The event name that's being registered
        data: Any, optional
            Effectively the arguments passed into the event. Think
            *args and **kwargs.
        """
        pass

class CustomGroup(Group):
    """A group to hold CustomSprites and use their custom draw() functions
    
    Methods
    -------
    alert(event, data)
        Calls the alert function of each of its sprites
    """
    # Copied from the pygame codebase almost directly, I only needed a small change
    # Instead of blitting an image, call the custom draw() function
    def draw(self, surface:pygame.Surface, to_draw=None):
        for spr in self.sprites():
            spr.draw(surface)
            
        self.lostsprites = [] # Need this line for some reason idk

    # This function is new, it pings each sprite to do something
    def alert(self, event:str, data:Dict[str, Any]=None) -> Dict[CustomSprite, Any]:
        """A utility function that allows the group to handle events.
        
        Parameters
        ----------
        event: str
            The event name that's being registered
        data: Any, optional
            Effectively the arguments passed into the event. Think
            *args and **kwargs.
        """
        rtn = {}
        for spr in self.sprites():
            rtn[spr] = spr.alert(event, data)
        return rtn

class TextBox:
    """A collection of images that renders as a textbox

    Attributes
    ----------
    images: list[pygame.Surface]
        All of the images that the textbox renders
    bg: pygame.Color
        The background color of the textbox
    kwargs: dict[str, Any]
        The arguments to pass to the surface in get_img

    Methods
    -------
    get_img()
        Returns a surface that can be drawn to the screen
    get_rects()
        Returns the rects used to place the images in get_img
    get_pos_of(idx, **box_pos_args)
        Gets a particular index of get_rects, with whatever
        transform is asked for by box_pos_args
    draw(surf, **pos_args)
        Draws the result of get_img to the surface, with the
        requested transforms from pos_args
    """
    def __init__(self, images: List[pygame.Surface], bg:pygame.Color, **kwargs:Any):
        """
        Parameters
        ----------
        images: list[pygame.Surface]
        All of the images that the textbox renders
        bg: pygame.Color
            The background color of the textbox
        **kwargs: Any
            The arguments to pass to the surface in get_img
        """
        self.images = images
        self.bg = bg
        self.kwargs = kwargs
    def get_img(self) -> pygame.Surface:
        """Returns a surface with all of the text on it
        """
        size = (max(t.get_width() for t in self.images),
        sum(t.get_height() for t in self.images))
        box = pygame.Surface(size, pygame.SRCALPHA, **self.kwargs).convert_alpha()
        box.fill(self.bg)
    
        v_offset = 0
        for t in self.images:
            blit_rect = t.get_rect(center=(box.get_width()/2,v_offset+t.get_height()/2))
            box.blit(t, blit_rect)
            v_offset += t.get_height()
        return box
    def get_rects(self) -> List[pygame.Rect]:
        """Returns the rects used to blit the images from get_img
        """
        size = (max(t.get_width() for t in self.images),
        sum(t.get_height() for t in self.images))
        box = pygame.Surface(size, pygame.SRCALPHA, **self.kwargs)
    
        v_offset = 0
        rects = []
        for t in self.images:
            blit_rect = t.get_rect(center=(box.get_width()/2,v_offset+t.get_height()/2))
            v_offset += t.get_height()
            rects.append(blit_rect)
        return rects
    def get_pos_of(self, t_idx:int, **box_pos_args:Any) -> pygame.Rect:
        """Gets the position of the image at the specified index, with
        a rect transform specified by box_pos_args

        Parameters
        ----------
        t_idx: int
            The image's index in the array
        **box_pos_args: dict[str, Any]
            The transform to apply to the rect
        """
        rect = self.get_rects()[t_idx]
        img_pos = self.get_img().get_rect(**box_pos_args)
        rect.topleft = add(rect.topleft, img_pos.topleft)
        return rect
    def draw(self, surf:pygame.Surface, **pos_args:Any):
        """Draws the box to the surface, with a rect tranform specified
        in pos_args

        Parameters
        ----------
        surf: pygame.Surface
            The surface to draw to
        **pos_args: dict[str, Any]
            The transform to apply to the image
        """
        img = self.get_img()
        pos = img.get_rect(**pos_args)
        surf.blit(img, pos)

def make_txtbox(objs:list, bg:pygame.Color, obj_to_img:Callable[[Any],pygame.Surface]=lambda o:o, obj_change:Callable[[pygame.Surface, pygame.Rect, Any],None]=lambda img,rect,o:None, **rect_kwargs:Any) -> TextBox:
    """A function to more easily make a textbox. standard_textbox is better.

    Parameters
    ----------
    objs: list[Any]:
        All of the objects to be put into the textbox
    bg: pygame.Color
        The background color
    obj_to_img: Any->pygame.Surface
        A function to turn any object into an image
    obj_change: (pygame.Surface, pygame.Rect, Any) -> None
        A function to do whatever is needed to an object
        after the textbox is made
    **rect_kwargs: dict[str, Any]
        The kwargs to apply to get_pos_of when running obj_change

    Returns
    -------
    TextBox
        The textbox
    """
    images = []
    obj_imgs = {}
    for obj in objs:
        img = obj_to_img(obj)
        images.append(img)
        obj_imgs[obj] = img

    box = TextBox(images, bg)

    for idx, (obj, img) in enumerate(obj_imgs.items()):
        rect = box.get_pos_of(idx, **rect_kwargs)
        obj_change(img, rect, obj)

    return box

def standard_textbox(objs: list, bg:pygame.Color, font:pygame.font.Font, font_args:list, **pos_args:Any):
    """A better version of make_txtbox.

    Note
    ----
    This function accepts the following as objects:
        Button
        str
        tuple[str, pygame.font.Font]
        Surface

    Parameters
    ----------
    objs: list[Any]:
        The list of objects to be put into the textbox
    bg: pygame.Color
        The background color
    font: pygame.font.Font
        The default font for any text passed in
    font_args: list[Any]
        The default arguments to apply to unrendered text
    **pos_args: dict[str, Any]
        The position arguments to pass into make_txtbox

    Returns
    -------
    TextBox
        The textbox
    """
    def to_img(obj):
        if isinstance(obj, Button):
            b = pygame.Surface(obj.rect.size, pygame.SRCALPHA).convert_alpha()
            b.fill((255,255,255,0))
            return b
        elif isinstance(obj, str):
            return font.render(obj, True, (255,255,255))
        elif isinstance(obj, tuple) and isinstance(obj[0], str):
            return obj[1].render(obj[0], True, (255,255,255))
        else:
            return obj
            
    def change_obj(img, rect, obj):
        if isinstance(obj, Button):
            obj.rect = rect
    
    # Create textbox
    return make_txtbox(
        objs, bg,
        to_img, change_obj, **pos_args
    )

class Button(CustomSprite):
    """A sprite that's a button. Pretty self-explanatory

    Attributes
    ----------
    image: pygame.Surface
        The button's image
    rect: pygame.Rect
        The image's rect
    on_click: None -> None
        What to do when the button is clicked
    mouse_down: bool
        Whether the mouse was down the last time this checked
    """
    def __init__(self, pos:Tuple[int, int], text_img:pygame.Surface, on_click:Callable=None):
        """
        Parameters
        ----------
        image: pygame.Surface
            The button's image
        rect: pygame.Rect
            The image's rect
        on_click: None -> None, optional
            What to do when the button is clicked. Defaults
            to doing nothing.
        """
        super().__init__()
        self.image = text_img
        self.rect = text_img.get_rect(center=pos)
        self.on_click = (lambda: print("clicked")) if on_click is None else on_click
        self.mouse_down = pygame.mouse.get_pressed(3)[0]
    def draw(self, surf:pygame.Surface):
        surf.blit(self.image, self.rect)
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed(3)[0]
        if self.rect.left < mouse_pos[0] < self.rect.right\
        and self.rect.top < mouse_pos[1] < self.rect.bottom:
            # The 3 is to signify that the mouse has 3
            # buttons, and the 0 is for the first
            if mouse_press and not self.mouse_down:
                self.clicked()
            # else do some hovering stuff if you want
        self.mouse_down = mouse_press
    def clicked(self):
        """A function that can be overridden in a subclass for
        more complex click actions. Right now it just calls on_click.
        """
        self.on_click()

def rect_collision(r1:pygame.Rect, r2:pygame.Rect):
    """Determines whether two rects have collided, and gives
    the rect of overlap between them if they have.

    Parameters
    ----------
    r1, r2: pygame.Rect
        The two rects to check between

    Returns
    -------
    pygame.Rect
        The overlap, or None if there isn't one
    """
    top = max(r1.top, r2.top)
    bottom = min(r1.bottom, r2.bottom)
    left = max(r1.left, r2.left)
    right = min(r1.right, r2.right)
    
    if right > left and bottom > top:
        return pygame.Rect(left, top, right-left, bottom-top)
    else:
        return None