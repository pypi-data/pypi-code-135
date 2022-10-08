"""
    DLT645协议
"""
from ats_base.base import req, entrance
from ats_base.config.configure import CONFIG
from ats_base.common import func

pro = entrance.api(CONFIG.get(func.PROTOCOL, 'dlt645'))


def manual(operation: str, mode: str = None, security: str = None):
    return req.get('{}/{}'.format(pro, 'manual'),
                   params=func.to_dict(operation=operation, mode=mode, security=security))


def encode(parse: dict, cache: str = None):
    parse.update(func.to_dict(cache=cache))
    return req.post('{}/{}'.format(pro, 'encode'), jsons=parse)


def decode(frame: str, session: dict = None, part_frame: str = None, cache: str = None):
    return req.post('{}/{}'.format(pro, 'decode'),
                    jsons=func.to_dict(frame=frame, session=session, part_frame=part_frame, cache=cache))
