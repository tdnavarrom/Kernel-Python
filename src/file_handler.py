import os
import socket
from threading import Thread

class FileHandler:

    def __init__(self):
        self.path = os.getcwd()

        self.host = '127.0.0.1'
        self.port = 5555
        self.file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_socket.bind((self.host, self.port))

        self.module_client = None
        self.module_address = None

    def start_file_socket(self):
        self.file_socket.listen(1)
        self.module_client, self.module_address = self.file_socket.accept()
        print('File --> Kernel connected!!..')
        self.kernel_connection_thread = Thread(target=self.connection, args=())
        self.kernel_connection_thread.start()
        self.kernel_connection_thread.join()
        

    def connection(self):
        self.connected = True
        

        while self.connected:
            print('File --> Waiting kernel instruction.....')
            rule = self.module_client.recv(1024).decode()
            print('File --> message from kernel: ', rule)
            self.set_rule(rule)
            self.module_client.send('Succesfull!'.encode())

        self.file_socket.close()

    def set_rule(self, command):
        command = command.strip().split()
        if 'create_dir' in command and len(command) == 2:
            self.create_dir(command[1])
        elif 'rm_dir' in command and len(command) == 2:
            self.delete_dir(command[1])
        elif 'exit':
            self.connected = False

    def create_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.mkdir(full_path)
            print('File --> Success: Folder created succesfully')
        except:
            print('File --> Error: The folder may already exist or the given path is incorrect.')

    def delete_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.rmdir(full_path)
            print('File --> Success: Folder deleted succesfully')
        except:
            print('File --> Error: The folder may doesn\'t exist or the given path is incorrect.')