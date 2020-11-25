import os
import socket

class FileHandler:

    def __init__(self):
        self.path = os.getcwd()

        self.host = '127.0.0.1'
        self.port = 9090
        self.file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_file_socket(self):
        try:
            self.file_socket.connect((self.host, self.port))
            print("hola desde file")
        except socket.error as e:
            print("hola desde file error")
            print(str(e))
        finally:
            self.file_socket.close()

    def set_rule(self, command):
        command = command.strip().split()
        if 'create_dir' in command and len(command) == 2:
            self.create_dir(command[1])
        elif 'rm_dir' in command and len(command) == 2:
            self.delete_dir(command[1])

    def create_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.mkdir(full_path)
            print('Success: Folder created succesfully')
        except:
            print('Error: The folder may already exist or the given path is incorrect.')

    def delete_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.rmdir(full_path)
            print('Success: Folder deleted succesfully')
        except:
            print('Error: The folder may doesn\'t exist or the given path is incorrect.')