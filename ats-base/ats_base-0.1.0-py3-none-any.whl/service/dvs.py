"""
    数据验证服务
"""
from ats_base.base import req, api
from ats_base.common import util
from ats_base.config.configure import CONFIG

KEY = 'dvs'


def verify(code: str, function: str, data):
    """
    数据验证
    :param code:
    :param function:
    :param data:
    :return:
    """
    url = '{}/{}/{}'.format(api.get(CONFIG.get(util.SERVICE, KEY)), code, function)
    result = req.post(url, jsons=data)

    if result['code'] == 500:
        raise Exception(result['message'])

    return result['data']
