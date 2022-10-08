"""
    协议栈
"""
from ats_base.base import req, api
from ats_base.config.configure import CONFIG
from ats_base.common import util

KEY = 'pro'


def manual(protocol: str, operation: str, mode: str = None, security: str = None):
    return req.get(api.get(CONFIG.get(util.SERVICE, KEY) + ':manual'),
                   params=util.to_dict(protocol=protocol, operation=operation, mode=mode, security=security))


def encode(parse: dict, cache: str = None):
    parse.update(util.to_dict(cache=cache))
    return req.post(api.get(CONFIG.get(util.SERVICE, KEY) + ':encode'), jsons=parse)


def decode(frame: str, session: dict = None, part_frame: str = None, cache: str = None):
    return req.post(api.get(CONFIG.get(util.SERVICE, KEY) + ':decode'),
                    jsons=util.to_dict(frame=frame, session=session, part_frame=part_frame, cache=cache))
