from threading import Thread
import socket 

import lexer as lx

class Kernel:

    def __init__(self):
        self.host = '127.0.0.1'
        
        #GUI CONNECTION
        self.port = 9090
        self.gui_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gui_socket.bind((self.host, self.port))

        #FILE CONNECTION
        self.fport = 5555
        self.file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #FILE CONNECTION
        self.aport = 5556
        self.app_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.module_client = None
        self.module_address = None

    
    def connection_with_modules(self):
        self.gui_socket.listen(1)
        self.module_client, self.module_address = self.gui_socket.accept()

        try:
            self.file_socket.connect((self.host, self.fport))
        except socket.error as e:
            print(str(e))

        try:
            self.app_socket.connect((self.host, self.aport))
        except socket.error as e:
            print(str(e))

        self.gui_thread = Thread(target=self.gui_methods_handler, args=(self.module_client,))
        self.gui_thread.start()     


        self.gui_thread.join()
        
    
    def gui_methods_handler(self, module_client):
        
        self.connected = True

        while self.connected:
            print('Connection of GUI has been stablished')

            rule = module_client.recv(1024).decode()
            status = lx.check_sintaxis(rule)

            module_client.send(status.encode())

            if status == 'OK':
                if rule == 'exit':
                    self.stop_connection(rule)    
                
                elif 'rm_dir' in rule or 'create_dir' in rule:
                    self.file_thread = Thread(target=self.file_methods_handler, args=(rule,))
                    self.file_thread.start()
                    self.file_thread.join()
                elif rule == 'create_app' or rule == 'create_child':
                    pass
                else:
                    print('rule not found ', rule)

        
        module_client.close()
    
    def file_methods_handler(self, rule):
        
        self.file_socket.send(rule.encode())
        response = self.file_socket.recv(1024).decode()

        print(response)

    def app_handler(self, rule):
        self.app_socket.send(rule.encode())
        response = self.app_socket.recv(1024).decode()

        print(response)


    def stop_connection(self, rule):

        print('Shutting down!..')
        self.connected = False  
        self.file_socket.send(rule.encode())
        self.file_socket.send(rule.encode())
        self.file_socket.close()
        self.app_socket.close()