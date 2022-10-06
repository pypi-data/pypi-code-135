from __future__ import annotations
from tkinter import Button as bt, Tk, Canvas
from .game_object import Game_Object
from .button import Button
from time import sleep, time

class Scene:
    """
    the scene class where the game takes place
    """

    def __init__(self, objects:list[Game_Object]=[], name:str="", width="900", height="600", bg:str="#ffffff"):
        self.__new_objects:list[Game_Object] = []
        self.__active_objects:list[Game_Object] = []
        self.__destroyed_objects:list[Game_Object] = []

        self.__name = name
        self.__width = width
        self.__height = height
        self.__bg = bg

        self.__destroyed = False
      
        for obj in objects:
            self.__new_objects.append(obj)

    def init_game_object(self, *obj:Game_Object):
        """
        initializes the given Game Objects into the scene
        """

        for object in obj:
            self.__new_objects.append(object)
    
    def destroy_game_object(self, *obj:Game_Object):
        """
        deletes the given Game Objects from the scene
        """
        for object in obj:
            self.__active_objects.remove(object)
            self.__destroyed_objects.append(object)
    
    def destroy(self):
        """
        destroys the scene and closes the window
        """

        self.__destroyed = True
        self.__window.destroy()
    
    def switch_scene(self, scene:Scene):
        self.destroy()

        new_scene = scene
        new_scene.startloop()

    def startloop(self):
        """
        starts the main loop of the scene 
        """

        delta = 0

        # creates the window and canvas for the game
        self.__window = Tk()
        self.__window.title(self.__name)
        self.__window.resizable(False, False)
        self.__window.protocol("WM_DELETE_WINDOW", self.destroy)

        self.__canvas = Canvas(self.__window, width=self.__width, height=self.__height, bg=self.__bg)
        self.__canvas.pack()

        # a dictionary with references to functions for the shapes 
        shapes = {
            'rect': self.__canvas.create_rectangle,
            'oval': self.__canvas.create_oval,
            'arc': self.__canvas.create_arc
        }

        while True:
            Time = time()
            # taking the objects from __new_objects and puts it in __active_objects
            for _ in range(len(self.__new_objects)):
                obj = self.__new_objects.pop(0)
                self.__active_objects.append(obj)

            # removing the destroyed objects from the scene
            for obj in self.__destroyed_objects:
                self.__canvas.delete(obj.uuid)
                obj.on_destroy()
            
            self.__destroyed_objects.clear()

            # rendering the objects in __active_objects
            for obj in self.__active_objects:
                if type(obj) == Button:
                    if not obj.initialized: self.__canvas.create_window(obj.transform.position.x, obj.transform.position.y, height=obj.transform.height, width=obj.transform.width, window=bt(background=obj.background, foreground=obj.foreground, text=obj.text, command=obj.on_press), tags=obj.uuid)
                    obj.initialized = True
                else:
                    self.__canvas.delete(obj.uuid)
                    shapes[obj.shape](obj.transform.position.x, obj.transform.position.y, obj.transform.width+obj.transform.position.x, obj.transform.position.y+obj.transform.height, fill=obj.colour, outline=obj.colour, tags=obj.uuid)

            # calls the update method of every object in __active_objects
            for obj in self.__active_objects:
                obj.update(delta)

                if self.__destroyed:
                    break

            self.__window.update()

            if self.__destroyed:
                break
                
            delta = time() - Time
            if delta == 0:
                delta = 0.01
                sleep(0.01)