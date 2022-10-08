"""
    协议栈
"""
from ats_base.base import req, entrance
from ats_base.config.configure import CONFIG
from ats_base.common import func

pro = entrance.api(CONFIG.get(func.SERVICE, 'pro'))


def manual(protocol: str, operation: str, mode: str = None, security: str = None):
    return req.get('{}/{}'.format(pro, 'manual'),
                   params=func.to_dict(protocol=protocol, operation=operation, mode=mode, security=security))


def encode(parse: dict, cache: str = None):
    parse.update(func.to_dict(cache=cache))
    return req.post('{}/{}'.format(pro, 'encode'), jsons=parse)


def decode(frame: str, session: dict = None, part_frame: str = None, cache: str = None):
    return req.post('{}/{}'.format(pro, 'decode'),
                    jsons=func.to_dict(frame=frame, session=session, part_frame=part_frame, cache=cache))
