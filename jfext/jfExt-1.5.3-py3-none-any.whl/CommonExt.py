# -*- coding: utf-8 -*-
"""
jf-ext.CommonExt.py
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2018-2022 by the Ji Fu, see AUTHORS for more details.
:license: MIT, see LICENSE for more details.
"""

import time


def dict_filter(dic, keys):
    new_dic = {}
    for key in keys:
        new_dic[key] = dic.get(key, "")
    return new_dic


def get_latency_str_for_millisecond(ms):
    if ms < 2:
        return "<2ms"
    elif ms < 5:
        return "2ms-5ms"
    elif ms < 20:
        return "5ms-20ms"
    elif ms < 100:
        return "20ms-100ms"
    elif ms < 1000:
        return "100ms-1s"
    elif ms < 5000:
        return "1s-5s"
    else:
        return ">5s"


def get_latency_msg_for_millisecond(ms, func_name):
    return ("[%4sms] [%10s] [%s]" % (ms, get_latency_str_for_millisecond(ms), func_name))


def timeout_tracking(func):
    """ 函数时间控制 """
    def wrapper(*argv, **kwgs):
        start_time = time.time()
        res = func(*argv, **kwgs)
        proc_time = int((time.time() - start_time) * 1000)
        msg = get_latency_msg_for_millisecond(proc_time, func.__name__)
        print(msg)
        return res
    return wrapper
