from threading import Thread
import socket 

import lexer as lx
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
        self.initialize_modules()

    def initialize_modules(self):
        self.fh = FileHandler()
        self.gh = GuiHandler()
        self.ah = AppHandler()

    def gui_connection(self):
        self.kernel_socket.listen(1)
        self.module_client, self.module_address = self.kernel_socket.accept()
        print('GUI-CONNECTION SUCCESFULL')
        gui_thread = Thread(target = self.module_connection, args=())
        gui_thread.start()

        methods_thread = Thread(target = self.gui_method_handler, args=())
        methods_thread.start()

        methods_thread.join()
        gui_thread.join()
        self.kernel_socket.close()

    def module_connection(self):
        self.gh.graphical_interface()
        self.gh.gui_socket.close()

    def gui_method_handler(self):
        connected = True
        print('Initializing connection with Modules!...')
        while connected:
            print('Modules connected!...')
            rule = self.module_client.recv(1024).decode()
            print('Addr: ',  self.module_address, ' RULE: ', rule)

            status = lx.check_sintaxis(rule)

            self.module_client.send(status.encode('utf-8'))

            if status == 'OK':

                if rule == 'exit':
                    print("connection closed from addr: ", self.module_address)
                    self.module_client.send(rule.encode('utf-8'))
                    connected = False
                elif 'create_dir' in rule or 'rm_dir' in rule:
                    print(rule)
                    self.file_methods_handler(rule)
                else:
                    print('ERROR, COMMAND NOT FOUND')
            else:
                self.module_client.send('Bad rule: Please Check the available instructions \n'.encode('utf-8'))


    def file_methods_handler(self, rule):
        self.fh.set_rule(rule)
        

    def file_delete_handler(self, module_client):
        pass

    def stop_connection(self):
        pass