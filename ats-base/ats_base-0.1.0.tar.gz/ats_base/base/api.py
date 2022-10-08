from ats_base.base import req
from ats_base.config.configure import CONFIG


def get(service: str):
    """
    获取service访问url
    :param service:
    :return:
    """
    url = '{}/{}'.format(CONFIG.get('BASE', 'url') + CONFIG.get('BASE', 'api'), service)

    result = req.get(url)
    if result['code'] == 500:
        raise Exception(result['message'])

    return result['data']
