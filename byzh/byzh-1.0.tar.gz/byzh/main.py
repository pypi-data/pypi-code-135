import requests as r
import json as j
import webbrowser as web
import io
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import requests

key = "e336627d3a7cd6235ad91eb9c82d157d"
url = "http://api.a20safe.com/api.php?"

# 获取ip归属地
def IP(ip):
    global key,url
    api = "19"
    ip = ip
    data = {"api":api , "key":key , "ip":ip}
    date = r.post(url=url,data = data)
    json = j.loads(date.text)["data"][0]
    print("您查询的IP为：",ip)
    print("地区：",json['region'])
    print("运营商：",json['company'])
    print("网络类型：",json['internet'])

# 获取随机一言
def code(type):
    global key,url
    api = "6"
    a = type

    data = {"api":api , "key":key , "type":a}
    string = r.post(url=url , data=data)
    json = j.loads(string.text)["data"][0]
    # print(json)
    print("句子：",json['motto'])
    print("来源作品：",json['from'])
    print("作者：",json['who'])
    print("创造人：", json['creator'])

# 获取随机图片
def picture(lx,hs):
    global key,url
    api = "9"
    a = lx
    b = hs

    data = {"api": api, "key": key, "lx": a, "hs": b}
    string = r.post(url=url, data=data)
    json = j.loads(string.text)["data"][0]
    # print(json)
    print("图片地址：", json['imgurl'])
    print("图片宽度：", json['width'])
    print("图片高度：", json['height'])

    web.open(json['imgurl'])
    # root = tk.Tk()
    # url = json['imgurl']
    # image_bytes = urlopen(url).read()
    # data_stream = io.BytesIO(image_bytes)
    # pil_image = Image.open(data_stream)
    # w, h = pil_image.size
    # fname = url.split('/')[-1]
    # sf = "{} ({}x{})".format(fname, w, h)
    # root.title(sf)
    # tk_image = ImageTk.PhotoImage(pil_image)
    # label = tk.Label(root, image=tk_image, bg='brown')
    # label.pack(padx=5, pady=5)
    # root.mainloop()

# 获取北京时间
def time():
    global key,url
    api = "2"

    data = {"api": api, "key": key}
    string = r.post(url=url, data=data)
    json = j.loads(string.text)["data"][0]
    print("北京时间：", json['time'])
    print("10位时间戳：", json['time10'])
    print("13位时间戳：", json['time13'])

# 生成二维码
def qrcode(t,d,l,ll,fg,bg,gd):
    global key,url
    api = "4"
    t = t
    d = d
    l = l
    ll = ll
    fg = fg
    bg = bg
    gd = gd

    data = {"api":api , "key":key , "t":t, "d":d, "l":l, "ll":ll, "fg":fg, "bg":bg, "gd":gd}
    string = r.post(url=url , data=data)
    json = j.loads(string.text)["data"][0]
    print("二维码图片地址：",json['url'])
    web.open(json['url'])

# 敏感词检测
def S_word(word):
    global key,url
    api = "5"
    # word = word

    data = {"api": api, "key": key, "text": word}
    string = r.post(url=url, data=data)
    json = j.loads(string.text)["data"][0]
    print("过滤后的内容：", json['text1'])
    print("过滤词：", json['words'])

#原神语音合成
def YS_yvyin(text,chara):
    URL = "http://233366.proxy.nscc-gz.cn:8888/"
    dicts = {'text': text, 'speaker': chara}
    def parse_url(data={}):
        item = data.items()
        urls = "?"
        for i in item:
            (ke, value) = i
            temp_str = ke + "=" + value
            urls = urls + temp_str + "&"
        urls = urls[:len(urls) - 1]
        return urls

    print(URL + parse_url(dicts))
    url = URL + parse_url(dicts)
    web.open(url)


def chunlian(text, HorV='V', quality='L', out_file=None):
    def get_word(ch, quality):
        """获取单个汉字（字符）的图片
        ch          - 单个汉字或英文字母（仅支持大写）
        quality     - 单字分辨率，H-640像素，M-480像素，L-320像素
        """
        fp = io.BytesIO(requests.post(url='http://xufive.sdysit.com/tk', data={'ch': ch}).content)
        im = Image.open(fp)
        w, h = im.size
        if quality == 'M':
            w, h = int(w * 0.75), int(0.75 * h)
        elif quality == 'L':
            w, h = int(w * 0.5), int(0.5 * h)
        return im.resize((w, h))

    def get_bg(quality):
        """获取春联背景的图片"""
        return get_word('bg', quality)

    # def write_couplets(text, HorV='V', quality='L', out_file=None):
    """生成春联
    text        - 春联内容，以空格断行
    HorV        - H-横排，V-竖排
    quality     - 单字分辨率，H-640像素，M-480像素，L-320像素
    out_file    - 输出文件名
    """
    usize = {'H': (640, 23), 'M': (480, 18), 'L': (320, 12)}
    bg_im = get_bg(quality)
    text_list = [list(item) for item in text.split()]
    rows = len(text_list)
    cols = max([len(item) for item in text_list])
    if HorV == 'V':
        ow, oh = 40 + rows * usize[quality][0] + (rows - 1) * 10, 40 + cols * usize[quality][0]
    else:
        ow, oh = 40 + cols * usize[quality][0], 40 + rows * usize[quality][0] + (rows - 1) * 10
    out_im = Image.new('RGBA', (ow, oh), '#f0f0f0')
    for row in range(rows):
        if HorV == 'V':
            row_im = Image.new('RGBA', (usize[quality][0], cols * usize[quality][0]), 'white')
            offset = (ow - (usize[quality][0] + 10) * (row + 1) - 10, 20)
        else:
            row_im = Image.new('RGBA', (cols * usize[quality][0], usize[quality][0]), 'white')
            offset = (20, 20 + (usize[quality][0] + 10) * row)
        for col, ch in enumerate(text_list[row]):
            if HorV == 'V':
                pos = (0, col * usize[quality][0])
            else:
                pos = (col * usize[quality][0], 0)
            ch_im = get_word(ch, quality)
            row_im.paste(bg_im, pos)
            row_im.paste(ch_im, (pos[0] + usize[quality][1], pos[1] + usize[quality][1]), mask=ch_im)
        out_im.paste(row_im, offset)
    if out_file:
        out_im.convert('RGB').save(out_file)

    def resize(w, h, w_box, h_box, pil_image):
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)
    root = tk.Tk()
    w_box = 800
    h_box = 800
    pil_image = Image.open(out_file)
    w, h = pil_image.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    label = tk.Label(root, image=tk_image, width=w_box, height=h_box)
    label.pack(padx=5, pady=5)
    root.mainloop()
    # out_im.show()




