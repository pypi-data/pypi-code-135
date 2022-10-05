import json
from random import Random
from TDhelper.network.rpc.Generic.Host import HostManager


def get_key(key, cnf):
    return cnf[key] if key in cnf else None


class RPC_Returns_description:
    returns: int = None
    key: str = None
    valueDescription: str = None

    def __init__(self, k, v_desc):
        self.key = k
        self.valueDescription = v_desc

    def toCnf(self):
        return json.dumps({
            "returns": self.returns,
            "key": self.key,
            "valueDescription": self.valueDescription
        })

    @classmethod
    def create_by_cnf(self, cnf):
        if isinstance(cnf, str):
            try:
                cnf = json.loads(cnf)
            except Exception as e:
                raise e
        results = []
        for item in cnf:
            results.append(
                RPC_Returns_description(item["key"], item["valueDescription"])
            )
        return results


class RPC_Params:
    serviceUri: int = None
    key: str = None
    descripiton: str = None
    default = None

    def __init__(self, k, desc, defaultV):
        self.key = k
        self.descripiton = desc
        self.default = defaultV

    def toCnf(self):
        return json.dumps({
            "serviceUri": self.serviceUri,
            "key": self.key,
            "description": self.descripiton,
            "defaultValue": self.default
        })

    @classmethod
    def create_by_cnf(self, cnf):
        if isinstance(cnf, str):
            try:
                cnf = json.loads(cnf)
            except Exception as e:
                raise e
        results = []
        for item in cnf:
            results.append(
                RPC_Params(get_key('key', item),
                           get_key('description', item),
                           get_key('defaultVale', item)
                           )
            )
        return results


class RPC_Returns:
    serviceUri: int = None
    valueType: str = None
    examples: dict = None
    descriptions: '[RPC_Returns_description]' = []

    def __init__(self, vt, examp, desc):
        self.valueType = vt
        self.examples = examp
        self.descriptions = desc

    def toCnf(self):
        return json.dumps({
            "serviceUri": self.serviceUri,
            "valueType": self.valueType,
            "examples": self.examples
        })

    @classmethod
    def create_by_cnf(self, cnf):
        if isinstance(cnf, str):
            try:
                cnf = json.loads(cnf)
            except Exception as e:
                raise e

        return RPC_Returns(
            get_key("valueType", cnf),
            get_key("examples", cnf),
            RPC_Returns_description.create_by_cnf(get_key('descriptions', cnf))
        )


class RPC_Method:
    service: int = None
    name: str = None
    uri: str = None
    method: str = None
    version: str = None
    description: str = None
    params: '[RPC_Params]' = []
    returns: '[RPC_Returns]' = []

    def __init__(self, name, uri, method, version, description, params, returns):
        self.name = name
        self.uri = uri
        self.method = method
        self.version = version
        self.description = description
        self.params = params
        self.returns = returns

    def __get_method_type__(self, v: str):
        v = v.upper()
        if v == "GET":
            return 1
        elif v == "POST":
            return 2
        elif v == "PUT":
            return 3
        elif v == "DELETE":
            return 4
        else:
            raise "method type value must GET,POST,PUT,DELETE."

    def __transfer_method_type__(self,v:int):
        if v==1:
            return "GET"
        elif v==2:
            return "POST"
        elif v==3:
            return "PUT"
        elif v==4:
            return "DELETE"
        else:
            raise "method transer value must 1,2,3,4."

    def toCnf(self):
        return json.dumps(
            {
                "service": self.service,
                "key": self.name,
                "uri": self.uri,
                "method": self.__get_method_type__(self.method),
                "version": self.version,
                "description": self.description
            }
        )

    @classmethod
    def create_by_cnf(self, name, key, cnf):
        if isinstance(cnf, str):
            try:
                cnf = json.loads(cnf)
            except Exception as e:
                raise e
        if 'collect' in cnf:
            name = "".join([name,'.', get_key('collect',cnf).upper(), '_', key])
        else:
            name = "".join([name,'.', key])
        return RPC_Method(
            name=name,
            uri=get_key('uri', cnf),
            method=get_key('method', cnf),
            version=get_key('version', cnf),
            description=get_key('description', cnf),
            params=RPC_Params.create_by_cnf(get_key('params', cnf)),
            returns=RPC_Returns.create_by_cnf(get_key("returns", cnf))
        )


class RPC_SERVICE:
    host: list = HostManager()
    name: str = None
    description: str = None
    key: str = None
    secret: str = None
    protocol: str = "http://"
    methods= {}
    def __init__(self, name=None, description=None, key=None, secret=None, protocol=None, host_cnf=None, methods_cnf=None):
        self.name = name
        self.description = description
        self.key = key
        self.secret = secret
        self.protocol = protocol
        if host_cnf:
            for item in host_cnf:
                self.host.register(
                    get_key('serverId', item),
                    get_key("host", item),
                    int(get_key("port", item)),
                    get_key("sniffer", item),
                    protocol,
                    True
                )
        if methods_cnf:
            for k,v in methods_cnf.items():
                self.methods[k]= RPC_Method.create_by_cnf(self.key.upper(),k.upper(),v)
            #self.methods = [RPC_Method.create_by_cnf(
            #    self.key.upper(), k.upper(), v) for k, v in methods_cnf.items()]

    def toCnf(self):
        return json.dumps({
            "name": self.name,
            "description": self.description,
            "key": self.key.upper(),
            "accessSecret": self.secret,
            "protocol": self.protocol
        })

    @classmethod
    def create_by_cnf(self, cnf):
        if isinstance(cnf, str):
            try:
                cnf = json.loads(cnf)
            except Exception as e:
                raise e
        return RPC_SERVICE(
            name=get_key('name', cnf),
            description=get_key('description', cnf),
            key=get_key('key', cnf).upper(),
            secret=get_key('secret', cnf),
            protocol=get_key('protocol', cnf),
            host_cnf=get_key('hosts', cnf),
            methods_cnf=get_key('methods', cnf)
        )


class RPC_SERVICE_CONF:
    uris: list = []
    token: str = None

    def __init__(self, uris, token):
        self.uris = uris
        self.token = token
        for offset in range(0, len(self.uris)):
            self.uris[offset] = self.uris[offset].strip("/")

    def getUri(self):
        offset = len(self.uris)-1
        if offset > 0:
            return self.uris[Random.randint(0, offset-1)]+"/"
        elif offset == 0:
            return self.uris[0]+"/"
        else:
            raise Exception("RPC server config has error, uri is none.")
