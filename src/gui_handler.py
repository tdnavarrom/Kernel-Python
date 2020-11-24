from tkinter import *

import lexer

def kill_child_app(app_pid, child_pid):
    pass

def kill_app(app_pid):
    pass

def create_dir(dir_name):
    pass

def delete_dir(dir_name):
    pass

def get_log():
    pass

def list_commands():
    pass


if __name__=='__main__':
    window = Tk()
    window.title("NavPROS")
    window.geometry('700x700')

    label = Label(window, text="Crear Carpeta")
    label.grid(column=0, row=0)

    button = Button(window, text="Click Me")
    button.grid(column=1, row=0)

    window.mainloop()