from types import FunctionType
from copy import copy
import sys
import os
import logging
sys.path.append("..")
sys.path.append('/home/tangjing/dev/python/pylib')

from TDhelper.generic.classDocCfg import doc
from TDhelper.network.rpc.Core.Meta import Meta
from TDhelper.network.rpc.Core.struct import *
from TDhelper.network.http.REST_HTTP import GET, POST, PUT, DELETE, ContentType

class SDCC(metaclass=Meta):
    '''SDCC
    service discovery center service.
    '''

    def __init__(self, uris: list, token: str, server_cnf: dict = None, logger: "logging" = None):
        self.__RPC_CNF__ = RPC_SERVICE_CONF(uris, token)
        self.__logger_hander__ = logger if logger else self.__logger_hander__
        self.__rpc_server_cnf__ = server_cnf if server_cnf else self.__rpc_server_cnf__
        self.__headers__["api-token"] = self.__RPC_CNF__.token

    def __set_coding__(self, encoding='utf-8'):
        self.__ENCODING__ = encoding

    def __setting__(self, cnf):
        self.__rpc_server_cnf__ = cnf

    def AutoRegister(self,conf,cxt:list):
        if "methods" not in conf:
            conf['methods']={}
        for cxt_item in cxt:
            for k, v in cxt_item.__dict__.items():
                if isinstance(v, FunctionType):
                    func_name = v.__name__.upper()
                    if v.__doc__:
                        methods = doc(v.__doc__, "rpc")
                        if methods:
                            methods = methods.replace("\n", "").strip()
                            try:
                                if func_name not in conf['methods']:
                                    conf['methods'][func_name]=json.loads(methods, encoding="utf-8")
                                    conf['methods'][func_name]["collect"]=cxt_item.__name__
                            except Exception as e:
                                raise e
        self.__register_by_cnf__(conf)

    def Register(self, cxt, filepath=False):
        if filepath:
            if os.path.exists(cxt):
                self.__register_by_file__(cxt)
            else:
                raise Exception("can not found path '%s'" % cxt)
        else:
            self.__register_by_cnf__(cxt)

    def __register_by_file__(self, filepath):
        m_json_source = None
        filepath = filepath.replace("\\", "/")
        with open(filepath, mode='r', encoding=self.__ENCODING__) as f:
            m_json_source = f.read()
            f.close()
        self.__register_by_cnf__(json.loads(m_json_source))

    def __register_by_cnf__(self, cnf: "dict|str"):
        if isinstance(cnf, str):
            cnf = json.loads(cnf)
        self.__analysis_cnf__(cnf)

    def __register_service__(self):
        uri = "".join([self.__RPC_CNF__.getUri(),
                      self.__service_register_uri__])
        state, res = self.__remote__(
            uri, self.__RPC_SERVICES__.toCnf(), copy(self.__headers__))
        if state:
            res = json.loads(res)
            if res["state"] == 200:
                s_id = res["msg"]["id"]
                self.__register_host__(s_id)
                self.__register_method__(s_id)
            else:
                self.__logger_hander__.error(
                    "Access(%s), '%s'" % (uri, res["msg"]))

    def __register_host__(self, parentId):
        uri = "".join([self.__RPC_CNF__.getUri(), self.__host_register_uri__])
        for v in self.__RPC_SERVICES__.host.__host__:
            host_cnf = self.__RPC_SERVICES__.host.get_host_by_key(v)
            data = {
                "host": host_cnf['host'],
                "port": host_cnf['port'],
                "state": True,
                "service": parentId
            }
            state, res = self.__remote__(uri, data, copy(self.__headers__))
            if state:
                res = json.loads(res)
                if res["state"] == 200:
                    self.__logger_hander__.info(
                        "register host '%s' success." % host_cnf['host'])
                else:
                    self.__logger_hander__.error(
                        "register host error(%s)" % res["msg"])

    def __register_method__(self, parentId):
        uri = "".join([self.__RPC_CNF__.getUri(),
                      self.__method_register_uri__])
        for item in self.__RPC_SERVICES__.methods:
            data = item
            data.service = parentId
            state, res = self.__remote__(
                uri, data.toCnf(), copy(self.__headers__))
            if state:
                res = json.loads(res)
                if res["state"] == 200:
                    self.__logger_hander__.info(
                        "register method '%s' success." % item.name)
                    m_id = res["msg"]["id"]
                    self.__register_parameters__(item, m_id)
                    self.__register_returns__(item, m_id)
                else:
                    self.__logger_hander__.error(
                        "register method '%s' error (%s)" % (item.name, res["msg"]))

    def __register_parameters__(self, method, parentId):
        uri = "".join([self.__RPC_CNF__.getUri(),
                      self.__params_register_uri__])
        for item in method.params:
            data = item
            data.serviceUri = parentId
            state, res = self.__remote__(
                uri, data.toCnf(), copy(self.__headers__))
            if state:
                res = json.loads(res)
                if res["state"] == 200:
                    self.__logger_hander__.info(
                        "register method paramete '%s' success." % item.key)
                else:
                    self.__logger_hander__.error(
                        "register method %s error(%s)." % (item.key, res["msg"]))

    def __register_returns__(self, method, parentId):
        uri = "".join([self.__RPC_CNF__.getUri(),
                      self.__return_register_uri__])
        data = method.returns
        data.serviceUri = parentId
        state, res = self.__remote__(uri, data.toCnf(), copy(self.__headers__))
        if state:
            res = json.loads(res)
            if res["state"] == 200:
                self.__logger_hander__.info("register method return success.")
                r_id = res["msg"]["id"]
                self.__register_return_desc__(data.descriptions, r_id)
            else:
                self.__logger_hander__.error(
                    "register method return error(%s)" % res["msg"])

    def __register_return_desc__(self, items, return_id):
        uri = "".join(
            [self.__RPC_CNF__.getUri(), self.__return_desc_register_uri__])
        for item in items:
            data = item
            data.returns = return_id
            state, res = self.__remote__(
                uri, data.toCnf(), copy(self.__headers__))
            if state:
                res = json.loads(res)
                if res["state"] == 200:
                    self.__logger_hander__.info(
                        "register method return description '%s' success." % item.key)
                else:
                    self.__logger_hander__.error(
                        "register method return description '%s' error(%s)", (item.key, res["msg"]))

    def __analysis_cnf__(self, cnf):
        assert isinstance(cnf, dict), "cnf must dict types."
        try:
            self.__RPC_SERVICES__ = RPC_SERVICE.create_by_cnf(cnf)
            if self.__RPC_SERVICES__:
                self.__register_service__()
            else:
                raise Exception("RPC services create error.")
        except Exception as e:
            raise e

    def __remote__(self, uri, data=b"", headers={}):
        try:
            state, res = POST(uri, post_data=data,
                              http_headers=headers, content_type=ContentType.JSON, time_out=5)
            if state == 200:
                return True, str(res, self.__ENCODING__)
            else:
                self.__logger_hander__.error(
                    "Access('%s'), HTTP CODE: %s" % (uri, state))
                return False, None
        except Exception as e:
            self.__logger_hander__.error(e.args)
            return False, None


if __name__ == "__main__":

    class services:
        def __init__(self) -> None:
            print('g')
        def list(self, request):
            '''
            [rpc]
            {
                "uri": "api/services",
                "method": "GET",
                "version": "1.0.0",
                "description": "获取服务列表",
                "params": [
                    {
                        "key":"page",
                        "description":"页码",
                        "defaultValue":"1"
                    }
                ],
            "returns":{
                "valueType":"json",
                "examples":"{&quot;state&quot;:200,&quot;msg&quot;:[{&quot;id&quot;:89,&quot;name&quot;:&quot;远程序配置中心&quot;,&quot;service_key&quot;:&quot;远程序配置服务.&quot;}]}",
                "descriptions":[
                    {
                        "key":"id",
                        "valueDescription":"服务ID"
                    },
                    {
                        "key":"name",
                        "valueDescription":"服务名称"
                    },
                    {
                        "key":"service_key",
                        "valueDescription":"服务KEY"
                    }
                ]
            }
            }
            [rpcend]
            '''
            return ""

        def create(self, request):
            '''
            [rpc]
            methods.storeGetApps::s.json
            [rpcend]
            '''
            return ""

        def retrieve(self, request, pk=None):
            '''
            [rpc]
            {
                "uri": "api/services/{pk}/",
                "method": "GET",
                "version": "1.0.0",
                "description": "根据ID获取一个服务",
                "params": [
                    {
                        "key": "pk",
                        "description": "ID值"
                    }
                ],
            "returns":{
                "valueType":"json",
                "examples":"{&quot;state&quot;:200,&quot;msg&quot;:{&quot;id&quot;:23,&quot;name&quot;:&quot;权限中心&quot;,&quot;service_key&quot;:&quot;PERMISSION_SERVICE&quot;}}",
                "descriptions":[
                    {
                        "key":"id",
                        "valueDescription":"服务ID"
                    },
                    {
                        "key":"name",
                        "valueDescription":"服务名称"
                    },
                    {
                        "key":"service_key",
                        "valueDescription":"服务KEY"
                    }
                ]
            }
            }
            [rpcend]
            '''
            return ""

    SDCC(["http://192.168.50.2:10001"], "d74218cff240f446d341c4a2f3a8c588", {
        "service": "api/services",
        "host": "api/hosts",
        "method": "api/uri",
        "params": "api/params",
        "return": "api/returns",
        "return_desc": "api/returnDescriptons"
    }).AutoRegister({
        "name": "测试服务",
        "description": "测试服务描述",
        "key": "RPC_TEST",
        "secret": "203920398409238408204324",
        "protocol": "http://",
        "hosts": [
            {
                "serverId": 1,
                "host": "192.168.0.1",
                "port": 8080,
                "sniffer": "api/sniffer",
                "proto": "http://"
            }
        ]
    },[services])
    '''.Register(
        os.path.join(
            sys.path[0],
            "s.json"
        ),
        filepath=True
    )'''
