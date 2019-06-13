import paramiko 

host = '212.8.234.46'
user = 'judchin'
secret = 'ENDifyQQ1'
port = 5554

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls -l')
data = stdout.read() + stderr.read()
print(data)
client.close()