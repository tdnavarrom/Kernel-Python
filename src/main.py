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
    
    print('Welcome to NavPROS V0.01!!!!!')
    
    connected=True
    
    while(connected):
        command = input("> ").strip()

        status = lexer.check_sintaxis(command)

        if status != 'OK':
            print('Error: Command not found, please use \'help\' command to se available commands ')
            continue
        
        if status == 'OK' and command == "exit":
            connected=False

        if status == 'OK':
            pass