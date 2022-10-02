import pygame
from collections import defaultdict
from .g_obj import *
from .gametools import GameFun
from .gameeventloop import UpdateController, EventController

class GameObject(pygame.sprite.Sprite, GameFun):

    def __init__(self, scene, position, size, event_controller:EventController, update_controller:UpdateController):
        super().__init__()
        self.type = 'game_object'
        self.rect = pygame.Rect(*position, *size)
        self.object_dict = defaultdict()
        self.delay_dict = defaultdict()
        self.count = 0
        self.scene = scene
        self.original_x = position[0]
        self.original_y = position[1]

        self.event_controller = event_controller
        self.update_controller = update_controller

    def create_rect(self, object_name: str, img_path: str, size: tuple[int, int] = None,
                    position: tuple[int, int] = (0, 0)):

        self.object_dict[object_name] = Rect(img_path, size, position, self.event_controller, self.update_controller)

    def create_font(self, object_name: str, text: str, font_size: int = 50,
                     color: tuple[int, int, int] = (0, 0, 0), position: tuple[int, int] = (0, 0)):
        self.object_dict[object_name] = Font(text, font_size, color, position, self.event_controller, self.update_controller)

    def create_button(self,
                      object_name: str,
                      text: str,
                      font_size: int = 50,
                      color: tuple[int, int, int] = (255, 255, 255),
                      position: tuple[int, int] = (0, 0),
                      bg_color: tuple[int, int, int] = (0, 0, 0),
                      hover_color: tuple[int, int, int] = (0, 0, 0),
                      hover_bg_color: tuple[int, int, int] = (255, 255, 255),
                      font_style:str = 'C:/Windows/Fonts/RAVIE.TTF',
                      ):
        self.object_dict[object_name] = Button(text, font_size, color, position, bg_color, self.event_controller,
                                               self.update_controller, hover_color, hover_bg_color,font_style)

    def create_txtRender(self, object_name: str, position=(0, 0), size=(700, 200)):
        self.object_dict[object_name] = TextRender(size, position, self.scene, self.event_controller, self.update_controller)

    def create_camera(self):
        self.camera = ''

    def delete_object(self, object_name: str):
        self.object_dict.pop(object_name)

    def values(self):
        return self.object_dict.values()

    def __getitem__(self, object_name) -> Rect:
        return self.object_dict[object_name]

    def add_collision(self):
        self.update_controller.bind_u('collision', collision_obj = self)

class DelayObject:

    def __init__(self, camera_obj, original_x, target_x, speed):
        self.scene = camera_obj.scene
        self.original_x = original_x
        self.target_x = target_x
        self.speed = speed
        self.is_invalid = False
        self.is_active = False

    def bind(self, func):
        self.func = func
    def run(self, delay_event):
        self.func(self, self.scene)

    def __str__(self):
        return str(self.speed)

def c_r(dfunc, scene):
    if dfunc.original_x < dfunc.target_x:
        obj_move(scene, x=-1 * dfunc.speed)
    else:
        dfunc.is_active = False
        dfunc.is_invalid = True
    dfunc.original_x += dfunc.speed

def obj_move(scene,x=0,y=0):
    for gobj_key in scene.game_object_dict:
        if not hasattr(scene[gobj_key], 'camera'):
            scene[gobj_key].rect.x += x
            scene[gobj_key].rect.y += y

class CameraObject(GameFun):

    def __init__(self, scene, position, size, event_controller:EventController, update_controller:UpdateController):
        self.type = 'camera'
        self.rect = pygame.Rect(*position, *size)
        self.object_dict = defaultdict()
        self.delay_dict = defaultdict()
        self.count = 0
        self.scene = scene
        self.original_x = position[0]
        self.original_y = position[1]

        self.event_controller = event_controller
        self.update_controller = update_controller

        self.addActionController()
        self.addCharacterController()
        self.action_controller.create_action('walk_r', 0, self.walk_r)

    def walk_r(self, meta):
        action_controller = meta['self']
        action_controller['walk_r']['action_value'] = meta['action_value']

    def move(self, delay_event_name, direction, distance, speed):
        if direction == 'right':
            original_x = self.original_x
            target_x = original_x + distance
            self.original_x = target_x
            print('初始', original_x, target_x)
            f = DelayObject(self, original_x, target_x, speed)
            f.bind(c_r)
            delay_ls = self.delay_dict.get(delay_event_name, [])
            delay_ls.append(f)
            self.delay_dict[delay_event_name] = delay_ls

    def work(self):
        for vls in self.delay_dict.values():
            self.update_controller.bind_u('delay_event', func_obj_ls=vls)





