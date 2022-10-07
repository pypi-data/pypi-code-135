# coding=utf-8
from .utils import os, SaverBase

__author__ = 'dolacmeo'


class VideoSaver(SaverBase):

    def __init__(self, acer, ac_obj):
        self.acer = acer
        self.ac_obj = ac_obj
        super().__init__(acer, ac_obj)

    @property
    def video_list(self):
        return self.ac_obj.video_list

    def save_all(self):
        self._save_raw()
        self._save_image()
        self._gen_html()
        for n in range(len(self.video_list)):
            self._save_video(n)
            self._save_danmaku(n)
        self._save_comment()
        self.update_js_data()
