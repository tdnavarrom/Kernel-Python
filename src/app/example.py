from tkinter import *
import os

class AppExample:

    def __init__(self):
        print('App instance created')
        self.pid = os.getpid()

    def graphic(self):
        window = Tk()
        window.title("App")
        window.geometry('600x300')
        window.resizable(False, False)

        label = Label(window, text="PID: " + str(self.pid), font="Times 20")
        label.place(x=150, y=100, width=300, height=60)

        window.mainloop()

if __name__ == "__main__":
    AppExample().graphic()