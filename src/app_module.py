import os
import socket
import signal
from threading import Thread
from app.example import AppExample

class APP_MODULE:

    def __init__(self):
        self.path = os.getcwd()

        self.host = '127.0.0.1'
        self.port = 9092
        self.app_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.app_socket.bind((self.host, self.port))

        self.app_client = None
        self.app_address = None

    def start_app_socket(self):
        connected = False

        while(not connected):
            self.app_socket.listen(1)
            self.app_client, self.app_address = self.app_socket.accept()
            if(self.app_client != None):
                connected = True
        print('app socket has stablished a connection with kernel')
        self.connection()

    def connection(self):
        self.connected = True

        while self.connected:
            self.rule = self.app_client.recv(1024).decode()
            command = self.rule.split(',')[3].split(':')[1].split()[0]
            print('message from kernel: ', command)
            self.set_rule(command)

        self.app_client.close()

    def set_rule(self, command):
        if 'create_app' in command:
            self.create_app()
        elif 'delete_app' in command:
            self.delete_app(pid)
        elif 'create_child' in command:
            self.create_child()
        elif 'delete_child' in command:
            self.delete_child(pid)
        elif 'halt' in command:
            self.connected = False
        else:
            pass

    def create_app():
        self.parent = AppExample()

    def create_child():
        if self.parent != None:
            self.parent.fork_this_one()
        else:
            print('could not create child, parent not found')

    def delete_app(pid):
        os.kill(pid, signal.SIGTERM)

    def delete_child(pid):
        os.kill(pid, signal.SIGTERM)