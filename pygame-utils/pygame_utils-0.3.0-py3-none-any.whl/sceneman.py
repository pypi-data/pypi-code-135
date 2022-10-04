"""sceneman
Adds a scene manager, as well as a class for making scenes

Classes
-------
Scene
    Represents a "room" in the game, has functions for updating
    and drawing its contents.

Functions
---------
init(surf: Surface, start_scene: str)
    Initializes everything this module needs. Should be called at
    the start of a program, just after pygame.init()
update()
    Updates the current scene. Not sure why this exists when
    there's Scene.play(), but oh well.
draw(surf: Surface=None)
    Draws the current scene to the screen, or to the provided surface
    if there is one.
set_scene(scene: str)
    Ends the current scene and switches to the provided one.
restart_scene()
    Restarts the current scene

Other Exports
-------------
clock
    The clock used for ticking the scenes, assuming update_raw remains intact.
curr_scene
    The current scene.
running
    Whether the program is still going, or if it's done.
scenes
    Effectively a dictionary of all of the scenes by name.
"""

import pygame, os, sys, inspect
clock = pygame.time.Clock()

# This class is meant to be inherited/overridden
# Any class that does so is a scene (a collection
# of groups and variables that acts as a "room" in
# the game)
class Scene:
    """A class that represents a scene, or "room" in a game.
    
    This class is meant to be overridden to make new scenes,
    with their own groups, sprites, and variables. Any and
    all of the following functions can be overridden, but
    there's already a baseline implementation of each if you
    don't need to change it.

    Attributes
    ----------
    groups: list[pygame.sprite.Group]
        The groups that the scene should update/draw
    
    Methods
    -------
    draw(surf:Surface)
        Draws everything in the scene to the given surface
    update()
        Runs the update function of each of the parts of the scene
    update_raw()
        Calls update(), ticks the clock, and returns True to keep
        the scene running
    on_start()
        Runs any starting/resetting behaviors of the scene
    on_end()
        Runs any ending/resetting behaviors of the scene
    play()
        Does everything required to let the scene run its course."""
    
    def __init__(self, *groups: pygame.sprite.Group):
        """
        Parameters
        ----------
        groups: list[pygame.sprite.Group]
            The groups that this scene should keep track of
        """
        self.groups = groups

    def draw(self, surf: pygame.Surface):
        """Draws everything in the scene to the provided surface
        
        Parameters
        ----------
        surf: pygame.Surface
            The surface to draw to
        """
        surf.fill((0, 0, 0))
        for g in self.groups:
            g.draw(surf)

    def update(self):
        """Updates everything in the scene. Can return False to
        stop the scene, or None or True to keep running.
        """
        for g in self.groups:
            g.update()
        return True

    def update_raw(self):
        """Returns the result of self.update() (or True if nothing is returned),
        and also ticks the clock. Can be overridden instead of update for
        somewhat more advanced control over the updating of the scene.
        """
        rtn = self.update()
        clock.tick(30)
        return rtn if rtn is not None else True

    def on_start(self):
        """Called when the scene starts or restarts"""
        pass

    def on_end(self):
        """Called when the scene ends or restarts"""
        pass

    def play(self, surf: pygame.Surface):
        """Runs the scene until self.update() returns False, signifying
        that it should stop.
        
        Parameters
        ----------
        surf: pygame.Surface
            The surface that should be used as the screen.
        """
        self.on_start(surf)
        run = True
        while run:
            run = self.update_raw()
            self.draw(surf)
        self.on_end(surf)

# Some globals for management
curr_scene = None
_surf = None
running = True

# Run this to start the scene management
def init(surf: pygame.Surface, start_scene: str):
    """Initializes the scene manager. Run this just after pygame.init
    
    Parameters
    ----------
    surf: pygame.Surface
        The surface to treat as the screen
    start_scene: str
        The name of the starting scene
    """
    # need this for _scene_cls to work
    currentdir = os.path.dirname(os.getcwd())
    print(currentdir)
    sys.path.insert(0, currentdir) 
    global _surf
    _surf = surf
    set_scene(start_scene)
    
# Run this every frame to update the scene
def update():
    """Updates the current scene"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    global running
    running = curr_scene.update_raw()

# Run this to draw the scene to a screen surface
def draw(surf:pygame.Surface=None):
    """Draws the current scene
    
    Parameters
    ----------
    surf: pygame.Surface, optional
        The surface to draw to. Defaults to the surface passed into init()
    """
    curr_scene.draw(surf if surf is not None else _surf)
    pygame.display.update()

# Run this to change the scene
def set_scene(scene:str):
    """Ends the current scene and starts the selected one
    
    Parameters
    ----------
    scene: str
        The scene to switch to
    """
    global curr_scene
    if curr_scene is not None:
        curr_scene.on_end()
    curr_scene = scenes[scene]
    curr_scene.on_start()

# Run this to restart the current scene
def restart_scene():
    """Restarts the current scene by calling on_end and on_start."""
    curr_scene.on_end()
    curr_scene.on_start()

# Basic thing for finding scene files
class _scene_cls(dict):
    def __getitem__(self, val:str):
        try:
            return super().__getitem__(val)
        except KeyError:
            self[val] = __import__(val+"scene").scene
            print(f"found {self[val]}")
            return self[val]

# Effectively a runtime dictionary of scenes
# Finds them by name, then looks for
# [name]scene.py and takes the "scene" var
scenes = _scene_cls()