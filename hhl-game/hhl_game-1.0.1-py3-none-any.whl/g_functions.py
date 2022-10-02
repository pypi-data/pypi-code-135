from .gameeventloop import EventController, UpdateController
from collections import defaultdict
import pygame
from pygame import sprite

class AnimationController:

    def __init__(self, g_obj, action_controller, event_controller: EventController, update_controller: UpdateController):
        self.event_controller = event_controller
        self.update_controller = update_controller
        self.action_controller = action_controller
        self.g_obj = g_obj

    def create_animation(self, gobj_name, anime_name, action_switch_kvls: list[tuple[object, int]], anime_name_path, anime_number_range: tuple[int, int], switch_type='&&'):
        '''
        创建一个动画
        :param gobj_name: 对象名称
        :param anime_name: 动画名称
        :param action_switch_kvls: 条件判断关系对
        :param switch_type: 只接受字符串: '&&'、'||'
        :param anime_name_path: 动画路径名称
        :param anime_number_range: 动画路径名称编号
        '''
        if not hasattr(self.g_obj[gobj_name], 'anime_dict'):
            self.g_obj[gobj_name].anime_dict = defaultdict()
            self.g_obj[gobj_name].action_controller = self.action_controller
        anime_img_ls = []
        for img_number in range(anime_number_range[0], anime_number_range[1]+1):
            if img_number < 10:
                anime_img_ls.append(anime_name_path + "_" + "0" + str(img_number) + ".png")
            else:
                anime_img_ls.append(anime_name_path + "_" + str(img_number) + ".png")
        anime_length = len(anime_img_ls)
        self.g_obj[gobj_name].anime_dict[anime_name] = {'anime_length': anime_length, 'anime_number': 0, 'anime_img_ls':anime_img_ls, 'action_switch_kvls': action_switch_kvls, 'is_active':0}
        self.update_controller.bind_u('anime_play', obj=self.g_obj[gobj_name], action_switch_kvls=action_switch_kvls, switch_type=switch_type,
                                      anime_name_path=anime_name_path, anime_number_range=anime_number_range, anime_name=anime_name)

    def play_anime(self, gobj_name, anime_name):
        '''
        启用动画
        :param gobj_name: 对象名称
        :param anime_name: 动画名称
        '''
        self.g_obj[gobj_name].anime_dict[anime_name]['is_active'] = 1

    def __getitem__(self, key):
        return self.g_obj.anime_dict[key]
class ActionController:

    def __init__(self, scene, g_obj, event_controller: EventController, update_controller: UpdateController):
        self.event_controller = event_controller
        self.update_controller = update_controller
        self.action_dict = defaultdict()

        self.scene = scene
        self.g_obj = g_obj

    def create_action(self, action_name, action_value, func):
        self.action_dict[action_name] = {'action_value':action_value, 'func': func}

    def bind_action(self, action_name, event_type, hot_key, action_value, meta={}):
        self.event_controller.bind(event_type, lambda meta:self.action_dict[action_name]['func'](meta), hot_key, meta={'self':self, 'action_name':action_name, 'action_value': action_value, 'meta':meta})

    def __getitem__(self, key):
        return self.action_dict[key]

class CharacterController:

    def __init__(self, scene, g_obj, action_controller, event_controller: EventController,
                 update_controller: UpdateController):
        self.event_controller = event_controller
        self.update_controller = update_controller
        self.action_controller = action_controller
        self.g_obj = g_obj
        self.g_obj.character_dict = defaultdict()
        self.scene = scene

    def bind_event(self, action_name, action_switch_kvls: list[tuple[object, int]], func, meta={},switch_type="&&"):
        self.update_controller.bind_u('character_event', action_name=action_name, action_switch_kvls=action_switch_kvls, func=func, gobj=self.g_obj, switch_type=switch_type, scene=self.scene, meta=meta)

class SpriteRect(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.rect = pygame.Rect(0, 0, width, height)

class CollisionController():

    def __init__(self, g_obj, collision_range, collision_size, obj_range, action_controller, event_controller: EventController,
                 update_controller: UpdateController):
        '''
        碰撞检测器
        :param g_obj: game_object对象
        :param collision_range: 检测器检测长度
        :param collision_size: 检测器检测宽度，顺序为上、下、左、右
        :param obj_range: 距离game_object的范围，顺序为上、下、左、右
        :param action_controller:
        :param event_controller:
        :param update_controller:
        '''
        self.event_controller = event_controller
        self.update_controller = update_controller
        self.action_controller = action_controller
        self.g_obj = g_obj
        self.g_obj.can_move_right = True
        self.g_obj.can_move_left = True
        self.g_obj.can_move_top = True
        self.g_obj.can_move_bottom = True
        self.r_rect = SpriteRect(collision_range, collision_size[3])
        self.l_rect = SpriteRect(collision_range, collision_size[2])
        self.t_rect = SpriteRect(collision_size[0], collision_range)
        self.d_rect = SpriteRect(collision_size[1], collision_range)

        self.obj_range = obj_range

        self.check_r = False
        self.check_l = False
        self.check_t = False
        self.check_d = False