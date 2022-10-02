import pygame
import sys
from collections import defaultdict
from pygame.sprite import Group


def hotkey_bind(e, event, func):
    # print(e['hot_key'])
    if e['hot_key']:
        if e['hot_key'] == 'a':
            if event.key == pygame.K_a:
                func(e['meta'])
        elif e['hot_key'] == 'b':
            if event.key == pygame.K_b:
                func(e['meta'])
        elif e['hot_key'] == 'c':
            if event.key == pygame.K_c:
                func(e['meta'])
        elif e['hot_key'] == 'd':
            if event.key == pygame.K_d:
                func(e['meta'])
        elif e['hot_key'] == 'e':
            if event.key == pygame.K_e:
                func(e['meta'])
        elif e['hot_key'] == 'f':
            if event.key == pygame.K_f:
                func(e['meta'])
        elif e['hot_key'] == 'g':
            if event.key == pygame.K_g:
                func(e['meta'])
        elif e['hot_key'] == 'h':
            if event.key == pygame.K_h:
                func(e['meta'])
        elif e['hot_key'] == 'i':
            if event.key == pygame.K_i:
                func(e['meta'])
        elif e['hot_key'] == 'j':
            if event.key == pygame.K_j:
                func(e['meta'])
        elif e['hot_key'] == 'k':
            if event.key == pygame.K_k:
                func(e['meta'])
        elif e['hot_key'] == 'l':
            if event.key == pygame.K_l:
                func(e['meta'])
        elif e['hot_key'] == 'm':
            if event.key == pygame.K_m:
                func(e['meta'])
        elif e['hot_key'] == 'n':
            if event.key == pygame.K_n:
                func(e['meta'])
        elif e['hot_key'] == 'o':
            if event.key == pygame.K_o:
                func(e['meta'])
        elif e['hot_key'] == 'p':
            if event.key == pygame.K_p:
                func(e['meta'])
        elif e['hot_key'] == 'q':
            if event.key == pygame.K_q:
                func(e['meta'])
        elif e['hot_key'] == 'r':
            if event.key == pygame.K_r:
                func(e['meta'])
        elif e['hot_key'] == 's':
            if event.key == pygame.K_s:
                func(e['meta'])
        elif e['hot_key'] == 't':
            if event.key == pygame.K_t:
                func(e['meta'])
        elif e['hot_key'] == 'u':
            if event.key == pygame.K_u:
                func(e['meta'])
        elif e['hot_key'] == 'v':
            if event.key == pygame.K_v:
                func(e['meta'])
        elif e['hot_key'] == 'w':
            if event.key == pygame.K_w:
                func(e['meta'])
        elif e['hot_key'] == 'x':
            if event.key == pygame.K_x:
                func(e['meta'])
        elif e['hot_key'] == 'y':
            if event.key == pygame.K_y:
                func(e['meta'])
        elif e['hot_key'] == 'z':
            if event.key == pygame.K_z:
                func(e['meta'])

class EventController:

    def __init__(self):
        self.event_ls = []

    def listen(self, event):
        # print(self.event_ls)
        if event.type == pygame.QUIT:
            sys.exit()
        for e in self.event_ls:
            event_type, func, hot_key = e['event_type'], e['func'], e['hot_key']
            if event_type == 'KEYDOWN':
                if event.type == pygame.KEYDOWN:
                    hotkey_bind(e, event, func)
            elif event_type == 'KEYUP':
                if event.type == pygame.KEYUP:
                    hotkey_bind(e, event, func)

            elif event_type == 'MOUSEBUTTONDOWN':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if e['meta'].get('gobj', None):
                        if e['meta']['gobj'].type == 'button':
                            if e['meta']['gobj'].rect.collidepoint(event.pos):
                                func(e['meta'])
                    else:
                        func(e['meta'])
            elif event_type == 'MOUSEMOTION':

                if event.type == pygame.MOUSEMOTION:
                    if e['meta'].get('gobj', None):
                        if e['meta']['gobj'].type == 'button':
                            if e['meta']['gobj'].rect.collidepoint(event.pos):
                                e['meta'].update({'is_hover': 1})
                            else:
                                e['meta'].update({'is_hover': 0})
                            func(e['meta'])

    def bind(self, event_type, func, hot_key, meta):
        self.event_ls.append({'event_type':event_type, 'func': func, 'hot_key': hot_key, 'meta': meta})

def update_obj_img(gobj, anime_name):
    anime_img_ls = gobj.anime_dict[anime_name]['anime_img_ls']
    gobj.image = pygame.image.load(anime_img_ls[gobj.anime_dict[anime_name]['anime_number']])

def update_anime(gobj, anime_name):
    update_obj_img(gobj, anime_name)

    if gobj.anime_dict[anime_name]['anime_number'] < gobj.anime_dict[anime_name]['anime_length'] - 1:

        gobj.anime_dict[anime_name]['anime_number'] += 1
    else:
        gobj.anime_dict[anime_name]['anime_number'] = 0

def anime_roll_back(gobj, anime_name):
    '''
    动画归位
    '''
    gobj.anime_dict[anime_name]['anime_number'] = 0
    update_obj_img(gobj, anime_name)

def switch_action_kvls(gobj, action_switch_kvls, switch_type="&&"):
    switch_ls = []
    for action_kv in action_switch_kvls:
        action_name = action_kv[0]
        action_value = action_kv[1]
        if gobj.action_controller[action_name]['action_value'] == action_value:
            switch_ls.append(True)
        else:
            switch_ls.append(False)
    if switch_type == "&&":
        if False not in switch_ls:
            return True
    elif switch_type == "||":
        if True in switch_ls:
            return True
    return False

class UpdateController:

    def __init__(self):
        self.anime_ls = []
        self.character_ls = []
        self.collision_group = Group()
        self.delay_ls = []

    def update_action(self):
        '''
        更新动作和动画
        '''
        for delay_event in self.delay_ls:
            func_obj_ls = delay_event['func_obj_ls']
            for func_obj in func_obj_ls:
                if func_obj.is_invalid:
                    del func_obj_ls[func_obj_ls.index(func_obj)]
                elif func_obj.is_active:
                    func_obj.run(delay_event)
                    break
                else:
                    func_obj.is_active = True
                    break # 防止一次性激活多个任务
        for c in self.character_ls:
            func = c['func']
            action_name = c['action_name']
            action_switch_kvls = c['action_switch_kvls']
            gobj = c['gobj']
            if switch_action_kvls(gobj, action_switch_kvls):
                func(c)
        for u in self.anime_ls:
            gobj = u['self']
            anime_name = u['anime_name']
            action_switch_kvls = gobj.anime_dict[anime_name]['action_switch_kvls']
            switch_type = u['switch_type']
            if switch_action_kvls(gobj, action_switch_kvls, switch_type):
                update_anime(gobj, anime_name)



    def bind_u(self, update_type, **meta):
        if update_type == 'anime_play':
            item = {
                'self': meta['obj'],
                'anime_name_path': meta['anime_name_path'],
                'anime_number_range' : meta['anime_number_range'],
                'action_switch_kvls': meta['action_switch_kvls'],
                'switch_type': meta['switch_type'],
                'anime_name': meta['anime_name'],
                'type': 'anime_play',
            }
            self.anime_ls.append(item)
        elif update_type == 'character_event':
            item = {
                'func': meta['func'],
                'action_name': meta['action_name'],
                'action_switch_kvls': meta['action_switch_kvls'],
                'gobj': meta['gobj'],
                'switch_type': meta['switch_type'],
                'scene': meta['scene'],
                'meta': meta['meta']
            }
            self.character_ls.append(item)
        elif update_type == 'collision':
            item = {
                'collision_obj': meta['collision_obj']
            }
            self.collision_group.add(item['collision_obj'])
        elif update_type == 'delay_event':
            item = {
                'func_obj_ls': meta['func_obj_ls']
            }
            self.delay_ls .append(item)