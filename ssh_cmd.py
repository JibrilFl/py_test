import time
import socket
import os
from datetime import datetime

import eel
import paramiko
from scp import SCPClient

def read_file():
    with open('outs.txt') as file:
        text = file.read()
        return text

@eel.expose
def host_down(ip, port='22', user='user', passwd='123456789', cmd=f'echo "{read_file()}" | sudo tee /etc/hosts'):

    mess = ''

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=user, password=passwd)
    except socket.timeout:
        mess = [1, f'Время подключения к ip:{ip} истекло --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess
    except paramiko.SSHException as error:
        mess = [1, f'Возникла ошибка {error} --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess
    except paramiko.ssh_exception.NoValidConnectionsError as error:
        mess = [1, f'Ошибка подключения к ip:{ip} --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()

    if output:
        file = open('outs_test.txt', 'w')
        for line in output:
            file.write(line.strip() + '\n')
        file.close()

    client.close()

    return [output, mess]



@eel.expose
def vnc_down(ip, port='22', user='user', passwd='123456789'):

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=user, password=passwd)
    except socket.timeout:
        mess = [1, f'Время подключения к ip:{ip} истекло --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess
    except paramiko.SSHException as error:
        mess = [1, f'Возникла ошибка {error} --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess
    except paramiko.ssh_exception.NoValidConnectionsError as error:
        mess = [1, f'Ошибка подключения к ip:{ip} --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess

    with SCPClient(client.get_transport()) as scp:
        scp.put('VNC-Server-6.7.2-Linux-x64.deb', recursive=True, remote_path='~/VNC.deb')


    with open('KEY.txt') as file:
        for line in file:
            _, stdout, stderr = client.exec_command(line)
            time.sleep(1)
        mess = [0, 'VNC установлен']


    scp.close()
    client.close()

    return mess

# ssh_command('10.74.43.80')

# 10.74.43.80
# 10.74.43.24
# echo "hello" | sudo tee -a /etc/hosts-test
# f'echo "{read_file()}" | sudo tee /etc/hosts-test'
# 'cat /etc/hosts-test'
# sudo /etc/init.d/networking restart

@eel.expose
def crypto_down(ip, port='22', user='user', passwd='123456789'):

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=user, password=passwd)
    except socket.timeout:
        mess = [1, f'Время подключения к ip:{ip} истекло --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess
    except paramiko.SSHException as error:
        mess = [1, f'Возникла ошибка {error} --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess
    except paramiko.ssh_exception.NoValidConnectionsError as error:
        mess = [1, f'Ошибка подключения к ip:{ip} --- {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}']
        return mess

    with SCPClient(client.get_transport()) as scp:
        scp.put('VNC-Server-6.7.2-Linux-x64.deb', recursive=True, remote_path='~/VNC.deb')


    with open('KEY.txt') as file:
        for line in file:
            _, stdout, stderr = client.exec_command(line)
            time.sleep(1)
        mess = [0, 'VNC установлен']


    scp.close()
    client.close()

    return mess

eel.init('.\web')
eel.start('index.html', size=(600, 260))

