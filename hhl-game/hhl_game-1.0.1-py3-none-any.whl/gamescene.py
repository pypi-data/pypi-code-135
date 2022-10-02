import pygame
from collections import defaultdict
from .gameobj import GameObject, CameraObject
from .gameeventloop import EventController, UpdateController



class Scene:

    def __init__(self, scene_name: str, size: tuple[int, int], bg_color):
        self.bg = bg_color
        self.name = scene_name
        self.screen = pygame.display.set_mode(size)
        self.screen_rect = self.screen.get_rect()
        self.game_object_dict = defaultdict()
        self.camera_object_dict = defaultdict()

        self.event_controller = EventController()
        self.update_controller = UpdateController()

        self.main_txt = 'hello world'

    def create_game_object(self, object_name, position: tuple[int, int] = (0, 0), size: tuple[int, int] = (0, 0)):
        game_object = GameObject(self, position, size, self.event_controller, self.update_controller)
        self.game_object_dict[object_name] = game_object

    def create_camera_object(self, position=None, size=(0, 0)):
        if not position:
            position = self.screen_rect.center
        self.camera = CameraObject(self, position, size, self.event_controller, self.update_controller)

    def fill(self):
        for event in pygame.event.get():
            self.event_controller.listen(event)
        self.screen.fill(self.bg)
        self.update_controller.update_action()
        for object_name, game_object in self.game_object_dict.items():
            self.load_game_object(game_object)

    def check_collision(self, game_object):
        '''
        碰撞检测
        :param game_object:
        :return:
        '''
        if hasattr(game_object, 'collision_controller'):
            g_centerx = game_object.rect.centerx
            g_centery = game_object.rect.centery
            obj_range = game_object.collision_controller.obj_range
            game_object.collision_controller.r_rect.rect.x = game_object.rect.right + obj_range[3]
            game_object.collision_controller.r_rect.rect.centery = g_centery
            game_object.collision_controller.l_rect.rect.x = game_object.rect.left - obj_range[2]
            game_object.collision_controller.l_rect.rect.centery = g_centery

            game_object.collision_controller.t_rect.rect.centerx = g_centerx
            game_object.collision_controller.t_rect.rect.y = game_object.rect.top - obj_range[0]
            game_object.collision_controller.d_rect.rect.centerx = g_centerx
            game_object.collision_controller.d_rect.rect.y = game_object.rect.bottom + obj_range[1]
            if pygame.sprite.spritecollide(game_object.collision_controller.r_rect,
                                           self.update_controller.collision_group,
                                           False):
                game_object.can_move_right = False
            else:
                game_object.can_move_right = True
            if pygame.sprite.spritecollide(game_object.collision_controller.l_rect,
                                           self.update_controller.collision_group,
                                           False):
                game_object.can_move_left = False
            else:
                game_object.can_move_left = True
            if pygame.sprite.spritecollide(game_object.collision_controller.t_rect,
                                           self.update_controller.collision_group,
                                           False):
                game_object.can_move_top = False
            else:
                game_object.can_move_top = True
            if pygame.sprite.spritecollide(game_object.collision_controller.d_rect,
                                           self.update_controller.collision_group, False):
                game_object.can_move_bottom = False
            else:
                game_object.can_move_bottom = True
            # self.screen.fill((0, 0, 0), game_object.collision_controller.r_rect)
            # self.screen.fill((0, 0, 0), game_object.collision_controller.l_rect)
            # self.screen.fill((0, 0, 0), game_object.collision_controller.t_rect)
            # self.screen.fill((0, 0, 0), game_object.collision_controller.d_rect)
    def load_game_object(self, game_object):
        self.check_collision(game_object)
        for gobj in game_object.values():

            gobj.rect.x = game_object.rect.x + gobj.position_for_obj[0]
            gobj.rect.y = game_object.rect.y + gobj.position_for_obj[1]
            if gobj.type == 'rect':
                self.screen.blit(gobj.image, gobj.rect)
            elif gobj.type == 'font':
                self.screen.blit(gobj.text, gobj.rect)
            elif gobj.type == 'button':
                self.screen.blit(gobj.text, gobj.rect)
            elif gobj.type == 'text_render':
                if gobj.is_show:
                    if gobj.is_play:
                        gobj.play(self.main_txt)
                    self.screen.blit(gobj.textbox_surf, gobj.rect)
    def __getitem__(self, game_object_name) -> GameObject:
        return self.game_object_dict[game_object_name]

    def bind(self, event_type, func, hot_key=None, meta={}):
        self.event_controller.bind(event_type, func, hot_key, meta)
