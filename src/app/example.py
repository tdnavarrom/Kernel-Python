import tkinter
import os

class AppExample:

    def __init__(self):
        print('App instance created')
        self.pid = os.getpid()
        self.ppid = os.getppid()

    def graphic(self):
        print('App: ---> pid: %s, parent: %s' %(self.pid, self.ppid))


if __name__ == "__main__":
    AppExample().graphic()
    while True:
        pass