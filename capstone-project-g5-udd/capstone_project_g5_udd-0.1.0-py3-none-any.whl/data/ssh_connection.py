import paramiko


def ssh_connection(hostname: str, username: str, password: str):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=password)
    return ssh_client.open_sftp()
