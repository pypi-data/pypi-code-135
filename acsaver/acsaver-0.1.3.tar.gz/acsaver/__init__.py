# coding=utf-8
from .bangumi import BangumiSaver
from .video import VideoSaver
from .article import ArticleSaver
from .moment import MomentSaver
from .live import LiveSaver
from .utils import os, json, zipfile, SaverData, downloader, \
    saver_template, update_js_data, create_http_server_bat, live_recorder

__author__ = 'dolacmeo'
__all__ = (
    "AcSaver",
    "SaverLocal"
)


class AcSaver:

    def __init__(self, acer, root_path: [os.PathLike, str, None] = None):
        self.acer = acer
        if root_path is None:
            root_path = os.getcwd()
        elif not os.path.exists(root_path):
            os.makedirs(root_path, exist_ok=True)
        self.acer.config.update({"SaverRootPath": root_path})
        self.local = SaverLocal(self.acer, root_path)
        self.loading()

    def loading(self):
        update_js_data(self.local.root_path)

    def BangumiSaver(self, ac_obj):
        return BangumiSaver(self.acer, ac_obj)

    def VideoSaver(self, ac_obj):
        return VideoSaver(self.acer, ac_obj)

    def ArticleSaver(self, ac_obj):
        return ArticleSaver(self.acer, ac_obj)

    def MomentSaver(self, ac_obj):
        return MomentSaver(self.acer, ac_obj)

    def LiveSaver(self, ac_obj):
        return LiveSaver(self.acer, ac_obj)

    def get_saver(self, ac_obj):
        s = SaverData.ac_saver_map.get(ac_obj.__class__.__name__)
        if s is None:
            return None
        return getattr(self, s)(ac_obj)

    def resource(self, rtype: int, rid: int):
        obj = self.acer.acfun.resource(rtype, rid)
        if obj is None:
            return None
        return self.get_saver(obj)

    def get(self, url_str: str):
        obj = self.acer.get(url_str)
        if obj is None:
            return None
        return self.get_saver(obj)


class SaverLocal:
    root_path = None
    __assets_check_times = 0

    def __init__(self, acer, root_path: [os.PathLike, str]):
        self.acer = acer
        self.root_path = root_path
        self.loading()

    def history(self):
        saver_data_path = os.path.join(self.root_path, "data.js")
        if os.path.isfile(saver_data_path) is False:
            return None
        with open(saver_data_path, 'r') as js_string:
            saver_data = json.loads(js_string.read()[12:-1])  # let AcSaver=.....;
        return saver_data

    def loading(self):
        self._folder_check()
        self._assets_check()
        self._page_check()
        create_http_server_bat(self.root_path)
        pass

    def _folder_check(self):
        # 必要目录检查
        done_mark = list()
        for x in SaverData.folder_names:
            f = os.path.join(self.root_path, x)
            os.makedirs(f, exist_ok=True)
            done_mark.append(os.path.isdir(f))
        return all(done_mark)

    def _assets_check(self):
        self.__assets_check_times += 1
        # 检查静态文件目录
        os.makedirs(os.path.join(self.root_path, "assets"), exist_ok=True)
        # 查找静态文件map
        assets_map_path = os.path.join(self.root_path, "assets.map")
        if os.path.isfile(assets_map_path) is False:
            # 如map不存在，认为静态文件缺失
            task = (SaverData.github_assets_map_url, assets_map_path)
            # 优先获取完整的map文件
            downloader(self.acer.client, [task], display=True)
            pass
        assert os.path.isfile(assets_map_path) is True
        # 读取map文件，进行本地文件校验
        assets_map_file = open(assets_map_path, 'rb')
        assets_map_data = assets_map_file.read().decode().split("\n")
        missing_assets = list()
        for x in assets_map_data:
            if not os.path.exists(os.path.join(self.root_path, x)):
                missing_assets.append(x)
        assets_map_file.close()
        # 如未通过校验，缺失少于10个
        if len(missing_assets) > 0:
            if len(missing_assets) <= 10:
                # 逐个将丢失文件重新下载
                tasks = list()
                for item in missing_assets:
                    url_end = item.replace('\\', '/')
                    tasks.append((f"{SaverData.github_assets_base}{url_end}",
                                  os.path.join(self.root_path, item)))
                downloader(self.acer.client, tasks)
            else:
                # 下载完整压缩包，覆盖解压处理
                assert_zip_path = os.path.join(self.root_path, "assets.zip")
                if not os.path.isfile(assert_zip_path):
                    downloader(self.acer.client, [(SaverData.github_assets_zip_url, assert_zip_path)], display=True)
                zip_file = zipfile.ZipFile(assert_zip_path)
                zip_file.extractall(self.root_path)
            # 循环调用检查，并计数，最大次数3次后报错
            if self.__assets_check_times > 3:
                raise FileNotFoundError("Assets Files Check MaxTried.")
            return self._assets_check()
        return True

    def _page_check(self):
        index_names = [
            ['index', '内容', 'https://www.acfun.cn/'],
            ['anime', '番剧', 'https://www.acfun.cn/bangumilist'],
            ['feed', '动态', 'https://www.acfun.cn/member/feeds'],
            # 直播
        ]
        for page, title, referer in index_names:
            index_html_path = os.path.join(self.root_path, f'{page}.html')
            if os.path.isfile(index_html_path) is False:
                templates = saver_template()
                index_html = templates.get_template(f'{page}.html').render(
                    main=dict(zip(["name", "title", "referer"], [page, title, referer])))
                with open(index_html_path, 'wb') as index_file:
                    index_file.write(index_html.encode())
        return True
