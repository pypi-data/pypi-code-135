# 工具
import json
import logging
import sys

import requests
from cacheout import Cache

from py_wechat_tools.libs.we_exception import WeError, WeAccessTokenExpired
import datetime


class WeChatData:
    errcode = 0
    errmsg = "ok"

    def __str__(self):
        return str(self.__dict__)


class LogsConf:

    CRITICAL = logging.CRITICAL
    FATAL = CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    WARN = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET

    name = "project_log"  # 名称
    level = DEBUG  # 是否输出debug日志。默认跟随debug模式
    file_path = None  # 输出到文件路径，为None则不启用文件存储日志
    formatter = "'%(asctime)s - %(name)s..%(filename)s.%(lineno)d - %(levelname)s: %(message)s'"  # 日志格式
    stream_handler = True  # 是否输出到终端，默认True

    def __init__(
            self,
            name="project_log",
            level=DEBUG,
            file_path=None,
            formatter="'%(asctime)s - %(name)s..%(filename)s.%(lineno)d - %(levelname)s: %(message)s'",
            stream_handler=True
    ):
        """
        重写日志输出类，默认输出到终端，可配置输出到文件。
        示例：Logs(...).logger.debug('输出内容')
        :param name: 显示名称
        :param level: 日志级别
        :param file_path: 输出到文件路径，为空则不启用文件存储日志（输出到文件和输出到终端必须选一个以上）
        :param formatter: 日志格式，默认格式：时间 - 显示名称 - 日志级别 - 在第几行：日志信息
        :param stream_handler: 是否输出到终端，（输出到文件和输出到终端必须选一个以上）
        """
        self.name = name
        self.level = level
        self.file_path = file_path
        self.formatter = formatter
        self.stream_handler = stream_handler


class Logs:

    def __init__(self, logs_conf: LogsConf):
        """
        重写日志输出类，默认输出到终端，可配置输出到文件。
        示例：Logs(...).logger.debug('输出内容')
        :param logs_conf: 日志配置类
        """

        logger = logging.getLogger(logs_conf.name)

        if logger.handlers:
            self.logger = logger
            return

        logger.setLevel(logs_conf.level)

        formatter = logging.Formatter(logs_conf.formatter)

        if logs_conf.file_path is None and logs_conf.stream_handler is False:
            raise ValueError("文件方式或输出到终端必须选一个以上")

        # 保存文件
        if logs_conf.file_path:
            handler = logging.FileHandler('output.log')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        # 输出到终端
        if logs_conf.stream_handler is not None:
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

        self.logger = logger


class WeRequest:
    """ 重新封装requsets """

    # def redirect(self, url):
    #     result = requests.get(url, stream=True)

    def __init__(self, logger):
        self.logger = logger

    def get(self, url, params=None, content_type="json", **kwargs):
        """
        的get请求
        :param url: 路径
        :param params: 参数
        :param content_type: 指定接收的类型，当前可指定类型有json:转换为WeChatData类，media: 返回content中的数据
        :param kwargs: 包含其他requests的参数
        :return: 返回一个WeChatData类，里面包含微信返回的结果，以及request_result：请求结果requests.Response
                如：
                    WeChatData.errcode: int
                    WeChatData.errmsg: str
                    WeChatData.request_result: <requests.Response>
                    WeChatData... 微信返回的对象
        """
        logger = self.logger
        result = requests.get(url, params=params, **kwargs)
        logger.debug("接口请求参数 >>> 微信api")
        logger.debug("路径：%s" % result.url)
        logger.debug("请求方式：GET")
        logger.debug("请求参数：%s" % params)
        logger.debug("——————————————————————————————————————————————————————————")
        logger.debug("")
        if content_type == "json":
            obj = self.deal_with(result)
            return obj
        elif content_type == "media":
            return result.content

        return result

    def post(self, url, data=None, encoding="utf-8", ensure_ascii=False, content_type="json", **kwargs):
        """
        get请求
        :param url: 路径
        :param data: 参数
        :param encoding: 给提交的数据(data)编码，
        :param ensure_ascii: json转文件存储时，中文是否使用ascii码，默认True
        :param content_type: 指定接收的类型，当前可指定类型有json:转换为WeChatData类，media: 返回content中的数据
        :param kwargs: 包含其他requests的参数
        :return: 返回一个WeChatData类，里面包含微信返回的结果，以及request_result：请求结果requests.Response
                如：
                    WeChatData.errcode: int
                    WeChatData.errmsg: str
                    WeChatData.request_result: <requests.Response>
                    WeChatData... 微信返回的对象
        """

        if isinstance(data, dict):
            data = json.dumps(data, ensure_ascii=ensure_ascii)

        if encoding:
            # 有些接口需要编码之后才生效
            data = data.encode(encoding)

        logger = self.logger
        result = requests.post(url, data=data, headers={'content-type': 'application/json'}, **kwargs)
        logger.debug("接口请求参数 >>> 微信api")
        logger.debug("路径：%s" % result.url)
        logger.debug("请求方式：POST")
        logger.debug("请求体(data)：%s" % data)
        logger.debug("——————————————————————————————————————————————————————————")
        logger.debug("")

        if content_type == "json":
            obj = self.deal_with(result)
            return obj
        elif content_type == "media":
            return result.content

        return result

    def deal_with(self, result):
        """
        解析请求，验证请求
        :param result: 请求返回的结果
        :return: WeChatData 对象
        """
        logger = self.logger
        logger.debug("接口响应参数 <<< 微信api")
        logger.debug("响应内容(源码): %s" % result.content)
        logger.debug("响应内容(解码后): %s" % str(result.content, encoding=result.encoding or "utf-8"))
        logger.debug("——————————————————————————————————————————————————————————")
        logger.debug("")

        if result.status_code != 200:
            raise ConnectionError("连接出错！errcode: %s。" % result.status_code)

        data_json = result.json() or {}
        if "errcode" not in data_json.keys():
            data_json["errcode"] = 0
        if "errmsg" not in data_json.keys():
            data_json["errmsg"] = "ok"

        # access_token 错误码
        err_code = [40001, 41001, 42001]
        if data_json["errcode"] in err_code:
            # access_token 错误
            raise WeAccessTokenExpired()

        if data_json["errcode"] != 0:
            raise WeError(result)

        data_json['request_result'] = result
        data_json['result_json'] = result.json()

        wechat_data = dict2obj(data_json)

        return wechat_data


class WeChatBase:

    DEBUG = False
    logs_conf = None

    # 定义日志类
    logger = None
    # 重写请求方法
    requests = None
    access_token = None
    cache = None
    passive_access_token = True  # 被动刷新access_token

    def __init__(self, appid, secret, debug=False, access_token=None, passive_access_token=True, **kwargs):
        """
        微信接口基础类
        :param appid: 小程序/公众号appid
        :param secret:  小程序/公众号secret
        :param debug: debug模式，开启后会debug日志
        :param access_token: 调用接口调用凭证，传入此凭证将不会从接口中重新获取，如果不传，会从get_access_token_cache()方法中获取
                            注意：从会从get_access_token_cache()方法中获取access_token会刷新access_token，
                                 旧的access_token将会在5分钟后失效（微信的平滑多度方案）
        :param passive_access_token: 是否被动更新access_token
                                    True: 当access_token 失效之后，自动获取新的access_token，并缓存
                                    False: 当access_token 失效之后抛出异常，需要主动调用get_access_token_cache() 接口刷新
        :param kwargs:
        """
        self.appid = appid
        self.secret = secret
        self.DEBUG = debug
        self.passive_access_token = passive_access_token

        # 初始化日志
        self.logs_conf = self.get_logs_conf()
        self.logger = Logs(self.logs_conf).logger

        # 初始化自定义的http请求方法
        self.wx_request = WeRequest(logger=self.logger)

        # 初始化access_token
        self.cache = self.get_cache_obj()
        self.access_token = access_token or self.cache.get("access_token", None)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def handle_access_token_expired(self, e, par):
        """ 处理 access_token过期方法 """
        if self.passive_access_token is False:
            raise e

        params = par["params"]

        self.cache_delete("access_token")
        self.access_token = self.get_access_token_cache()
        if isinstance(params, dict):
            params["access_token"] = self.access_token
        elif isinstance(params, str):
            params = json.loads(params)
            params["access_token"] = self.access_token
            params = json.dumps(params)
        else:
            raise ValueError("参数错误，params必须是dict或json字符串")

        par["params"] = params
        print("-"*60)
        print(params)
        return par

    def get(self, url, params=None, content_type="json", **kwargs):
        par = get_parameter(locals())

        try:
            result = self.wx_request.get(**par, **kwargs)
        except WeAccessTokenExpired as e:
            # 更新传参 或抛出异常
            par = self.handle_access_token_expired(e, par)
            result = self.wx_request.get(**par, **kwargs)  # 重新发起请求

        return result

    def post(self, url, data=None, params=None, encoding="utf-8", ensure_ascii=False, content_type="json", **kwargs):
        par = get_parameter(locals())

        try:
            result = self.wx_request.post(**par, **kwargs)
        except WeAccessTokenExpired as e:
            # 更新传参 或抛出异常
            par = self.handle_access_token_expired(e, par)
            result = self.wx_request.post(**par, **kwargs)  # 从新发起请求

        return result

    def get_access_token(self):
        """
        获取access_token

        获取小程序全局唯一后台接口调用凭据（access_token）。调用绝大多数后台接口时都需使用 access_token，开发者需要进行妥善保存
        2小时内有效，每天请求次数有限，做好缓存。

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/access-token/auth.getAccessToken.html

        :return: 返回WeChatDate对象对象包含参数：
                属性                  类型              说明
                errcode             number          错误码，正常时返回0
                errmsg              str             错误描述，正常时返回ok
                access_token        string          获取到的调用接口凭证
                expires_in          string          有效时长

        """
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = self.get_full_params(grant_type="client_credential")
        return self.get(url, params=params)

    @staticmethod
    def m2n(*args, **kwargs):
        """ 多选一 """
        return any(args) or any(list(kwargs.values()))

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_access_token_cache(self):
        """ 重写当前方法，获取缓存中的access_token """
        return self.access_token

    def get_full_params(self, **kwargs):
        """ 填充appid以及secret """
        return {"appid": self.appid, "secret": self.secret, **self.check_params(**kwargs)}

    @staticmethod
    def check_params(**kwargs):
        """ 排除掉为空的参数 """
        _dict = {**kwargs}
        [kwargs.pop(k) for k, v in _dict.items() if v is None or v == ""]
        return {**kwargs}

    # def set_logs(self, logs: dict):
    #     for k, v in logs.items():
    #         self.logs[k] = v

    def cache_delete(self, name, *args, **kwargs):
        return  self.cache.delete(name, *args, **kwargs)

    def get_logs_conf(self):
        """ 配置日志方法 """
        return LogsConf("wechat_tools")

    def set_cache_obj(self, cache):
        """
        设置缓存对象
        :param cache: 缓存对象，必须拥有.get()， .set()方法
        :return:
        """
        self.cache = cache
        # 尝试从缓存中获取access_token
        self.access_token = self.cache.get("access_token", None)

    def get_cache_obj(self):
        return Cache()


class OABase(WeChatBase):

    redirect_uri = None

    def __init__(self, appid, secret, redirect_uri, debug=False, access_token=None, passive_access_token=True, **kwargs):
        """
        初始化微信公众号工具

        获取用户信息优先级
        1、从 ot_dict 参数请求用户信息 （仅发起一次请求）
        2、根据 refresh_token 更新 access_token 再获取数据（会发起两次请求）
        3、重新授权code 拉起数据请求

        :param appid: 小程序/公众号appid
        :param secret:  小程序/公众号secret
        :param redirect_uri:  微信网页授权 用户刷新access_token
        :param refresh_token:  微信网页授权 用户刷新access_token
        :param debug: debug模式，开启后会debug日志
        :param access_token: 调用接口调用凭证，传入此凭证将不会从接口中重新获取，如果不传，会从get_access_token_cache()方法中获取
                            注意：从会从get_access_token_cache()方法中获取access_token会刷新access_token，
                                 旧的access_token将会在5分钟后失效（微信的平滑多度方案）
        :param passive_access_token: 是否被动更新access_token
                                    True: 当access_token 失效之后，自动获取新的access_token，并缓存
                                    False: 当access_token 失效之后抛出异常，需要主动调用get_access_token_cache() 接口刷新
        """

        super(OABase, self).__init__(
            appid=appid,
            secret=secret,
            redirect_uri=redirect_uri,
            debug=debug,
            access_token=access_token,
            passive_access_token=passive_access_token,
            **kwargs
        )


def dict2obj(d):
    """ 将字典转为可调用的对象 """

    # top = type(new_obj, (object,), d)
    top = WeChatData()
    seqs = tuple, list, set, frozenset
    for i, j in d.items():
        if isinstance(j, dict):
            setattr(top, i, dict2obj(j))
        elif isinstance(j, seqs):
            setattr(top, i, type(j)(dict2obj(sj) if isinstance(sj, dict) else sj for sj in j))
        else:
            setattr(top, i, j)
    return top


def get_parameter(parameter, *args):
    """ 获取方法参数，排除掉 self等自带参数。 """
    par = parameter
    par.pop("self", None)
    par.pop("args", None)
    par.pop("kwargs", None)
    [par.pop(i) for i in args]
    return par
