"""
    数据验证服务
"""
from ats_base.base import req, entrance
from ats_base.common import util
from ats_base.config.configure import CONFIG

dvs = entrance.api(CONFIG.get(util.SERVICE, 'dvs'))


def verify(code: str, function: str, data):
    """
    数据验证
    :param code:
    :param function:
    :param data:
    :return:
    """
    result = req.post('{}/{}/{}'.format(dvs, code, function), jsons=data)

    if result['code'] == 500:
        raise Exception(result['message'])

    return result['data']
