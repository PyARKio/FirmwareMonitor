# -- coding: utf-8 --
from __future__ import unicode_literals
import paramiko


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class UnblockSSH:
    def __init__(self, **kwargs):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.kwargs = kwargs

    def __enter__(self):
        kw = self.kwargs
        self.client.connect(hostname=kw.get('hostname'), username=kw.get('username'),
                            password=kw.get('password'), port=int(kw.get('port', 22)),
                            key_filename=kw.get('key_filename'))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        data = stdout.read()

        stdin.write('{}\n'.format(self.kwargs.get('password')))
        stdin.flush()

        return data.decode()


class SCP:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.remotepath = kwargs.get('remotepath')
        self.localpath = kwargs.get('localpath')
        self.transport = None
        self.sftp = None

    def __enter__(self):
        kw = self.kwargs
        self.transport = paramiko.Transport((kw.get('hostname'), int(kw.get('port', 22))))
        self.transport.connect(username=kw.get('username'), password=kw.get('password'))
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sftp.close()
        self.transport.close()

    def sftp_put(self):
        return self.sftp.put(self.localpath, self.remotepath)

    def sftp_get(self):
        return self.sftp.get(self.remotepath, self.localpath)


if __name__ == '__main__':
    with UnblockSSH(hostname='cloud.bron.ua', username='ubuntu', password='123', port=22, key_filename='/home/bron/cloud/bron_su.pem') as ssh:
        out = ssh.exec_cmd('ls -la')
        print(out)
    #
    # with SCP(hostname='192.168.0.200', username='user', password='123', port=22,
    #          remotepath='/home/user/gas_1.0_120_arm64.deb',
    #          localpath='/media/qwerty/Back-UP/Firmwares/gas/120___2020_08_19T09_05_05Z/DEB/gas_1.0_120_arm64.deb') as ssh:
    #     out = ssh.sftp_put()
    #     print(out)

    # import subprocess '(psql -U postgres -h 0.0.0.0 cloud -c \\\"select ip_address from tablet where serial_number =\'ce5bbea33c8e6c60\'\\\")'
    #
    # command = 'ssh -i /home/bron/cloud/bron_su.pem ubuntu@cloud.bron.ua'
    #
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    # proc_stdout, proc_stderr = process.communicate()
    # print(proc_stdout)

"""
add update enable/disable (dpkg -s app -> modify in cloud)

"""
