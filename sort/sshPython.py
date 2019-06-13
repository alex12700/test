import paramiko 
 
host = '192.168.0.8'
user = 'login'
secret = 'password'
port = 22
 
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Подключение
client.connect(hostname=host, username=user, password=secret, port=port)
 
# Выполнение команды
stdin, stdout, stderr = client.exec_command('ls -l')
 
# Читаем результат
data = stdout.read() + stderr.read()
client.close()