from kernel import Kernel
from gui_handler import GuiHandler

from threading import Thread
from time import time



if __name__ == "__main__":

    kernel = Kernel()
    fh = kernel.fh
    gh = kernel.gh

    kernel_thread = Thread(target=kernel.gui_connection, args=())
    kernel_thread.start()
    
    gui_thread = Thread(target=gh.start_gui_socket, args=())
    gui_thread.start()


    gui_thread.join()
    kernel_thread.join()


    
    
