from ats_base.base import req, api
from ats_base.common import util
from ats_base.config.configure import CONFIG


def get(name: str, key: str):
    """
    获取 - 参数格式
    :param name:
    :param key:
    :param params:
    :return:
    """
    url = '{}/{}/{}'.format(api.get(CONFIG.get('BASE', 'url') + CONFIG.get('BASE', 'manual')), name, key)

    result = req.get(url)
    if result['code'] == 500:
        raise Exception(result['message'])

    return result['data']


def assist(pattern: dict, **kwargs):
    """
    辅助 - 获取格式内容并替换其中变量
    :param pattern:
    :return:
    """
    ftd = {}
    for pk, data in kwargs.items():
        ftd[pk] = util.replace(pattern, **data)

    return ftd
