from operator import itemgetter

data = {}
bind_address = {}

# Configure and start SSH Tunnel
def setTunnel(host=None, port=None, username=None, password=None, password_mode=None, address_list=None, alias=None, *args, **kwargs):
    """
        Set Up Tunnel

        Configure and start SSH Tunnel to create a tunnel with randomized local address(es) to the specified remote address(es)

        Usage:
            1. Just configure using tunnel password and start without returning anything
                Run with the following format:
                < setTunnel("tunnel_alias", "tunnel_host", 1234, "tunnel_username", "tunnel_password", "pass", [("remote_host1", 1), ("remote_host2", 2)]) >

                then get your set up local address using the following format:
                < viewBindLocalAddress(remote_host, remote_port) >

            2. Configure, start and request a session in return
                Run with the following format:
                < setTunnel("tunnel_alias", "tunnel_host", 1234, "tunnel_username", "tunnel_password", "pass", [("remote_host1", 1), ("remote_host2", 2)], "session") >

    """
    if alias != None:
        configTunnel(alias, host, port, username, password, password_mode, address_list)
        session = startTunnel(alias=alias)
    if alias == None:
        session = startTunnel(host=host, port=port, username=username, password=password, mode=password_mode, remote_address=address_list)
    return session

# Start SSH Tunnel based on the stored information
def startTunnel(host=None, port=None, username=None, password=None, mode=None, remote_address=None, alias=None):
    from sshtunnel import SSHTunnelForwarder
    session = None
    if alias in data.keys():
        host, port, username, password, mode, remote_address = itemgetter("host", "port", "username", "password", "mode", "remote_address")(data[alias])
    if type(remote_address) == dict:
        nremote_address = []
        for remote_host, remote_port in remote_address.items():
            nremote_address.append((remote_host, remote_port))
        remote_address = nremote_address
    if host != None and port != None and username != None and password != None and mode != None and remote_address != None:
        passkey = None
        passphrase = None
        if mode == "pass":
            passphrase = password
        if mode == "pkey":
            passkey = password
        if mode == "rsa":
            passkey = _get_passkey_from_rsa_(password)
        session = SSHTunnelForwarder((host, port),ssh_username = username, ssh_pkey = passkey, ssh_password = passphrase, remote_bind_addresses = remote_address)
        session.start()
        if alias in data.keys():
            configSessionTunnel(alias, session)
        local_address = session.local_bind_addresses
        for index in range(0, len(remote_address)):
            remote_host, remote_port = remote_address[index]
            local_host, local_port = local_address[index]
            _config_tunnel_bind_address_(remote_host, remote_port, local_host, local_port)
    return session

# Configure SSH Tunnel
def configTunnel(alias, host, port, username, password, password_mode, address_list):
    ref = {"host": host, "port": port, "username": username, "password": password, "mode": password_mode, "remote_address": address_list}
    _config_tunnel_alias_(alias)
    for cred, value in ref.items():
        _config_tunnel_cred_specific_(alias, cred, value)

def configHostTunnel(alias, value):
    _config_tunnel_cred_specific_(alias, "host", value)

def configPortTunnel(alias, value):
    _config_tunnel_cred_specific_(alias, "port", value)

def configUsernameTunnel(alias, value):
    _config_tunnel_cred_specific_(alias, "username", value)

def configPasswordTunnel(alias, value):
    _config_tunnel_cred_specific_(alias, "password", value)

def configPasswordModeTunnel(alias, value):
    _config_tunnel_cred_specific_(alias, "mode", value)

def configRemoteAddressTunnel(alias, value):
    _config_tunnel_cred_specific_(alias, "remote_address", value)

def configSessionTunnel(alias, value):
    _config_tunnel_cred_specific_(alias, "session", value)

def _config_tunnel_cred_specific_(alias, cred, value):
    global data
    if cred in data[alias].keys():
        data[alias][cred] = value

def _config_tunnel_alias_(alias):
    global data
    if alias not in data.keys():
        data[alias] = {
            "session": None
            , "host": None
            , "port": None
            , "username": None
            , "password": None
            , "mode": None
            , "remote_address": None
        }

def _config_tunnel_bind_address_(remote_host, remote_port, local_host, local_port):
    global bind_address
    if remote_host not in bind_address.keys():
        bind_address[remote_host] = {}
    if str(remote_port) not in bind_address[remote_host].keys():
        bind_address[remote_host][str(remote_port)] = {"host": None, "port": None}
    bind_address[remote_host][str(remote_port)]["host"] = local_host
    bind_address[remote_host][str(remote_port)]["port"] = local_port

# View SSH Tunnel Configuration
def viewHostTunnel(*alias):
    return _view_tunnel_cred_specific_("host", *alias)

def viewPortTunnel(*alias):
    return _view_tunnel_cred_specific_("port", *alias)

def viewUsernameTunnel(*alias):
    return _view_tunnel_cred_specific_("username", *alias)

def viewPasswordTunnel(*alias):
    return _view_tunnel_cred_specific_("password", *alias)

def viewPasswordModeTunnel(*alias):
    return _view_tunnel_cred_specific_("mode", *alias)

def viewRemoteAddressTunnel(*alias):
    return _view_tunnel_cred_specific_("remote_address", *alias)

def viewSessionTunnel(*alias):
    return _view_tunnel_cred_specific_("session", *alias)

def _view_tunnel_cred_specific_(cred, *alias):
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

def viewBindLocalHostTunnel(remote_host, remote_port):
    result = viewBindLocalAddressTunnel(remote_host, remote_port)
    if result == None:
        return None
    if result != None:
        return result["host"]

def viewBindLocalPortTunnel(remote_host, remote_port):
    result = viewBindLocalAddressTunnel(remote_host, remote_port)
    if result == None:
        return None
    if result != None:
        return result["port"]

def viewBindLocalAddressTunnel(remote_host, remote_port):
    result = None
    if remote_host in bind_address.keys():
        if str(remote_port) in bind_address[remote_host]:
            result = bind_address[remote_host][str(remote_port)]
    return result

# Misc
def _get_passkey_from_rsa_(password):
    import io
    import paramiko

    # if "-----BEGIN RSA PRIVATE KEY-----" not in password:
    if password.__contains__("-----BEGIN RSA PRIVATE KEY-----") == False:
        password = "%s\n%s"%("-----BEGIN RSA PRIVATE KEY-----", password)
    # if "-----END RSA PRIVATE KEY-----" not in password:
    if password.__contains__("-----END RSA PRIVATE KEY-----") == False:
        password = "%s\n%s"%(password, "-----END RSA PRIVATE KEY-----")
    return paramiko.RSAKey.from_private_key(io.StringIO(password))