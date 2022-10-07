# coding=utf-8
import os
import re
import math
import time
import json
import httpx
import shutil
import random
import zipfile
import filetype
import subprocess
from urllib import parse
from PIL import Image
from bs4 import BeautifulSoup as Bs
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.live import Live
from rich.progress import Progress
from jinja2 import PackageLoader, Environment
from acfunsdk.source import AcSource
from .ffmpeg_progress_yield import FfmpegProgress
from .source import SaverData

__author__ = 'dolacmeo'
__all__ = (
    "os",
    "time",
    "json",
    "parse",
    "zipfile",
    "subprocess",
    "Console",
    "Text",
    "Align",
    "Panel",
    "Live",
    "Progress",
    "Bs",
    "AcSource",
    "SaverData",
    "FfmpegProgress",
    "saver_template",
    "sizeof_fmt",
    "unix2datestr",
    "url_saver",
    "json_saver",
    "json2js",
    "downloader",
    "m3u8_downloader",
    "ffmpeg_gen_thumbnails",
    "scenes_to_thumbnails",
    "danmaku2dplayer",
    "danmaku2ass",
    "get_usable_ffmpeg",
    "tans_uub2html",
    "tans_comment_uub2html",
    "live_recorder",
    "update_js_data",
    "create_http_server_bat"
)


def clean_file_name(filename:str):
    invalid_chars='[\\\/:*?"<>|]'
    replace_char='-'
    return re.sub(invalid_chars,replace_char,filename)


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Yi{suffix}"


def unix2datestr(t: (int, float, None) = None, f: str = "%Y-%m-%d %H:%M:%S"):
    if t is None:
        return time.strftime(f, time.localtime(time.time()))
    t = int(t)
    n = int(math.log10(t)) + 1
    if n > 10:
        t = t // math.pow(10, n - 10)
    elif n < 10:
        t = t * math.pow(10, 10 - n)
    return time.strftime(f, time.localtime(t))


def url_saver(url: str, base_path: [os.PathLike, str], filename: str):
    file_path = os.path.join(base_path, clean_file_name(filename))
    if not file_path.endswith(".url"):
        file_path = f"{file_path}.url"
    raw_data = f"[InternetShortcut]\nURL={url}\n"
    with open(file_path, 'wb') as url_file:
        url_file.write(raw_data.encode())
    result = os.path.isfile(file_path)
    return result


def json2js(src_path: [os.PathLike, str], keyname: str, dest_path: [str, None] = None):
    data = json.load(open(src_path, 'r'))
    if "moment" in src_path:
        text = tans_uub2html(data['text'], os.path.dirname(os.path.dirname(src_path)))
        data['text'] = text[0].replace(r"\"", '"').replace('emot/big', 'emot/small')

    str_data = json.dumps(data, separators=(',', ':'))
    data_js = f"{keyname}={str_data};"
    if dest_path is None:
        if src_path.endswith(".json"):
            dest_path = src_path[:-2]
        else:
            dest_path = os.path.join(os.path.dirname(src_path), f"{keyname}.js")
    with open(dest_path, 'wb') as js:
        js.write(data_js.encode())
    return os.path.isfile(dest_path)


def json_saver(data: dict, base_path: [os.PathLike, str], filename: str):
    file_path = os.path.join(base_path, filename)
    if not file_path.endswith(".json"):
        file_path = f"{file_path}.json"
    json_string = json.dumps(data, separators=(',', ':'))
    with open(file_path, 'wb') as json_file:
        json_file.write(json_string.encode())
    result = os.path.isfile(file_path)
    return result


def ffmpeg_gen_thumbnails(base_path: [os.PathLike, str], filename: str):
    media_path = os.path.join(base_path, f"{filename}.mp4")
    thumbnails_path = os.path.join(base_path, "data", f"{filename}.thumbnails.png")
    if os.path.isfile(thumbnails_path) is True:
        return True
    ffprobe_params = [
        "ffprobe", "-v", "error", "-show_entries", "stream=width,height,duration",
        "-of", "default=noprint_wrappers=1", "-print_format", "json", media_path
    ]
    p = subprocess.Popen(ffprobe_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    media_info = json.loads(p.stdout.read()).get("streams", [None])[0]
    w, h, d = media_info['width'], media_info['height'], media_info['duration']
    scale = "160:90" if w > h else "90:160"
    ffmpeg_cmd = get_usable_ffmpeg()
    ffmpeg_params = [
        ffmpeg_cmd, '-y', '-i', media_path, '-vsync', 'vfr', '-vf',
        f'fps=1/{float(d) / 100},scale={scale},tile=100x1',
        '-qscale:v', '3', thumbnails_path,
        # "-v", "quiet"
    ]
    # print(f"{ffmpeg_params=}")
    p = subprocess.Popen(ffmpeg_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.stdout.read()
    return os.path.isfile(thumbnails_path)


def scenes_to_thumbnails(base_path: [os.PathLike, str], filename: str):
    scenes_data_path = os.path.join(base_path, "data", f"{filename}.scenes.json")
    if not os.path.isfile(scenes_data_path):
        return False
    sprite = json.load(open(scenes_data_path, 'r'))
    pos = sprite['pos']
    if len(pos) % 100 != 0:
        if (len(pos) % 100) <= 10:
            pos = pos[:-(len(pos) % 100)]
        else:
            return ffmpeg_gen_thumbnails(base_path, filename)
    img_task = list()
    for i, x in enumerate(sprite['sprite_images']):
        img_task.append([x, os.path.join(base_path, "data", f"{filename}.scenes.{i}.png")])
    downloader(httpx.Client(), img_task, os.path.join(base_path, "data"))
    scenes0 = Image.open(img_task[0][1])
    ww, hh = scenes0.width // 5, scenes0.height // 10
    thumbnails = Image.new('RGB', (ww * 100, hh))
    step = len(pos) // 100
    for i in range(100):
        x, y, w, h = list(map(int, pos[i * step][2].split(',')))
        img = Image.open(img_task[pos[i * step][3]][1])
        region = img.crop((x, y, x + w, y + h))
        thumbnails.paste(region, (ww * i, 0))
    thumbnails_path = os.path.join(base_path, "data", f"{filename}.thumbnails.png")
    thumbnails.save(thumbnails_path, "png")
    return os.path.isfile(thumbnails_path)


def danmaku2dplayer(folder_path: str, filenameId: str):
    # 检查路径
    assert os.path.isdir(folder_path) is True
    danmaku_data_path = os.path.join(folder_path, 'data', f"{filenameId}.danmaku.json")
    assert os.path.isfile(danmaku_data_path) is True
    danmaku_data = json.load(open(danmaku_data_path, 'rb'))
    dplayer_data = dict(code=0, data=list())
    for danmaku in danmaku_data:
        dplayer_data['data'].append([
            round(danmaku['position'] / 1000, 3),
            danmaku['mode'] - 1,
            danmaku['color'],
            f"{danmaku['userId']}",
            danmaku['body']
        ])
    return json_saver(dplayer_data, os.path.join(folder_path, 'data'), f"{filenameId}.dplayer.json")


def danmaku2ass(folder_path: str, filenameId: str, vq: str = "720p", fontsize: int = 40):
    """
    https://github.com/niuchaobo/acfun-helper/blob/master/src/fg/modules/danmaku.js
    基础代码复刻自acfun助手中弹幕相关处理
    关于解决原代码中的弹幕重叠问题：
        0. 原弹幕数据要按时间进行排序
        1. 记录每条弹幕通道最后截止位置
        2. 如果同期所有通道已满，则减少弹幕停留时间(加速通过)

    :param client: acer.client
    :param folder_path: source path
    :param filenameId: ac_num
    :param vq: VideoQuality
    :return: ass file path
    :param fontsize: num px
    """
    # 检查路径
    assert os.path.isdir(folder_path) is True
    folder_name = os.path.basename(folder_path)
    main_json_name = f"{filenameId}.json"
    if "_" in filenameId:
        main_json_name = f"{filenameId.split('_')[0]}.json"
    main_data_path = os.path.join(folder_path, 'data', main_json_name)
    danmaku_data_path = os.path.join(folder_path, 'data', f"{filenameId}.danmaku.json")
    video_data_path = os.path.join(folder_path, 'data', f"{filenameId}.video.json")
    assert all([os.path.isfile(main_data_path), os.path.isfile(danmaku_data_path)]) is True
    main_data = json.load(open(main_data_path, 'rb'))
    danmaku_data = json.load(open(danmaku_data_path, 'rb'))
    video_data = json.load(open(video_data_path, 'rb'))
    ks_data = json.loads(video_data['ksPlayJson'])
    quality_data = None
    for x in ks_data['adaptationSet'][0]['representation']:
        if x['qualityType'] == vq:
            quality_data = x
    if isinstance(quality_data, dict) is False:
        return None
    if len(danmaku_data) == 0:
        return None
    thisVideoInfo = AcSource.videoQualitiesRefer[vq]
    thisVideoWidth = quality_data['width']
    thisVideoHeight = quality_data['height']
    thisDuration = 10
    channelNum = math.floor(thisVideoWidth / fontsize)
    if "dougaId" in main_data:
        scriptInfo = "\n".join([
            "[Script Info]",
            f"; AcVid: {folder_name}",
            f"; StreamName: {main_data['title']}",
            f"Title: {folder_name} - {main_data['user']['name']} - {main_data['title']}",
            f"Original Script: {folder_name} - {main_data['user']['name']} - {main_data['title']}",
            "Script Updated By: acfunSDK转换",
            "ScriptType: v4.00+",
            "Collisions: Normal",
            f"PlayResX: {thisVideoWidth}",
            f"PlayResY: {thisVideoHeight}"
        ])
    elif "bangumiId" in main_data.get("data", {}):
        scriptInfo = "\n".join([
            "[Script Info]",
            f"; AcVid: {folder_name}",
            f"; StreamName: {main_data['data']['bangumiTitle']}",
            f"Title: {folder_name} - {main_data['data']['bangumiTitle']}",
            f"Original Script: {folder_name} - {main_data['data']['bangumiTitle']}",
            "Script Updated By: acfunSDK转换",
            "ScriptType: v4.00+",
            "Collisions: Normal",
            f"PlayResX: {thisVideoWidth}",
            f"PlayResY: {thisVideoHeight}"
        ])
    styles = "\n".join([
        "[V4+ Styles]",
        "Format: " + ", ".join([
            'Name', 'Fontname', 'Fontsize', 'PrimaryColour', 'SecondaryColour', 'OutlineColour',
            'BackColour', 'Bold', 'Italic', 'Underline', 'StrikeOut', 'ScaleX', 'ScaleY',
            'Spacing', 'Angle', 'BorderStyle', 'Outline', 'Shadow', 'Alignment', 'MarginL',
            'MarginR', 'MarginV', 'Encoding']),
        "Style: " + ",".join([
            'Danmu', 'Microsoft YaHei', f'{fontsize}',
            '&H00FFFFFF', '&H00FFFFFF', '&H00000000', '&H00000000',
            '0', '0', '0', '0', '100', '100', '0', '0', '1', '1',
            '0', '2', '20', '20', '2', '0'])
    ])
    events = "\n".join([
        "[Events]",
        "Format: " + ", ".join([
            'Layer', 'Start', 'End', 'Style', 'Name',
            'MarginL', 'MarginR', 'MarginV', 'Effect', 'Text\n'])
    ])
    assData = list()
    screenChannel = [None for i in range(channelNum)]

    def timeProc(second, offset=0):
        second = second + offset
        minute = math.floor(second / 60)
        hours = math.floor(second / 60 / 60)
        minute = minute - hours * 60
        second = second - hours * 60 * 60 - minute * 60
        sec = second + offset
        return f"{hours:0>2}:{minute:0>2}:{sec:0>2.2f}"

    def choice_channel(startT, endT):
        # 按新时间移除频道占位
        empty = []
        for i, thisEnd in enumerate(screenChannel):
            if i in [0, 1]:
                continue
            elif thisEnd is None:
                empty.append(i)
            elif startT > thisEnd:
                screenChannel[i] = None
        # 无空位时返回空
        if len(empty) == 0:
            return None
        # 随机选择空位，记录结束时间，返回结果
        used = random.choice(empty)
        screenChannel[used] = endT
        return used

    for danmaku in danmaku_data:
        # 略过高级弹幕
        if danmaku['danmakuType'] != 0:
            continue
        # 弹幕挂载时间（文本）（弹幕左边界 接触到 视频的右边界）
        startTime = danmaku['position'] / 1000
        # 弹幕的长度
        danmakuLen = len(danmaku['body']) * fontsize
        danmakuLen_total = danmakuLen + thisVideoWidth
        # 运动到出界的时间点
        toLeftTime = startTime + thisDuration + (danmakuLen_total / thisVideoWidth)
        # 寻找频道
        danmaku_channel = choice_channel(startTime, toLeftTime)
        if danmaku_channel is None:  # 频道全满，加速通过
            toLeftTime -= int(thisDuration / 2)
            danmaku_channel = random.randint(2, channelNum)
        channelHeight = danmaku_channel * fontsize
        # 所有点位
        x1 = danmakuLen_total
        y1 = channelHeight
        x2 = - danmakuLen
        y2 = channelHeight
        dialogue = [
            "Dialogue: 0", timeProc(startTime), timeProc(toLeftTime),
            "Danmu", f"{danmaku['userId']}", "20", "20", "2", "",
            "{\\move(" + f"{x1}", f"{y1}", f"{x2}", f"{y2})" + "}" + f"{danmaku['body']}"
        ]
        assData.append(",".join(dialogue))
    events += "\n".join(assData)
    result = "\n\n".join([scriptInfo, styles, events])
    ass_path = os.path.join(folder_path, f"{filenameId}.ass")
    with open(ass_path, 'w', encoding="utf_8_sig") as ass_file:
        ass_file.write(result)
    return os.path.isfile(ass_path)


def get_usable_ffmpeg(cmd: [str, None] = None):
    cmds = ['ffmpeg', os.path.join(os.getcwd(), 'ffmpeg.exe')]
    if cmd is not None and os.path.isfile(cmd):
        cmds = [cmd] + cmds
    for x in cmds:
        try:
            p = subprocess.Popen([x, '-version'], stdin=subprocess.DEVNULL,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            vers = str(out, 'utf-8').split('\n')[0].split()
            assert vers[0] == 'ffmpeg' and vers[2][0] > '0'
            return x
        except FileNotFoundError:
            continue
    return None


def m3u8_downloader(m3u8_url: str, save_path: [str, os.PathLike, None] = None):
    # ffmpeg 下载
    filename = os.path.split(save_path)[-1]
    ffmpeg_cmd = get_usable_ffmpeg()
    ffmpeg_params = [
        ffmpeg_cmd, '-y', '-i', m3u8_url,
        '-c', 'copy', '-bsf:a', 'aac_adtstoasc',
        '--', save_path
    ]
    try:
        ff = FfmpegProgress(ffmpeg_params)
        with Progress() as pp:
            print(f"{m3u8_url=}")
            ff_download = pp.add_task(filename, total=100)
            for progress in ff.run_command_with_progress():
                if progress > 0:
                    pp.update(ff_download, completed=progress)
            pp.update(ff_download, completed=100)
            pp.stop()
    except RuntimeError as e:
        print(f"RuntimeError.ERROR: downloader run {ffmpeg_params=}")
        return False
    except TypeError as e:
        print(f"TypeError.ERROR: downloader run {ffmpeg_params=}")
        return False
    except KeyboardInterrupt as e:
        os.remove(save_path)
        return False
    return os.path.isfile(save_path)


def downloader(client, src_urls_with_filename: list,
               dest_dir: [os.PathLike, str, None] = None,
               display: [bool, None] = None,
               force: bool = False) -> dict:
    assert isinstance(client, httpx.Client)
    assert len(src_urls_with_filename) > 0 and len(src_urls_with_filename[0]) == 2
    dest_dir = os.getcwd() if dest_dir is None else dest_dir
    assert os.path.isdir(dest_dir)
    total = len(src_urls_with_filename)
    display = (total > 5) if display is None else display
    done_mark = dict()
    with Progress(disable=not display) as pp:
        for src_url, filename in src_urls_with_filename:
            ext_guess = filename is None
            if filename is None:
                filename = src_url.split("/")[-1] if filename is None else filename
                filename = os.path.join(dest_dir, filename)
            if force is False and os.path.isfile(filename):
                continue
            try:
                with client.stream("GET", src_url) as resp:
                    if resp.status_code // 100 != 2:
                        continue
                    total = int(resp.headers.get("Content-Length", 0))
                    total = None if total == 0 else total // 1024
                    download_task = pp.add_task(os.path.basename(filename), total=(total or 100))
                    with open(filename, 'wb') as save_file:
                        for chunk in resp.iter_bytes():
                            save_file.write(chunk)
                            if total is None:
                                pp.update(download_task, advance=1)
                            else:
                                pp.update(download_task, completed=resp.num_bytes_downloaded // 1024)
                        pp.update(download_task, completed=total or 100)
            except (httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadTimeout):
                print("httpx.ConnectError:", src_url)
                if os.path.isfile(filename):
                    os.remove(filename)
                if src_url.startswith("https://raw.githubusercontent.com"):
                    for x in SaverData.github_booster:
                        new_url = src_url.replace("raw.githubusercontent.com", x)
                        print(f"Retry With Github Booster: {new_url}")
                        resp = downloader(client, [(new_url, filename)])
                        if all(list(resp.values())):
                            break
                continue
            except ValueError as e:
                print("ValueError:", f"{src_url=}")
                continue
            except KeyboardInterrupt:
                if os.path.isfile(filename):
                    os.remove(filename)
                raise KeyboardInterrupt
            finally:
                done_mark[src_url] = os.path.isfile(filename)
                if os.path.isfile(filename) is True and ext_guess is True:
                    if '.' not in filename:
                        kind = filetype.guess_extension(filename)
                        if kind is not None:
                            new_fpath = ".".join([filename, kind])
                            shutil.move(filename, new_fpath)
    return done_mark


def tans_uub2html(src: str, save_path: str) -> tuple:
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
    root_path = os.path.dirname(os.path.dirname(save_path))
    emot_map_path = os.path.join(root_path, 'assets', 'emot', 'emotion_map.json')
    emot_map = json.load(open(emot_map_path, 'r'))
    # 基础替换：换行,加粗,斜体,下划线,删除线,颜色结尾
    for ubb, tag in ubb_tag_basic.items():
        src = src.replace(ubb, tag)
    # 正则替换：颜色,表情,图片
    img_task = list()
    for n, rex_rule in ubb_tag_rex.items():
        for tag in re.compile(rex_rule).findall(src):
            if n == 'color':
                src = src.replace(tag[0], f'<font color=\\"{tag[1]}\\">')
            elif n == 'size':
                src = src.replace(tag[0], f'<span style=\\"font-size:{tag[1]}\\">{tag[2]}</span>')
            elif n == 'emot':
                if tag[1] in emot_map:
                    src = src.replace(tag[0], f'<img class=\\"ubb-emotion\\" src=\\"{emot_map[tag[1]]}\\">')
            elif n == 'emot_old':
                alias = ",".join(tag[1:])
                if alias in emot_map['saved']:
                    src = src.replace(tag[0], f'<img class=\\"ubb-emotion\\" src=\\"{emot_map["saved"][alias]}\\">')
                elif alias in emot_map['lost']:
                    pass
            elif n == 'image':
                img_name = tag[1].split('/')[-1]
                img_path = os.path.join(save_path, 'img', img_name)
                img_task.append((tag[1], img_path))
                src = src.replace(tag[0], f'<img class=\\"lazy\\" src=\\"../../assets/img/404img.png\\" data-src=\\"img/{img_name}\\" alt=\\"{tag[1]}\\">')
            elif n == 'at':
                src = src.replace(tag[0], f'<a class=\\"ubb-name\\" target=\\"_blank\\" href=\\"https://www.acfun.cn/u/{tag[1]}\\">{tag[2]}</a>')
            elif n == 'at_old':
                src = src.replace(tag[0], f'<a class=\\"ubb-name\\">@{tag[1]}</a>')
            elif n == 'jump':
                src = src.replace(tag[0], f'<a class=\\"quickJump\\" onclick=\\"SAVER.utils.quickJump({tag[1]})\\">{tag[2]}</a>')
            elif n == 'resource':
                resource_a = '<a class=\\"ubb-ac\\" data-aid=\\"{ac_num}\\" href=\\"{href}\\" target=\\"_blank\\">{title}</a>'
                src = src.replace(
                    tag[0], ubb_resource_icon[tag[2]] + resource_a.format(
                        ac_num=tag[1],
                        href=ubb_resource_url[tag[2]] + tag[1],
                        title=tag[3]
                    ))
    # for tag in re.compile(r"(\[([^\]]+)\])").findall(src):
    #     print(tag)
    return src, img_task


def tans_comment_uub2html(data_path):
    rid = os.path.basename(data_path)
    comment_json_path = os.path.join(data_path, 'data', f"{rid}.comment.json")
    comment_json_temp = os.path.join(data_path, 'data', f"{rid}.comment.temp")
    temp_ok = os.path.isfile(comment_json_temp)
    img_task = list()
    if temp_ok:
        comment_json_string = open(comment_json_temp, 'r').read()
    else:
        comment_json_string = open(comment_json_path, 'r').read()
        comment_json_string, img_task = tans_uub2html(comment_json_string, data_path)
        with open(comment_json_temp, 'w') as t:
            t.write(comment_json_string)
    comment_data = json.loads(comment_json_string)
    total_comment = len(comment_data['rootComments'])
    # 评论分块存储，每块100条；跟楼按每页划分。
    # 区块正向划分，预留已删除位置；区块顺序列表倒置；热评在最后。
    total_block = math.ceil(total_comment / 100)
    blocks = {}
    count = 0
    for X in comment_data['rootComments']:
        count += 1
        z = str(math.floor(X['floor'] / 100))
        if z not in blocks:
            blocks[z] = {
                "hotComments": [],
                "rootComments": [],
                "subCommentsMap": {},
                "save_unix": time.time(),
                "totalComment": total_comment
            }
        blocks[z]['rootComments'].append(X)
        cid = str(X['commentId'])
        if cid in comment_data['subCommentsMap']:
            blocks[z]['subCommentsMap'][cid] = comment_data['subCommentsMap'][cid]
    totals = 0
    for v in blocks.values():
        totals += len(v["rootComments"])
    if totals == 0:
        comment_block_js_path = os.path.join(data_path, 'data', f"{rid}.comment.1.js")
        with open(comment_block_js_path, 'wb') as js_file:
            comment_js = "LOADED.comment[1]={'hotComments':[],'rootComments':[],'subCommentsMap':{},};"
            js_file.write(comment_js.encode())
        return img_task
    blocks = [j for i, j in sorted(blocks.items(), reverse=True)]
    blocks[0]["hotComments"] = comment_data["hotComments"]
    for Y in blocks[0]["hotComments"]:
        cid = str(Y['commentId'])
        if cid not in blocks[0]['subCommentsMap'] and cid in comment_data['subCommentsMap']:
            blocks[0]['subCommentsMap'][cid] = comment_data['subCommentsMap'][cid]
    for i in range(len(blocks)):
        B = blocks[i]
        B.update({'page': i + 1, 'total': len(blocks)})
        B['rootComments'] = sorted(B['rootComments'], key=lambda x: x['floor'], reverse=True)
        comment_block_js_path = os.path.join(data_path, 'data', f"{rid}.comment.{i+1}.js")
        comment_block_js_string = json.dumps(B, separators=(',', ':'))
        with open(comment_block_js_path, 'wb') as js_file:
            comment_js = f"LOADED.comment[{i+1}]={comment_block_js_string};"
            js_file.write(comment_js.encode())
    if temp_ok:
        os.remove(comment_json_temp)
    return img_task


def saver_template(**filters):
    templates = Environment(loader=PackageLoader('acsaver', 'templates'))
    templates.filters['unix2datestr'] = unix2datestr
    templates.filters['math_ceil'] = math.ceil
    for name, func in filters.items():
        templates.filters[name] = func
    return templates


def live_recorder(live_obj, save_path: [os.PathLike, str], quality: [int, str] = 0):
    assert live_obj.is_open is True
    if isinstance(quality, str) and quality.isdigit():
        quality = int(quality)
    begin_time = live_obj.start_time.replace("-", "").replace(":", "").replace(" ", "")
    save_dir = os.path.join(save_path, begin_time)
    time_now = unix2datestr(f="%Y%m%d%H%M%S")
    save_mp4 = os.path.join(save_dir, f"{time_now}.mp4")
    os.makedirs(save_dir, exist_ok=True)
    adapt = live_obj.m3u8_url(quality, False)
    live_obs_stream = adapt['url']
    stream_split = parse.urlsplit(live_obs_stream)
    stream_key = parse.parse_qs(stream_split.query).get('auth_key', [])[0]
    live_obs_stream = f"{stream_split.scheme}://{stream_split.netloc}{stream_split.path}?auth_key={stream_key}"
    ffmpeg = get_usable_ffmpeg()
    if ffmpeg is None:
        print(f"ERROR: record need ffmpeg")
        return False
    cmd_with_progress = [
        ffmpeg,
        "-progress", "-", "-nostats",
        '-loglevel', '+repeat',
        "-i", f"{live_obs_stream}",
        "-c:v", "copy", "-c:a", "copy",
        f"{save_mp4}"
    ]
    p = subprocess.Popen(
        cmd_with_progress,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=False)
    begin_read = False
    tmp = dict()
    console = Console()

    def display_tui(data):
        filesize = int(data.get('total_size', 0))
        infos = f" 已录制 {data.get('out_time', '00:00:00.000000')}\r\n " \
                f" 比特率: {data.get('bitrate', '???')}  " \
                f" 大小: {sizeof_fmt(filesize): >6} "
        record_panel = Panel(Text(infos, justify='center'),
                             title=f"AcLive({live_obj.uid})@{time_now}.mp4",
                             border_style='red', width=50, style="black on white")
        return record_panel

    with Live(console=console) as live_console:
        while True:
            if p.stdout is None:
                continue
            stderr_line = p.stdout.readline().decode("utf-8", errors="replace").strip()
            if stderr_line == "" and p.poll() is not None:
                break
            if stderr_line == "Press [q] to stop, [?] for help":
                begin_read = True
                continue
            if begin_read is True:
                r = stderr_line.split('=')
                tmp.update({r[0]: r[1]})
                live_console.update(Align.center(display_tui(tmp)))

    return True


def update_js_data(save_root: [os.PathLike, str]):
    saver_data = dict()
    saver_data_path = os.path.join(save_root, "data.js")
    if os.path.isfile(saver_data_path):
        with open(saver_data_path, 'r') as js_string:
            saver_data = json.loads(js_string.read()[12:-1])  # let AcSaver=.....;
    least = saver_data.get('least', [])
    for fn in SaverData.folder_names:
        if fn in ['member', 'live']:
            continue
        old_dirs = saver_data.get(fn, [])
        fpath = os.path.join(save_root, fn)
        now_dirs = [i for i in os.listdir(fpath) if os.path.isdir(os.path.join(fpath, i))]
        news = list(set(now_dirs).difference(set(old_dirs)))
        nomore = list(set(old_dirs).difference(set(now_dirs)))
        final_dirs = list()
        for x in old_dirs:
            if x not in nomore:
                final_dirs.append(x)
            least_v = (fn, x)
            if x in nomore and least_v in least:
                least.remove(least_v)
        for y in news:
            if y not in final_dirs:
                final_dirs.append(y)
        final_dirs = [n for n in final_dirs if os.path.isfile(os.path.join(save_root, fn, n, 'data', f'{n}.js'))]
        saver_data[fn] = final_dirs
        for i in news:
            if [fn, i] not in news:
                least.append([fn, i])
    new = list()
    for u in least:
        if u not in new and u[1] in saver_data[u[0]]:
            new.append(u)
    saver_data['least'] = new
    with open(saver_data_path, 'wb') as js:
        saver_data_string = json.dumps(saver_data, separators=(',', ':'))
        data_js = f"let AcSaver={saver_data_string};"
        js.write(data_js.encode())
    return os.path.isfile(saver_data_path)


def create_http_server_bat(save_root: [os.PathLike, str]):
    bat_path = os.path.join(save_root, "CivetWeb.bat")
    if os.path.isfile(bat_path) is True:
        return True
    cmd = "@echo off\n" \
          "if exist CivetWeb64.exe (set \"exename=CivetWeb64.exe\" & goto run\n" \
          ") else if exist CivetWeb32.exe (set \"exename=CivetWeb32.exe\" & goto run\n" \
          ") else (echo \"需要CivetWeb64.exe或CivetWeb32.exe，赶紧去下载一个\" " \
          "& start https://github.com/civetweb/civetweb/releases & pause)\n" \
          ":run\nstart http://127.0.0.1:666/index.html\n" \
          "tasklist /fi \"ImageName eq %exename%\" /fo csv 2>NUL | find /I \"%exename%\">NUL\n" \
          "if \"%ERRORLEVEL%\"==\"1\" (start %exename% -listening_ports 666)\ngoto end"
    with open(bat_path, 'w') as bat:
        bat.write(cmd)
    return os.path.isfile(bat_path)
