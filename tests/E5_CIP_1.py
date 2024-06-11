import os

def read_file(file_name):

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, file_name)

    f=open(file_path,"r")
    data=f.read()
    f.close()
    return data