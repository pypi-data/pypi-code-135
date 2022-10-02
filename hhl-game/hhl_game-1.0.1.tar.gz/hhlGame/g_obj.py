from .gametools import GameFun
from .gameeventloop import EventController, UpdateController
import pygame

class Rect:

    def __init__(self, img_path: str, size: tuple[int, int], position_for_obj: tuple[int, int], event_controller, update_controller):
        """
        方块对象
        :param img_path: 图片路径
        """
        self.type = 'rect'
        self.img_path = img_path
        self.size = size
        self.position_for_obj = position_for_obj
        self.image = pygame.image.load(self.img_path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

        self.event_controller = event_controller
        self.update_controller = update_controller


class Font:

    def __init__(self, text: str, font_size: int,  color: tuple[int, int, int], position_for_obj: tuple[int, int], event_controller, update_controller):
        """
        文本对象
        :param text: 文本内容
        :param color: 文本颜色
        :param font_size: 文字大小
        """
        self.type = 'font'
        self.font_size = font_size
        self.text = text
        self.color = color
        self.position_for_obj = position_for_obj
        f = pygame.font.Font('C:/Windows/Fonts/RAVIE.TTF', self.font_size)
        self.text = f.render(self.text, True, self.color)
        self.rect = self.text.get_rect()

        self.event_controller = event_controller
        self.update_controller = update_controller

class Button:

    def __init__(self,
                 text: str,
                 font_size: int,
                 color: tuple[int, int, int],
                 position_for_obj: tuple[int, int],
                 bg_color: tuple[int, int, int],
                 event_controller: EventController,
                 update_controller: UpdateController,
                 hover_color: tuple[int, int, int],
                 hover_bg_color: tuple[int, int, int],
                 font_style: str):
        """
        文本对象
        :param text: 文本内容
        :param color: 文本颜色
        :param font_size: 文字大小
        """
        self.type = 'button'
        self.font_size = font_size
        self.txt = text
        self.color = color
        self.position_for_obj = position_for_obj
        self.bg_color = bg_color

        self.f = pygame.font.Font(font_style, self.font_size)
        self.text = self.f.render(self.txt, True, self.color, self.bg_color)
        self.rect = self.text.get_rect()

        self.event_controller = event_controller
        self.update_controller = update_controller

        self.hover_color = hover_color
        self.hover_bg_color = hover_bg_color

        self.event_controller.bind('MOUSEMOTION', self.mouse_hover, None, {'gobj':self, 'is_hover':0})

    def mouse_hover(self, meta):
        if meta['is_hover'] == 1:
            self.text = self.f.render(self.txt, True, self.hover_color, self.hover_bg_color)
        else:
            self.text = self.f.render(self.txt, True, self.color, self.bg_color)

    def bind(self, func):
        self.event_controller.bind('MOUSEBUTTONDOWN', func, meta={'gobj':self}, hot_key=None)

class TextRender:

    def __init__(self, size, position_for_obj, scene, event_controller:EventController, update_controller:UpdateController):
        self.type = 'text_render'
        self.position_for_obj = position_for_obj
        self.textbox_surf = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.textbox_surf.get_rect(topleft=(150, 200))
        self.border_rect = self.textbox_surf.get_rect(topleft=(0, 0))
        self.FONT = pygame.font.SysFont('SimSun', 24, 0)
        self.event_controller = event_controller
        self.update_controller = update_controller
        self.scene = scene
        self.is_show = False
        self.is_play = True
        self.cur = 0
        self.txt_ls = []

    def play(self, txt):
        rendering = ''
        self.scene.screen.blit(self.textbox_surf, self.rect)
        for char in txt:
            pygame.time.delay(15)
            rendering = rendering + char
            rendered_text = self.FONT.render(rendering, 1, 'White')
            text_rect = rendered_text.get_rect(topleft=(20, 90))
            self.textbox_surf.fill((0, 0, 20, 100))
            pygame.draw.rect(self.textbox_surf, "Black", self.border_rect, 6)
            self.textbox_surf.blit(rendered_text, text_rect)
            self.scene.screen.blit(self.textbox_surf, self.rect)
            pygame.display.update()
        self.is_play = False

    def change_txt(self, txt:str):
        self.scene.main_txt = txt

    def show(self):
        self.is_show = True

    def hidden(self):
        self.is_show = False

    def add_txt_ls(self, txt_ls: list[str]):
        self.txt_ls = txt_ls
        self.scene.main_txt = self.txt_ls[self.cur]

class MusicPlayer:

    def __init__(self):
        pass
