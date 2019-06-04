import os


def open_file(file_name):
    file_info = os.stat(file_name)
    if os.path.isfile(file_name) and file_info.st_size != 0:
        with open(file_name, 'r') as of:
            print(of.read())
    else:
        print("nie ma takiego pliku")


def save_file(file_name, save_content):
    if os.path.isfile(file_name):
        print("ten plik już istnieje i nie może zostać nadpisany")
    else:
        with open(file_name, 'a+') as sf:
            sf.write(save_content)

