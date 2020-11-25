from tkinter import *
import socket

class GuiHandler:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090
        self.gui_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.window = None

        self.graphical_interface()

    def start_gui_socket(self):
        try:
            self.gui_socket.connect((self.host, self.port))
            print("hola desde gui")
        except socket.error as e:
            print("hola desde gui error")
            print(str(e))

    def kill_child_app(self, app_pid, child_pid):
        pass

    def kill_app(self, app_pid):
        pass

    def create_dir(self, dir_name):
        pass

    def delete_dir(self, dir_name):
        pass

    def get_log(self):
        pass

    def graphical_interface(self):
        self.window = Tk()
        self.window.title("NavPROS")
        self.window.geometry('1200x700')
        label = Label(self.window, text="Crear Carpeta")
        label.grid(column=0, row=0)

        button = Button(self.window, text="Click Me")
        button.grid(column=1, row=0)

        self.window.mainloop()