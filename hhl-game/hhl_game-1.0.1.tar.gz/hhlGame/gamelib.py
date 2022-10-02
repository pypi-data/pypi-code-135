import sys
import pygame
from collections import defaultdict
from .gamescene import Scene


class Game:

    def __init__(self, title: str, size: tuple[int, int], icon_path: str = None, fps=60):
        """
        初始化
        :param size: 窗口大小
        :param title: 窗口标题
        :param icon_path: 窗口图标路径
        """
        pygame.init()
        pygame.mixer.init()
        self.size = size
        self.main_scene = Scene('default_scene', size, (255, 255, 255))
        self.scene_dict = defaultdict()
        pygame.display.set_caption(title)
        if icon_path:
            img = pygame.image.load(icon_path)
            pygame.display.set_icon(img)

        self.fps = fps
        self.sound_dict = defaultdict()

    def create_scene(self, scene_name, bg_color: tuple[int, int, int] = (255, 255, 255)):
        self.scene_dict[scene_name] = Scene(scene_name, self.size, bg_color)

    def load_scene(self, scene_name):
        self.main_scene = self.scene_dict[scene_name]

    def run(self):

        fps_clock = pygame.time.Clock()
        while True:
            self.main_scene.fill()

            pygame.display.flip()
            fps_clock.tick(self.fps)

    def __getitem__(self, key) -> Scene:
        return self.scene_dict[key]

    def play_background_music(self, music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def add_sound(self, sound_name, sound_file_path):
        self.sound_dict[sound_name] = pygame.mixer.Sound(sound_file_path)

    def play_sound(self, sound_name):
        self.sound_dict[sound_name].play()

    def stop_sound(self, sound_name):
        self.sound_dict[sound_name].stop()


