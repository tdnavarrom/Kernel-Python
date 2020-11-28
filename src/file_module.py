import os
import socket
from threading import Thread
from datetime import datetime

class FILE_MODULE:

    def __init__(self):
        self.path = os.getcwd()

        self.host = '127.0.0.1'
        self.port = 9091
        self.file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_socket.bind((self.host, self.port))

        self.file_client = None
        self.file_address = None

        self.writer = None

        self.msg_structure = "cmd:{}, src:{}, dst:{}, msg:{}"

        self.initialize_log()

    def initialize_log(self):
        folder_name = 'transactional_log'
        try:
            if (not os.path.isdir(os.path.join(self.path, folder_name))):
                os.mkdir(os.path.join(self.path, folder_name))
                self.writer = open(os.path.join(self.path, folder_name, 'log.txt'), 'w')
        except:
            print('Error')

    def start_file_socket(self):
        connected = False

        while(not connected):
            self.file_socket.listen(1)
            self.file_client, self.file_address = self.file_socket.accept()
            if(self.file_client != None):
                connected = True
        print('file socket has stablished a connection with kernel')
        self.connection()

    def connection(self):
        self.connected = True

        while self.connected:
            self.rule = self.file_client.recv(1024).decode('utf-8')
            command = self.rule.split(',')[3].split(':', 1)[1].split()[0]
            print('message from kernel: ', command)
            self.set_rule(command)

        self.file_client.close()

    def set_rule(self, command):
        if 'create_dir' in command:
            file_name = self.rule.split(',')[3].split(':')[1].split()[1]
            self.create_dir(file_name)
        elif 'delete_dir' in command:
            file_name = self.rule.split(',')[3].split(':')[1].split()[1]
            self.delete_dir(file_name)
        elif 'Log' in command:
            self.write_log(self.rule)
        elif 'halt' in command:
            self.writer.close()
            self.connected = False

    def create_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.mkdir(full_path)
            cmd = 'send'
            origin = 'file_module'
            destiny = 'gui_module'
            msg = ' Log: ' + str(datetime.now()) + '-> success create_dir ' + name
            self.file_client.send((self.msg_structure.format(cmd, origin, destiny, msg)).encode())
        except:
            cmd = 'send'
            origin = 'file_module'
            destiny = 'gui_module'
            msg = ' Log: ' + str(datetime.now()) + '-> failed create_dir ' + name
            self.file_client.send((self.msg_structure.format(cmd, origin, destiny, msg)).encode())

    def delete_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.rmdir(full_path)
            cmd = 'send'
            origin = 'file_module'
            destiny = 'gui_module'
            msg = ' Log: ' + str(datetime.now()) + '-> success delete_dir ' + name
            self.file_client.send((self.msg_structure.format(cmd, origin, destiny, msg)).encode())
        except:
            cmd = 'send'
            origin = 'file_module'
            destiny = 'gui_module'
            msg = ' Log: ' + str(datetime.now()) + '-> failed delete_dir ' + name
            self.file_client.send((self.msg_structure.format(cmd, origin, destiny, msg)).encode())

    def write_log(self, command):
        try:
            self.writer.write(command + '\n')
        except:
            cmd = 'send'
            origin = 'file_module'
            destiny = 'gui_module'
            msg = ' Log: ' + str(datetime.now()) + '-> failed write_log '
            self.file_client.send((self.msg_structure.format(cmd, origin, destiny, msg)).encode())