#!/usr/bin/python
#
# Paramiko
#
import paramiko
import sys
import subprocess
#
# we instantiate a new object referencing paramiko's SSHClient class
#
vm = paramiko.SSHClient()
vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm.connect('192.168.115.103', username='osmanl', password='xxxxxx')
#
vmtransport = vm.get_transport()
dest_addr = ('10.103.53.26', 22) #edited#
local_addr = ('192.168.115.103', 22) #edited#
vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)
#
jhost = paramiko.SSHClient()
jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#jhost.load_host_keys('/home/osmanl/.ssh/known_hosts') #disabled#
jhost.connect('10.103.53.26', username='latiu', password='xxxx', sock=vmchannel)
#
stdin, stdout, stderr = jhost.exec_command("show version | no-more") #edited#
#
print stdout.read() #edited#
#
jhost.close()
vm.close()
# End




























# Set up the proxy (forwarding server) credentials
proxy_hostname = 'your.proxy.hostname'
proxy_username = 'proxy-username'
proxy_port = 22

# Instantiate a client and connect to the proxy server
proxy_client = SSHClient()
proxy_client.load_host_keys('~/.ssh/known_hosts/')
proxy_client.connect(
    proxy_hostname,
    port=proxy_port,
    username=proxy_username,
    key_filename='/path/to/your/private/key/'
)

# Get the client transport and open a `direct-tcpip` channel passing
# the destination hostname:port and the local hostname:port
transport = proxy_client.get_transport()
dest_addr = ('0.0.0.0', 8000)
local_addr = ('127.0.0.1', 1234)
channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

# Create a NEW client and pass this channel to it as the `sock` (along with
# whatever credentials you need to auth into your REMOTE box
remote_client = SSHClient()
remote_client.load_host_keys(hosts_file)
remote_client.connect('localhost', port=1234, username='remote_username', sock=channel)

# `remote_client` should now be able to issue commands to the REMOTE box
remote_client.exec_command('pwd')







import paramiko
from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(
    ('1.5.18.1', 22),
    ssh_username='user',
    ssh_pkey="/root/.ssh/id_rsa",
    ssh_private_key_password="userpass",
    remote_bind_address=("1.15.18.1", 22)
) as tunnel:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=tunnel.local_bind_host, port=tunnel.local_bind_port, username="root", password="remotepass")
    # do some operations with client session
    stdin, stdout, stderr = client.exec_command("./script >> output.txt")
    print stdout.channel.recv_exit_status()    # status is 0
    client.close()
print('FINISH!')












