import os

class FileHandler:

    def __init__(self):
        super().__init__()
        self.path = os.getcwd()

    def get_command(self):
        pass

    def create_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.mkdir(full_path)
            print('Success: Folder created succesfully')
        except:
            print('Error: The folder may already exist or the given path is incorrect.')

    def delete_dir(self, name):
        try:
            full_path = os.path.join(self.path, name)
            os.rmdir(full_path)
            print('Success: Folder deleted succesfully')
        except:
            print('Error: The folder may doesn\'t exist or the given path is incorrect.')

    def get_dir_name(self):
        pass