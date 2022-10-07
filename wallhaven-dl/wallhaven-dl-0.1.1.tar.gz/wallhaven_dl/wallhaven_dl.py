# -*- encoding: utf-8 -*-
'''
@File    :   wallhaven-dl.py
@Time    :   2022/10/04 10:13:51
@Author  :   geekocean
@Version :   1.0
@Contact :   liuyaanng@gmail.com
@Desc    :   downalod wallpapers from wallhaven.cc
'''

import json
import argparse
import sys
import requests
import os
import yaml
import time
from rich.progress import track


BASE_URL = "https://wallhaven.cc/api/v1/search"
API_KEY = ""
cookies = dict()
ROOT = ""
PAGES = 0
# parameters for request


def setparse():
    global API_KEY, BASE_URL, ROOT, PAGES
    parser = argparse.ArgumentParser(
        description="Download wallpapers from wallpaper.cc", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-s", "--search", action='store_true',
                        help="Search.", required=True)
    parser.add_argument("-d", "--dir", type=str,
                        help="Directory to store wallpapers, default path is 'Images/Wallhaven'", default="Images/Wallhaven")
    parser.add_argument("-q", "--query", type=str,
                        help='''tagname - search fuzzily for a tag/keyword\n-tagname - exclude a tag/keyword\n+tag1 +tag2 - must have tag1 and tag2\n+tag1 -tag2 - must have tag1 and NOT tag2\n@username - user uploads\nid:123 - Exact tag search (can not be combined)\ntype:{png/jpg} - Search for file type (jpg = jpeg)\nlike:wallpaper ID - Find wallpapers with similar tags''')
    parser.add_argument("-c", "--categories", type=str, choices=['all', 'general', 'anime', 'people', 'ga', 'gp', 'ap'],
                        help='''all      - All Categories(Default).\ngeneral  - For 'General' wallpapers only.\nanime    - For 'Anime' wallpapers only.\npeople   - For 'People' wallpapers only.\nga       - For both 'General' and 'Anime' wallpapers.\ngp       - For both 'General' and 'People' wallpapers.\nap       - For both 'Anime' and 'People' wallpapers.''', default="ga")
    parser.add_argument("-p", "--purity", type=str, choices=['all', 'sfw', 'sketchy', 'nsfw', 'sfsk', 'sfn', 'skn'],
                        help='''all      - All Purity.\nsfw      - For 'Safe For Work'.\nsketchy  - For 'Sketchy'.\nnsfw     - For 'Not Safe For Work'.\nsfsk     - For both 'sfw' and 'sketchy'(Default).\nskn      - For both 'sketchy' and 'nsfw'.\nsfn      - For both 'sfw' and 'nsfw'.''', default="sfsk")
    parser.add_argument("-sort", "--sorting", type=str,
                        choices=['data_added', 'relevance', 'random', 'views', 'favorites', 'toplist'], help="Method of sorting results", default="date_added")
    parser.add_argument("-o", "--order", type=str,
                        choices=['desc', 'asc'], help="Sorting order, it contains 'desc and asc'", default="desc")
    parser.add_argument("-t", "--topRange", type=str, choices=[
                        '1d', '3d', '1w', '1M', '3M', '6M', '1y'], help="Sorting MUST be set to 'toplist'", default="1M")
    # add mutually exclusive group
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--atleast", type=str,
                       help="Minimum resolution allowed\n1920x1080")
    group.add_argument("-re", "--resolutions", type=str,
                       help="List of exact wallpaper resolutions\nSingle resolution allowed\n1920x1080,1920x1200")

    parser.add_argument("-ra", "--ratios", type=str,
                        help="List of aspect ratios\Single ratio allowed\n16x9,16x10")
    parser.add_argument("-pa", "--page", type=int,
                        help="Pagination\n¹ Not actually infinite", default=1)
    parser.add_argument("-key", "--key", type=str,
                        help="NSFW requires a valid API key, you can find it in Account Settings")
    args = parser.parse_args()
    if args.search:
        if args.query is not None:
            BASE_URL = BASE_URL + '&q=' + args.query
            ROOT = "Images/" + str(args.query)
        if args.categories is not None:
            cdicts = {'all': '111', 'general': '100', 'anime': '010',
                      'people': '001', 'ga': '110', 'gp': '101', 'ap': '011'}
            BASE_URL = BASE_URL + '?categories=' + cdicts[args.categories]
        if args.purity is not None:
            pdicts = {'all': '111', 'sfw': '100', 'sketchy': '010',
                      'nsfw': '001', 'sfsk': '110', 'skn': '011', 'sfn': '101'}
            if args.purity in ('nsfw', 'skn', 'sfn'):
                if args.key is None:
                    print("Downlaod nsfw wallpapers requires a vaild API key!")
                    sys.exit(0)
            BASE_URL = BASE_URL + '&purity=' + pdicts[args.purity]
        if args.sorting is not None:
            BASE_URL = BASE_URL + '&sorting=' + args.sorting
        if args.order is not None:
            BASE_URL = BASE_URL + '&order=' + args.order
        if args.topRange is not None:
            BASE_URL = BASE_URL + '&topRange=' + args.topRange
        if args.atleast is not None:
            BASE_URL = BASE_URL + '&atleast=' + args.atleast
        if args.resolutions is not None:
            BASE_URL = BASE_URL + '&resolution=' + args.resolutions
        if args.ratios is not None:
            BASE_URL = BASE_URL + '&ratios=' + args.ratios
        if args.page is not None:
            PAGES = args.page
        if args.key is not None:
            BASE_URL = BASE_URL + '&apikey=' + args.key
        if args.dir is not None:
            ROOT = args.dir
        os.makedirs(ROOT, exist_ok=True)


def download():

    img_data = []
    for i in range(PAGES):
        api_url = BASE_URL + '&page=' + str(i+1)
        api_response = requests.get(api_url, cookies=cookies)
        img_data += json.loads(api_response.content)['data']

    new_count = 0
    old_count = 0
    img_count = 0
    for img in track(img_data, description="Downloading...", refresh_per_second=30, update_period=0.01):
        img_url = img['path']
        img_num = "%03d" % img_count
        file_name = "image" + img_num + '.' + \
            img['file_type'].split('/')[-1]
        ospath = os.path.join(ROOT, file_name)
        if not os.path.exists(ospath):
            img_stream = requests.get(img_url, cookies=cookies)
            if img_stream.status_code == 200:
                with open(ospath, 'ab') as imgfile:
                    for chunk in img_stream.iter_content(1024):
                        imgfile.write(chunk)
                new_count += 1
            elif img_stream.status_code != 403 or img_stream.status_code != 404:
                print('Unable to download from: ', img_url)

        else:
            old_count += 1

        time.sleep(0.5)
        img_count += 1
    print('Total download %d wallpapers, %d already exists in folder %s' %
          (new_count, old_count, ROOT))
