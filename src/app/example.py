import tkinter
import os

class AppExample:

    def __init__(self):
        self.pid = os.getpid()
        self.ppid = os.getppid()

        self.graphic()
        

    def fork_this_one(self):
        os.fork()

    def graphic(self):
        print('Hola mundo')
        print('App: ---> %s' % (self.pid, self.ppid))
