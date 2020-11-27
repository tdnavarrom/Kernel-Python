import os
import socket
import psutil
import subprocess
import platform
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

        self.parent_pid = []
        self.child_pids = []

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
            command = self.rule.split(',')[3].split(':')[1]
            print('message from kernel: ', command)
            self.set_rule(command)
            self.app_client.send('Executing instruction!.'.encode())

        self.app_client.close()

    def set_rule(self, command):
        if 'create_app' in command:
            self.create_app()
        elif 'create_child' in command:
            self.create_child()
        elif 'kill_app' in command:
            print(command)
            pid = int(command.split()[1])
            self.delete_app(pid)
        elif 'halt' in command:
            self.connected = False
        else:
            pass

    def create_app(self):
        system = platform.system()
        if system == "Windows":
            parent = subprocess.Popen('python app\example.py', cwd=os.path.dirname(os.path.realpath(__file__)))
        else:
            parent = subprocess.Popen(['python', 'app/example.py'])

        if len(self.parent_pid) == 0:
            self.parent_pid.append(parent.pid)
            print('pid del padre: ', parent.pid)
        else: print('Ya hay un proceso padre creado')
            

    def create_child(self):
        if len(self.parent_pid) != 0:
            system = platform.system()
            if system == "Windows":
                parent = subprocess.Popen('python app\example.py', cwd=os.path.dirname(os.path.realpath(__file__)))
            else:
                parent = subprocess.Popen(['python', 'app/example.py'])
            self.child_pids.append(parent.pid)
            print('pid del hijo: ', parent.pid)
        else:
            print('could not create child, parent not found')

    def delete_app(self, pid):

        if pid in self.parent_pid:
            p = psutil.Process(pid)
            p.terminate()
            if len(self.child_pids) != 0:
                print(self.child_pids)
                for i in self.child_pids:
                    p_c = psutil.Process(i)
                    p_c.terminate()
                    print('se murio el hijo: ', i)
                for i in self.child_pids:
                    self.child_pids.remove(i)
            self.parent_pid.remove(pid)
            print('Se murio el padre : ', pid)
        elif pid in self.child_pids:
            p = psutil.Process(pid)
            p.terminate()
            print('se murio el hijo: ', pid)
            self.child_pids.remove(pid)
        else:
            print('Error: no hay un proceso con ese nombre')
