import requests

async def tag_search(tag) -> dict:
    '''
    传入需要搜索的tag，返回列表
    '''
    result = dict(requests.get(url = f"https://api.lolicon.app/setu/v2?size=original&tag={tag}&num=20").json())
    if not result.get("error"):
        return result.get("data")