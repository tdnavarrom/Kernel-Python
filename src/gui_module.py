import socket
from tkinter import *
from threading import Thread

class GUI_MODULE:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090
        self.gui_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gui_socket.bind((self.host, self.port))

        self.gui_client = None
        self.gui_address = None

        self.window = None

        self.msg_structure = "cmd:{}, src:{}, dst:{}, msg:{}"

    def start_gui_socket(self):
        connected = False

        while(not connected):
            self.gui_socket.listen(1)
            self.gui_client, self.gui_address = self.gui_socket.accept()
            if(self.gui_client != None):
                connected = True
        print('Gui socket has stablished a connection with kernel')
        self.grapical_interface()

    def stop_gui(self):
        print('Stopping gui')
        cmd = 'info'
        origin = 'gui_module'
        destiny = 'kernel'
        msg = 'halt'
        self.gui_client.send(self.msg_structure.format(cmd, origin, destiny, msg).encode('utf-8'))
        self.gui_client.close()
        self.window.destroy()

    def kill_child_app(self, app_pid, child_pid):
        pass

    def kill_app(self, app_pid):
        pass

    def create_dir(self, dir_name):
        print('Creating Dir')
        cmd = 'info'
        origin = 'gui_module'
        destiny = 'file_module'
        msg = 'create_dir ' + str(dir_name)
        self.gui_client.send((self.msg_structure.format(cmd, origin, destiny, msg)).encode('utf-8'))
        self.messages_gui_kernel.set(self.msg_structure.format(cmd, origin, destiny, msg))

    def delete_dir(self, dir_name):
        print('Deleting Dir')
        cmd = 'info'
        origin = 'gui_module'
        destiny = 'file_module'
        msg = 'delete_dir ' + str(dir_name)
        self.gui_client.send((self.msg_structure.format(cmd, origin, destiny, msg)).encode('utf-8'))
        self.messages_gui_kernel.set(self.msg_structure.format(cmd, origin, destiny, msg))

    def get_log(self):
        pass

    def grapical_interface(self):
        # Main Window
        self.window = Tk()
        self.window.title("Eternal OS")
        self.window.geometry('1200x700')
        self.window.resizable(False, False)

        # Frame
        self.frame1 = Frame(master=self.window, width=1200, height=700)
        self.frame1.pack()

        self.label_title = Label(self.frame1, text="Eternal OS", fg="black", font="Times 30")
        self.label_title.pack()

        # Wrapper 1
        self.wrapper1 = LabelFrame(self.window)
        self.wrapper1.pack(fill='both', expand="yes", padx=20, pady=10)

        self.create_folder_title = Label(self.wrapper1, text="Crear Carpeta", font="Times 20")
        self.create_folder_title.place(x=40, y=20, width=300, height=50)

        self.create_folder_label = Label(self.wrapper1, text="Nombre:")
        self.create_folder_label.place(x=100, y=70, width=50, height=25)

        self.create_folder_name = Entry(self.wrapper1, width=10)
        self.create_folder_name.place(x=155, y=70, width=50, height=25)

        def create_clicked():
            self.create_dir(self.create_folder_name.get())
            self.create_folder_name.delete(0, END)

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
            self.delete_folder_name.delete(0, END)

        self.delete_folder_button = Button(self.wrapper1, text="Eliminar", command=delete_clicked)
        self.delete_folder_button.place(x=970, y=70, width=50, height=25)

        # Wrapper 2
        self.wrapper2 = LabelFrame(self.window)
        self.wrapper2.pack(fill='both', expand="yes", padx=20, pady=10)

        # Wrapper 3
        self.wrapper3 = LabelFrame(self.window)
        self.wrapper3.pack(fill='both', expand="yes", padx=20, pady=10)

        self.messages_gui_kernel_title = Label(self.wrapper3, text="Gui Messages", font="Times 20")
        self.messages_gui_kernel_title.place(x=40, y=20, width=300, height=50)

        self.messages_gui_kernel = StringVar()
        self.messages_gui_kernel_label = Label(self.wrapper3, textvariable=self.messages_gui_kernel)
        self.messages_gui_kernel_label.place(x=0, y=80, width=400, height=30)

        self.messages_file_kernel_title = Label(self.wrapper3, text="File Messages", font="Times 20")
        self.messages_file_kernel_title.place(x=420, y=20, width=300, height=50)

        self.messages_file_kernel = StringVar()
        self.messages_file_kernel.set("Hola")
        self.messages_file_kernel_label = Label(self.wrapper3, textvariable=self.messages_file_kernel)
        self.messages_file_kernel_label.place(x=500, y=80, width=100, height=30)

        self.messages_app_kernel_title = Label(self.wrapper3, text="App Messages", font="Times 20")
        self.messages_app_kernel_title.place(x=860, y=20, width=200, height=50)

        # Wrapper 4
        def quit_clicked():
            self.stop_gui()

        self.wrapper4 = LabelFrame(self.window)
        self.wrapper4.pack(fill='both', expand="yes", padx=20, pady=10)

        self.quit_button = Button(self.wrapper4, text="Cerrar", command=quit_clicked)
        self.quit_button.place(x=550, y=50, width=50, height=25)

        self.window.mainloop()
