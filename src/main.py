from kernel import Kernel
from gui_handler import GuiHandler
from file_handler import FileHandler
from app_handler import AppHandler


from threading import Thread
import time



if __name__ == "__main__":

    kernel = Kernel()
    gui = GuiHandler()
    fh = FileHandler()
    ah = AppHandler()

    file_thread = Thread(target=fh.start_file_socket, args=())
    file_thread.start()

    app_thread = Thread(target=ah.start_app_socket, args=())
    app_thread.start()

    kernel_thread = Thread(target=kernel.connection_with_modules, args=())
    kernel_thread.start()
    
    gui_thread = Thread(target=gui.start_gui_socket, args=())
    gui_thread.start()




    file_thread.join()
    app_thread.join()
    gui_thread.join()
    kernel_thread.join()

    
    
