import os

os.system('ssh judchin@212.8.234.46 -L 5554:127.0.0.1:5554')
os.system('ssh odroid@10.8.0.14 -L 5554:192.168.1.117:554')

print("finish")