import socket 

from lexer import check_sintaxis
from app_handler import AppHandler
from file_handler import FileHandler

class Kernel:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090
        self.kernel_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.kernel_socket.bind((self.host, self.port))

        self.file_module_client = None
        self.file_module_address = None

    def initialize_app_module(self):
        pass

    def initialize_file_module(self):
        fh = FileHandler()
        fh.start_file_socket()
        self.kernel_socket.listen(1)

        self.file_module_client, self.file_module_address = self.kernel_socket.accept()

    def initialize_gui_module(self):
        pass

    def module_connection(self):
        pass

    def stop_connection(self):
        pass

    def write_log(self):
        pass