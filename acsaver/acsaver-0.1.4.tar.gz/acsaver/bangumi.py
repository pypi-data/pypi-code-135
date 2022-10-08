# coding=utf-8
from .utils import os, SaverBase

__author__ = 'dolacmeo'


class BangumiSaver(SaverBase):

    def __init__(self, acer, ac_obj):
        self.acer = acer
        self.ac_obj = ac_obj
        super().__init__(acer, ac_obj)

    @property
    def episode_list(self):
        return self.ac_obj.bangumi_list.get("items", [])

    def save_all(self):
        self.tasks.append((self.ac_obj.cover_image('v'), os.path.join(self._save_path, 'coverV._')))
        self._save_raw()
        self._save_image()
        self._gen_html()
        for n in range(len(self.episode_list)):
            self._save_video(n)
            self._save_danmaku(n)
        self._save_comment()
        self.update_js_data()
