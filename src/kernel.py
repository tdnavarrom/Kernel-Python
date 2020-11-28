import socket
from threading import Thread

from gui_module import GUI_MODULE
from file_module import FILE_MODULE
from app_module import APP_MODULE

class Kernel:


    def __init__(self):
        self.host = '127.0.0.1'

        #GUI CONNECTION
        self.gui_port = 9090
        self.gui_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #FILE CONNECTION
        self.file_port = 9091
        self.file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #APP CONNECTION
        self.app_port = 9092
        self.app_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.msg_structure = "cmd:{}, src:{}, dst:{}, msg:{}"

    def initialize_connections(self):
        try:
            self.gui_socket.connect((self.host, self.gui_port))
            self.file_socket.connect((self.host, self.file_port))
            self.app_socket.connect((self.host, self.app_port))

            self.connection_handle_thread = Thread(target=self.connection_handler, args=())
            self.connection_handle_thread.start()

            self.connection_handle_thread.join()

        except socket.error as e:
            print(str(e))

    def connection_handler(self):
        connected = True

        while connected:
            msg = self.gui_socket.recv(1024).decode('utf-8')
            arguments = msg.split(',')
            cmd = arguments[0].split(':')[1]
            dst = arguments[2].split(':')[1]

            if cmd == "info":
                if dst == "file_module":
                    self.file_socket.send(msg.encode())
                    response = self.file_socket.recv(1024).decode()
                    self.gui_socket.send(response.encode())
                    self.file_socket.send(response.encode())
                elif dst == "app_module":
                    self.app_socket.send(msg.encode())
                    response = self.app_socket.recv(1024).decode()
                    self.gui_socket.send(response.encode())
                    self.file_socket.send(response.encode())
                elif dst == "kernel":
                    if arguments[3].split(':')[1] == "halt":
                        connected = False
                        cmd = 'info'
                        origin = 'kernel'
                        msg = 'halt'
                        self.file_socket.send((self.msg_structure.format(cmd, origin, 'file_module', msg)).encode())
                        self.app_socket.send((self.msg_structure.format(cmd, origin, 'app_module', msg)).encode())
                        self.file_socket.close()
                        self.app_socket.close()
                        self.gui_socket.close()

if __name__ == "__main__":
    gui_module = GUI_MODULE()
    gui_thread = Thread(target=gui_module.start_gui_socket, args=())
    gui_thread.start()

    file_module = FILE_MODULE()
    file_thread = Thread(target=file_module.start_file_socket, args=())
    file_thread.start()

    app_module = APP_MODULE()
    app_thread = Thread(target=app_module.start_app_socket, args=())
    app_thread.start()

    kernel_module = Kernel()
    kernel_thread = Thread(target=kernel_module.initialize_connections, args=())
    kernel_thread.start()

    file_thread.join()
    app_thread.join()
    gui_thread.join()
    kernel_thread.join()
   