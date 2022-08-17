import os
from pathlib import Path


def create_file(file_name, extension):
    fp = Path(f'/Users/dev3s/Desktop/2month/homework4/files/{file_name}.{extension}')
    if not fp.exists():
        fp = open(f'/Users/dev3s/Desktop/2month/homework4/files/{file_name}.{extension}', 'a').close()
        print("Crete!")
        print(os.path.abspath(file_name))
    else:
        print("Uzhe Est")




