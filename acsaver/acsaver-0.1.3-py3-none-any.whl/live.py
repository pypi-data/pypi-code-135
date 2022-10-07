# coding=utf-8
from .utils import os, SaverBase, SaverData, url_saver, json_saver, json2js, downloader

__author__ = 'dolacmeo'


class LiveSaver(SaverBase):

    def __init__(self, acer, ac_obj):
        self.acer = acer
        self.ac_obj = ac_obj
        super().__init__(acer, ac_obj)

    @property
    def begin_time(self):
        if self.ac_obj.past_time > 0:
            return self.ac_obj.live.start_time.replace("-", "").replace(":", "").replace(" ", "")
        return None

    @property
    def save_dir(self):
        return os.path.join(self._save_path, self.begin_time)

    def live_raw_save(self):
        if self.ac_obj.past_time == -1:
            return False
        os.makedirs(self.save_dir, exist_ok=True)
        url_name = f"{self.ac_obj.live.raw_data.get('caption', '@'+self.ac_obj.username)}"
        url_saved = url_saver(self.ac_obj.referer, self.save_dir, url_name)
        raw_saved = json_saver(self.ac_obj.live.raw_data, self.save_dir, f"{self.begin_time}")
        json2js(os.path.join(self.save_dir, f"{self.begin_time}.json"),
                f"LOADED.live['{self.ac_obj.uid}_{self.begin_time}']")
        downloader(self.acer.client, [(self.ac_obj.cover, os.path.join(self.save_dir, 'cover._'))])
        return all([url_saved, raw_saved])

    def loading(self):
        assert self.ac_obj.__class__.__name__ in SaverData.ac_name_map.keys()
        self.keyname = SaverData.ac_name_map[self.ac_obj.__class__.__name__]
        self._save_root = self.acer.config.get("SaverRootPath", os.getcwd())
        self._save_path = os.path.join(self._save_root, self.keyname, str(self.ac_obj.uid))
        os.makedirs(self._save_path, exist_ok=True)

    def _save_raw(self):
        url_name = f"@{self.ac_obj.raw_data['user']['name']}"
        url_saved = url_saver(self.ac_obj.referer, self._save_path, url_name)
        self.tasks.extend([
            (self.ac_obj.qrcode, os.path.join(self._save_path, 'share_qrcode.png')),
            (self.ac_obj.mobile_qrcode, os.path.join(self._save_path, 'mobile_qrcode.png'))
        ])
        downloader(self.acer.client, self.tasks)
        self.tasks = list()
        self._save_member([self.ac_obj.uid])
        return url_saved

    def save_all(self):
        self._save_raw()
        self.live_raw_save()
        if self.ac_obj.past_time > 0:
            self._record_live()
        else:
            print(f"Live is CLOSED.")
        # 记录弹幕
        # 保存直播信息
        # self.update_js_data()
