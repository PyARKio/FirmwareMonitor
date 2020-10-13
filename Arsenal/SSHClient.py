# -- coding: utf-8 --
from __future__ import unicode_literals
import paramiko


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


# class SSHClient:
host = '192.168.0.74'
user = 'user'
secret = '123'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls -l')
data = stdout.read() + stderr.read()
print(data)
client.close()

