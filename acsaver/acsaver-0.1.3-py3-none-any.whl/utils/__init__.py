# coding=utf-8
from .utils import *

__author__ = 'dolacmeo'


class SaverBase:
    ac_obj = None
    keyname = None
    _save_root = None
    _save_path = None
    tasks = list()

    def __init__(self, acer, ac_obj):
        self.acer = acer
        self.ac_obj = ac_obj
        self.templates = saver_template()
        self.loading()

    @property
    def _objname(self):
        return self.__class__.__name__

    @property
    def _data_path(self):
        p = os.path.join(self._save_path, 'data')
        os.makedirs(p, exist_ok=True)
        return p

    @property
    def _img_path(self):
        p = os.path.join(self._save_path, 'img')
        os.makedirs(p, exist_ok=True)
        return p

    @property
    def rtype(self):
        return self.ac_obj.resource_type

    @property
    def rid(self):
        return self.ac_obj.resource_id

    @property
    def page_data(self):
        data = {"rType": self.rtype, "rId": self.rid, "objName": self._objname, "keyName": self.keyname}
        return json.dumps(data, separators=(',', ':'))

    @property
    def page_template(self):
        return self.templates.get_template(f"{self.keyname}.html")

    @property
    def comment_count(self):
        if self.rtype in [2, 3, 10]:
            return self.ac_obj.raw_data.get("commentCount", 0)
        elif self.rtype in [1]:
            return self.ac_obj.raw_data.get("data", {}).get("commentCount", 0)
        return 0

    def loading(self):
        assert self.ac_obj.__class__.__name__ in SaverData.ac_name_map.keys()
        self.keyname = SaverData.ac_name_map[self.ac_obj.__class__.__name__]
        self._save_root = self.acer.config.get("SaverRootPath", os.getcwd())
        self._save_path = os.path.join(self._save_root, self.keyname, str(self.rid))
        os.makedirs(self._save_path, exist_ok=True)
        pass

    def _save_raw(self):
        url_name = f"{self.ac_obj.title}"
        if self.rtype == 10:
            url_name = f"@{self.ac_obj.raw_data['user']['name']}"
        url_saved = url_saver(self.ac_obj.referer, self._save_path, url_name)
        raw_saved = json_saver(self.ac_obj.raw_data, self._data_path, f"{self.ac_obj.resource_id}")
        json2js(os.path.join(self._data_path, f"{self.rid}.json"), f"LOADED.{self.keyname}['{self.rid}']")
        if self.rtype not in [1]:
            self._save_member([self.ac_obj.up().uid])
        return all([url_saved, raw_saved])

    def _save_image(self):
        img_task = [
            (self.ac_obj.cover, os.path.join(self._save_path, 'cover._')),
            (self.ac_obj.qrcode, os.path.join(self._data_path, 'share_qrcode.png'))
        ]
        if self.keyname in ['video']:
            img_task.append((self.ac_obj.mobile_qrcode, os.path.join(self._data_path, 'mobile_qrcode.png')))
        self.tasks.extend(img_task)
        t = downloader(self.acer.client, self.tasks, display=True)
        self.tasks = list()
        return t

    def _part_video_name(self, num: int):
        assert self.keyname in ['video', 'bangumi']
        ends = "" if num == 0 else f"_{num + 1}"
        if self.keyname == 'bangumi':
            this_episode = self.ac_obj.episode_data[num]
            item_id = this_episode['itemId']
            vid = this_episode['videoId']
            ends = "" if num == 0 else f"_36188_{item_id}"
        return f"{self.rid}{ends}"

    def _gen_html(self) -> bool:
        page_html = self.page_template.render(dict(saver=self))
        html_path = os.path.join(self._save_path, f"{self.rid}.html")
        with open(html_path, 'wb') as html_file:
            html_file.write(page_html.encode())
        return os.path.isfile(html_path)

    def _save_video(self, num: int = 0, quality: [int, str] = 0):
        this_video = self.ac_obj.video(num)
        m3u8_url = this_video.m3u8_url(quality, False)
        vname = self._part_video_name(num)
        json_saver(this_video.raw_data, self._data_path, f"{vname}.video.json")
        scenes_data = this_video.scenes
        if isinstance(scenes_data, dict):
            json_saver(scenes_data, self._data_path, f"{vname}.scenes.json")
            scenes_to_thumbnails(self._save_path, vname)
        else:
            ffmpeg_gen_thumbnails(self._save_path, vname)
        hotspot_data = this_video.hotspot
        if isinstance(hotspot_data, dict):
            json_saver(hotspot_data, self._data_path, f"{vname}.hotspot.json")
        save_path = os.path.join(self._save_path, f"{vname}.mp4")
        if os.path.isfile(save_path):
            return True
        download_ok = m3u8_downloader(m3u8_url[0], save_path)
        retry_count = 0
        while download_ok is False and retry_count < 10:
            u = m3u8_url[1][retry_count % len(m3u8_url[1])]
            retry_count += 1
            download_ok = m3u8_downloader(u, save_path)
        return True

    def _record_live(self, quality: [int, str] = -1):
        live = self.ac_obj.live
        if live is None:
            return False
        if quality in [-1, "-1"]:
            quality = len(live.representation) - 1
        cmd_with_progress = [
            "start", "cmd", "/q", "/k",
            f"chcp 65001 && mode con cols=49 lines=4 && title AcLive({live.uid}) &&",
            "python", SaverData.cmd_path, "live_recorder",
            "--args",
            f"{self.ac_obj.referer}",
            f"{self._save_path}",
            f"{quality}"
        ]
        subprocess.Popen(cmd_with_progress, shell=True)

    def _save_danmaku(self, num: int = 0, quality: [int, str] = "1080p"):
        this_video = self.ac_obj.video(num)
        vname = self._part_video_name(num)
        json_saver(this_video.danmaku.danmaku_data, self._data_path, f"{vname}.danmaku.json")
        json2js(os.path.join(self._data_path, f"{vname}.danmaku.json"), f"LOADED.danmaku['{vname}']")
        ass_req = danmaku2ass(self._save_path, vname, quality)
        player_req = danmaku2dplayer(self._save_path, vname)
        return all([ass_req, player_req])

    def _save_comment(self, update: bool = False, with_user_data: bool = False):
        local_comment_data, local_comment_floors = None, []
        comment_json_path = os.path.join(self._data_path, f"{self.rid}.comment.json")
        comment_json_path_saved = os.path.isfile(comment_json_path)
        if comment_json_path_saved:
            local_comment_data = json.load(open(comment_json_path, 'rb'))
            local_comment_floors = [x['floor'] for x in local_comment_data['rootComments']]
        if update is True or comment_json_path_saved is False:
            comment_obj = self.ac_obj.comment()
            if self.comment_count < 1000:
                comment_obj.get_all_comments()
            else:
                comment_obj.get_all_comments(3)
            if local_comment_data is not None:
                comment_data = local_comment_data
                comment_data['hotComments'] = comment_obj.hot_comments
                comment_data['rootComments'].extend(
                    [c for c in comment_obj.root_comments if c['floor'] not in local_comment_floors])
                comment_data['subCommentsMap'].update(comment_obj.sub_comments)
                comment_data['save_unix'] = time.time()
            else:
                comment_data = {
                    "hotComments": comment_obj.hot_comments,
                    "rootComments": comment_obj.root_comments,
                    "subCommentsMap": comment_obj.sub_comments,
                    "save_unix": time.time()
                }
            uids = list()
            for c in comment_data['rootComments']:
                if c['userId'] not in uids:
                    uids.append(c['userId'])
            for _, i in comment_data['subCommentsMap'].items():
                for j in i['subComments']:
                    if j['userId'] not in uids:
                        uids.append(j['userId'])
            json_saver(comment_data, self._data_path, f"{self.rid}.comment.json")
            if with_user_data is True:
                self._save_member(uids)
        img_task = tans_comment_uub2html(self._save_path)
        if len(img_task) > 0:
            os.makedirs(os.path.join(self._save_path, 'img'), exist_ok=True)
            downloader(self.acer.client, img_task, display=True)
        return True

    def _save_member(self, ids: list, force: bool = False):
        if len(ids) == 0:
            return []
        done = list()
        member_dir = os.path.join(self._save_root, 'member')
        saved = os.listdir(member_dir)
        ids = sorted(list(set(ids)))
        ids_with_ext = [f"{i}.json" for i in ids]
        ids = list(set(ids_with_ext).difference([x for x in saved if x.endswith('.json')]))
        ids = [y.split('.')[0] for y in ids]
        avatar_task = list()
        with Progress(disable=len(ids) <= 5) as pp:
            get_member = pp.add_task("save members", total=len(ids))
            for uid in ids:
                if all([f"{uid}.json" in saved, f"{uid}.js" in saved, f"{uid}_avatar" in saved]) is True \
                        and force is False:
                    pp.update(get_member, advance=1)
                    done.append(uid)
                    continue
                user_req = self.acer.client.get(AcSource.apis['userInfo'], params=dict(userId=uid))
                user_data = user_req.json()
                profile = user_data.get('profile')
                user_json = os.path.join(member_dir, f"{uid}.json")
                user_js = os.path.join(member_dir, f"{uid}.js")
                user_avatar = os.path.join(member_dir, f"{uid}_avatar")
                if all([os.path.isfile(user_json), os.path.isfile(user_js), os.path.isfile(user_avatar)]) is True \
                        and force is False:
                    pp.update(get_member, advance=1)
                    done.append(uid)
                    continue
                with open(user_json, 'w') as uid_file:
                    json.dump(profile, uid_file, separators=(',', ':'))
                user_json_saved = os.path.isfile(user_json)
                user_json_string = open(os.path.join(user_json), 'rb').read().decode()
                with open(user_js, 'wb') as js_file:
                    user_js_string = f"let user_{uid}={user_json_string};"
                    js_file.write(user_js_string.encode())
                user_js_saved = os.path.isfile(user_js)
                avatar = parse.urlparse(profile['headUrl'])
                if not avatar.path.endswith('defaultAvatar.jpg'):
                    avatar_url = f"{avatar.scheme}://{avatar.netloc}{avatar.path}"
                    avatar_task.append((avatar_url, user_avatar))
                if all([user_json_saved, user_js_saved]):
                    done.append(uid)
                pp.update(get_member, advance=1)
                time.sleep(0.1)
            pp.update(get_member, completed=len(ids))
            pp.stop()
        if len(avatar_task) > 0:
            downloader(self.acer.client, avatar_task, display=True)
        return done

    def update_js_data(self):
        return update_js_data(self._save_root)
