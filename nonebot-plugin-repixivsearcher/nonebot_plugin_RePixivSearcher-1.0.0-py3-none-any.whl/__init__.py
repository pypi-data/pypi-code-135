from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GROUP
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.params import CommandArg

from .search import tag_search

import random

search_tag = on_command("搜", permission=GROUP, priority=0, block=True)
@search_tag.handle()
async def search_(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
    await search_tag.send('正在搜索，请勿多次发送请求')
    tag = str(arg).split(' ')
    if tag[0] == '':
        await search_tag.finish('你的标签去哪了')
    if tag[0] != '':
        img_json = await tag_search(tag[0])
        if img_json:
            await _img_(bot, event, img_json)
        if not img_json:
            await search_tag.finish('很抱歉，此标签没有任何可以找到的图片')

async def _img_(bot: Bot, event: GroupMessageEvent, data):
    '''预处理img信息并发送img信息'''
    img_list = []
    num = random.sample(range(0,len(data)-1), 3)
    for i in num:
        image = MessageSegment.image(f"https://px3.rainchan.win/img/small/{data[i]['pid']}")
        reply_msg = f'图片ID：{data[i]["pid"]}\n标题：{data[i]["title"]}\n作者：{data[i]["author"]}\n作者Pixiv UID：{data[i]["uid"]}\n标签：' + ', '.join(data[i]['tags']) + f'\n由于防止图片无法发出，图片为经过压缩的small版本，如需保存请前往下面链接：\nhttps://pixiv.re/{data[i]["pid"]}.jpg'
        img_list.append({"type":"node","data":{"name": "SDBot", "uin": bot.self_id,"content": reply_msg + image}})
    await bot.call_api("send_group_forward_msg", **{"group_id": event.group_id, "messages": [{"type":"node","data":{"name": "SDBot", "uin": bot.self_id,"content": img_list}}]})

_random = on_command('random',aliases={"来份涩图","随机涩图","来一份涩图","来一份二次元图"}, permission=GROUP, priority=3, block=True)
@_random.handle()
async def random_(bot: Bot, event: GroupMessageEvent):
    reply = MessageSegment.reply(event.message_id)
    await _random.send(reply + '正在随机涩图中，请勿多次发送请求')
    img = MessageSegment.image("https://px3.rainchan.win/random")
    await bot.call_api("send_group_forward_msg", **{"group_id": event.group_id, "messages": [{"type":"node","data":{"name": "SDBot", "uin": bot.self_id,"content": img}}]})