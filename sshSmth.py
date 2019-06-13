import paramiko
from sshtunnel import SSHTunnelForwarder


REMOTE_SERVER_IP = ''
PRIVATE_SERVER_IP

with SSHTunnelForwarder(
    (REMOTE_SERVER_IP, 5554),
    ssh_username="",
    ssh_pkey="/var/ssh/rsa_key",
    ssh_private_key_password="secret",
    remote_bind_address=(PRIVATE_SERVER_IP, 554),
    local_bind_address=('127.0.0.1', 5554)
) as tunnel:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1', 10022)
    # do some operations with client session
    client.close()

print('FINISH!')