
from operator import itemgetter

from vetl.core import tunnel

data = {}
default = {
    "engine": {
        "5432": "postgres"
    }
}

def setDB(host=None, port=None, dbname=None, username=None, password=None, engine=None, alias=None, *args, **kwargs):
    if alias != None:
        configDB(alias, host, port, dbname, username, password, engine)
        session = startDB(alias=alias)
    if alias == None:
        session = startDB(host=host, port=port, dbname=dbname, username=username, password=password, engine=engine)
    return session

def startDB(host=None, port=None, dbname=None, username=None, password=None, engine=None, alias=None):
    session = None
    if alias in data.keys():
        host, port, dbname, username, password, engine = itemgetter("host", "port", "dbname", "username", "password", "engine")(data[alias])
    if host != None and port != None and dbname != None and username != None and password != None and engine != None:
        if engine == None:
            if str(port) in default["engine"].keys():
                engine = default["engine"][str(port)]
        if tunnel.viewBindLocalAddressTunnel(host, port) != None:
            nhost = tunnel.viewBindLocalHostTunnel(host, port)
            nport = tunnel.viewBindLocalPortTunnel(host, port)
            host = nhost
            port = nport
        if engine in ["postgresql", "postgres", "postgre", "psql"]:
            session = _start_db_postgres_(host, port, dbname, username, password)
        if engine in ["redshift"]:
            session = _start_db_redshift_(host, port, dbname, username, password)
        if alias in data.keys():
            configSessionDB(alias, session)
    return session

def _start_db_postgres_(host, port, dbname, username, password):
    import psycopg2 as postgres
    return postgres.connect(host=host, port=port, database=dbname, user=username, password=password)

def _start_db_redshift_(host, port, dbname, username, password):
    import redshift_connector as redshift
    return redshift.connect(host=host, port=port, database=dbname, user=username, password=password)

def stopDB():
    pass

def configDB(alias, host, port, dbname, username, password, engine):
    ref = {"host": host, "port": port, "dbname": dbname, "username": username, "password": password, "engine": engine}
    _config_db_alias_(alias)
    for cred, value in ref.items():
        _config_db_cred_specific_(alias, cred, value)

def configHostDB(alias, value):
    _config_db_cred_specific_(alias, "host", value)

def configPortDB(alias, value):
    _config_db_cred_specific_(alias, "port", value)

def configNameDB(alias, value):
    _config_db_cred_specific_(alias, "dbname", value)

def configUsernameDB(alias, value):
    _config_db_cred_specific_(alias, "username", value)

def configPasswordDB(alias, value):
    _config_db_cred_specific_(alias, "password", value)

def configEngineDB(alias, value):
    _config_db_cred_specific_(alias, "engine", value)

def configSessionDB(alias, value):
    _config_db_cred_specific_(alias, "session", value)

def _config_db_cred_specific_(alias, cred, value):
    global data
    if cred in data[alias].keys():
        data[alias][cred] = value
    
def _config_db_alias_(alias):
    global data
    if alias not in data.keys():
        data[alias] = {
            "session": None
            , "host": None
            , "port": None
            , "dbname": None
            , "username": None
            , "password": None
            , "engine": None
        }

def viewCredentialDB(*alias):
    result = {}
    if len(alias) == 0:
        alias = data.keys()
    for nalias in alias:
        if type(nalias) == str:
            if len(alias) == 1:
                result = _view_db_cred_all_(nalias)
            if len(alias) != 1:
                result[nalias] = _view_db_cred_all_(nalias)
        if type(nalias) != str:
            pass
    return result
 
def _view_db_cred_all_(alias):
    host, port, dbname, username, password, engine = itemgetter("host", "port", "dbname", "username", "password", "engine")(data[alias])
    return {
        "host": host
        , "port": port
        , "dbname": dbname
        , "username": username
        , "password": password
        , "engine": engine
    }

def viewHostDB(*alias):
    return _view_db_cred_specific_("host", *alias)

def viewPortDB(*alias):
    return _view_db_cred_specific_("port", *alias)

def viewNameDB(*alias):
    return _view_db_cred_specific_("dbname", *alias)
       
def viewUsernameDB(*alias):
    return _view_db_cred_specific_("username", *alias)

def viewPasswordDB(*alias):
    return _view_db_cred_specific_("password", *alias)

def viewEngineDB(*alias):
    return _view_db_cred_specific_("engine", *alias)

def viewSessionDB(*alias):
    return _view_db_cred_specific_("session", *alias)

def _view_db_cred_specific_(cred, *alias):
    if len(alias) == 0:
        nalias = data.keys()
    if len(alias) != 0:
        nalias = alias
    result = {}
    for a in nalias:
        if len(nalias) == 1:
            result = data[a][cred]
        if len(nalias) > 1:
            result[a] = data[a][cred]
    return result