# coding=utf-8
import os.path
from dataclasses import dataclass
from acfunsdk.source import AcSource

__author__ = 'dolacmeo'


@dataclass(frozen=True)
class SaverData:
    github_assets_map_url = "https://raw.githubusercontent.com/dolaCmeo/acsaver/assets/assets.map"
    github_assets_zip_url = "https://raw.githubusercontent.com/dolaCmeo/acsaver/assets/assets.zip"
    github_assets_base = "https://raw.githubusercontent.com/dolaCmeo/acsaver/assets/"
    github_booster = (
        "raw.fastgit.org",
        # "raw.githubusercontents.com",
        "raw.staticdn.net",
        "raw.iqiq.io"
    )
    folder_names = ['bangumi', 'article', 'video', 'live', 'member', 'moment']
    emot_alias = ['default', 'ac', 'ac2', 'ac3', 'dog', 'tsj', 'brd', 'ais', 'td', 'zuohe', 'blizzard']
    ac_name_map = {
        "AcArticle": "article",
        "AcMoment": "moment",
        "AcVideo": "video",
        "AcBangumi": "bangumi",
        "AcLiveUp": "live",
        "AcUp": "member"
    }
    ac_saver_map = {
        "AcBangumi": "BangumiSaver",
        "AcArticle": "ArticleSaver",
        "AcVideo": "VideoSaver",
        "AcUp": "MemberSaver",
        "AcMoment": "MomentSaver",
        "AcLiveUp": "LiveSaver",
    }
    rtype_name_map = {
        "1": "番剧",  # bangumi
        "2": "视频",  # video
        "3": "文章",  # article
        "4": "合辑",  # album
        "5": "用户",  # member
        "6": "评论",  # comment
        # "8": "私信",
        "10": "动态",  # moment
    }
    ubb_tag_basic = {
        r"\r\n": "<br>",
        "[b]": "<b>", "[/b]": "</b>",
        "[i]": "<i>", "[/i]": "</i>",
        "[u]": "<u>", "[/u]": "</u>",
        "[s]": "<s>", "[/s]": "</s>",
        "[/color]": r"</color>"
    }
    ubb_tag_rex = {
        "color": r"(\[color=(#[a-f0-9]{6})\])",
        "size": r"(\[size=(\d+px)\]([^\[]+)\[/size\])",
        "emot": r"(\[emot=acfun,(\S+?)\/])",
        "emot_old": r"(\[emot=([a-z0-9]+),(\S+?)\/])",
        "image": r"(\[img=\\u56fe\\u7247\]([^\[]*)\[\/img\])",
        "at": r"(\[at uid=(\d+)\](@[^\[]+)\[/at\])",
        "at_old": r"(\[at\]([^\[]+)\[/at\])",
        "resource": r"(\[resource id=(\d+) type=([1-5]) icon=[^\]]*\]([^\[]*)\[\/resource\])",
        "jump": r"(\[time duration=(\d+)\]([^\[]+)\[/time\])",
    }
    ubb_resource_url = {
        "1": AcSource.routes['bangumi'],
        "2": AcSource.routes['video'],
        "3": AcSource.routes['article'],
        "4": AcSource.routes['album'],
        "5": AcSource.routes['up']
    }
    ubb_resource_icon = {
        "1": r'<img class=\"ubb-icon\" src=\"../../assets/img/icon_comment_video_pc.png\">',
        "2": r'<img class=\"ubb-icon\" src=\"../../assets/img/icon_comment_pc_vid_18_3.png\">',
        "3": r'<img class=\"ubb-icon\" src=\"../../assets/img/icon_popup_article_pc.png\">',
        "4": r'<img class=\"ubb-icon\" src=\"../../assets/img/icon_comment_heji_pc.png\">',
        "5": r'<img class=\"ubb-icon\" src=\"../../assets/img/icon_comment_human_pc.png\">',
    }
    cmd_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "__main__.py")
