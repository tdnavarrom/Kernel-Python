import os
import socket
from threading import Thread

class FILE_MODULE:

    def __init__(self):
        self.path = os.getcwd()

        self.host = '127.0.0.1'
        self.port = 9091
        self.file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_socket.bind((self.host, self.port))

        self.file_client = None
        self.file_address = None

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
            self.rule = self.file_client.recv(1024).decode()
            command = self.rule.split(',')[3].split(':')[1].split()[0]
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
        elif 'halt' in command:
            self.connected = False

    def create_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.mkdir(full_path)
            self.file_client.send('Success create_dir'.encode('utf-8'))
        except:
            self.file_client.send('Failed create_dir'.encode('utf-8'))

    def delete_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.rmdir(full_path)
            self.file_client.send('Success delete_dir'.encode('utf-8'))
        except:
            self.file_client.send('Failed delete_dir'.encode('utf-8'))