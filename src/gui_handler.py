from tkinter import *
import socket

class GuiHandler:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090
        self.gui_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.window = None

    def start_gui_socket(self):
        try:
            self.gui_socket.connect((self.host, self.port))
            print("hola desde gui")
            self.graphical_interface()
        except socket.error as e:
            print("hola desde gui error")
            print(str(e))
            

    def stop_gui(self):
        self.gui_socket.send(('exit').encode('utf-8'))
        response = self.gui_socket.recv(1024).decode()

        if response == 'OK':
            print('Closing Down!! Please close the window now safely')
            self.gui_socket.close()

    def kill_child_app(self, app_pid, child_pid):
        pass

    def kill_app(self, app_pid):
        pass

    def create_dir(self, dir_name):
        print('Creating Dir')
        self.gui_socket.send(('create_dir ' + str(dir_name)).encode('utf-8'))
        response = self.gui_socket.recv(1024).decode()

        if response == 'OK':
            print('Finished Creating Dir')


    def delete_dir(self, dir_name):
        print('Deleting Dir')
        self.gui_socket.send(('rm_dir ' + str(dir_name)).encode('utf-8'))
        response = self.gui_socket.recv(1024).decode()

        if response == 'OK':
            print('Finished Deleting Dir')

    def get_log(self):
        pass

    def graphical_interface(self):
        self.window = Tk()
        self.window.title("Eternal OS")
        self.window.geometry('1200x700')

        create_folder_label = Label(self.window, text="Nombre:")
        create_folder_label.grid(column=30, row=0)

        self.create_folder_name = Entry(self.window, width=10)
        self.create_folder_name.grid(column=32, row=0)

        def create_clicked():
            self.create_dir(self.create_folder_name.get())

        create_folder_button = Button(self.window, text="Crear", command=create_clicked)
        create_folder_button.grid(column=45, row=0)

        delete_folder_label = Label(self.window, text="Nombre:")
        delete_folder_label.grid(column=100, row=0)

        self.delete_folder_name = Entry(self.window, width=10)
        self.delete_folder_name.grid(column=102, row=0)

        def delete_clicked():
            self.delete_dir(self.delete_folder_name.get())

        delete_folder_button = Button(self.window, text="Eliminar", command=delete_clicked)
        delete_folder_button.grid(column=115, row=0)

        def quit_clicked():
            self.stop_gui()

        quit_button = Button(self.window, text="Cerrar", command=quit_clicked)
        quit_button.grid(column=350, row=1200)

        self.window.mainloop()