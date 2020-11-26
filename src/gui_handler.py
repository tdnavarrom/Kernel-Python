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
        self.window.resizable(False, False)

        self.frame = Frame(master=self.window, width=1200, height=700)
        self.frame.pack()

        self.label_title = Label(self.frame, text="Eternal OS", fg="black", font="Times 30")
        self.label_title.pack()

        self.wrapper1 = LabelFrame(self.window)
        self.wrapper1.pack(fill='both', expand="yes", padx=20, pady=10)

        self.wrapper2 = LabelFrame(self.window)
        self.wrapper2.pack(fill='both', expand="yes", padx=20, pady=10)

        self.wrapper3 = LabelFrame(self.window)
        self.wrapper3.pack(fill='both', expand="yes", padx=20, pady=10)

        self.create_folder_title = Label(self.wrapper1, text="Crear Carpeta", font="Times 20")
        self.create_folder_title.place(x=40, y=20, width=300, height=50)

        self.create_folder_label = Label(self.wrapper1, text="Nombre:")
        self.create_folder_label.place(x=100, y=70, width=50, height=25)

        self.create_folder_name = Entry(self.wrapper1, width=10)
        self.create_folder_name.place(x=155, y=70, width=50, height=25)

        def create_clicked():
            self.create_dir(self.create_folder_name.get())

        self.create_folder_button = Button(self.wrapper1, text="Crear", command=create_clicked)
        self.create_folder_button.place(x=210, y=70, width=50, height=25)

        self.delete_folder_title = Label(self.wrapper1, text="Eliminar Carpeta", font="Times 20")
        self.delete_folder_title.place(x=800, y=20, width=300, height=50)
        
        self.delete_folder_label = Label(self.wrapper1, text="Nombre:")
        self.delete_folder_label.place(x=860, y=70, width=50, height=25)

        self.delete_folder_name = Entry(self.wrapper1, width=10)
        self.delete_folder_name.place(x=915, y=70, width=50, height=25)

        def delete_clicked():
            self.delete_dir(self.delete_folder_name.get())

        self.delete_folder_button = Button(self.wrapper1, text="Eliminar", command=delete_clicked)
        self.delete_folder_button.place(x=970, y=70, width=50, height=25)

        def quit_clicked():
            self.stop_gui()

        self.quit_button = Button(self.window, text="Cerrar", command=quit_clicked)
        self.quit_button.place(x=550, y=600, width=50, height=25)

        self.window.mainloop()