import os
import socket
from threading import Thread

class AppHandler:

    def __init__(self):
        self.path = os.getcwd()

        self.host = '127.0.0.1'
        self.port = 5556
        self.app_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.app_socket.bind((self.host, self.port))

        self.module_client = None
        self.module_address = None

    def start_app_socket(self):
        self.app_socket.listen(1)
        self.module_client, self.module_address = self.app_socket.accept()
        print('App --> Kernel connected!!..')
        self.kernel_connection_thread = Thread(target=self.connection, args=())
        self.kernel_connection_thread.start()
        self.kernel_connection_thread.join()
        

    def connection(self):
        self.connected = True
        

        while self.connected:
            print('App --> Waiting kernel instruction.....')
            rule = self.module_client.recv(1024).decode()
            print('App --> message from kernel: ', rule)
            self.set_rule(rule)
            self.module_client.send('Succesfull!'.encode())

        self.app_socket.close()

    def set_rule(self, command):
        if 'create_app' in command and len(command) == 1:
            self.create_app()
        elif 'create_child' in command and len(command) == 1:
            self.create_child()
        elif 'exit':
            self.connected = False

    def create_app(self):
        print('App created')

    def create_child(self):
        print('Child created')

    def get_info(self):
        pass

    def get_info_childs(self):
        pass

    def kill_childs(self):
        pass

    def kill_child(self):
        pass