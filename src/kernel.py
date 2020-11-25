from _thread import start_new_thread
import socket 

from lexer import check_sintaxis
from app_handler import AppHandler
from file_handler import FileHandler
from gui_handler import GuiHandler

class Kernel:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090
        self.kernel_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.kernel_socket.bind((self.host, self.port))

        self.module_client = None
        self.module_address = None

        self.modules_socket = {}

    def initialize_modules(self):
        self.kernel_socket.listen(3)
        while True:
            self.module_client, self.module_address = self.kernel_socket.accept()
            start_new_thread(self.module_connection, (self.module_client, self.module_address))

    def module_connection(self, module_client, module_address):
        pass

    def stop_connection(self):
        pass

if __name__ == "__main__":

    kernel = Kernel()
    kernel.initialize_modules()

    fh = FileHandler()
    fh.start_file_socket()

    gh = GuiHandler()
    gh.start_gui_socket()
