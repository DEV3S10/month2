import os
from pathlib import Path


def delete_file(file):
    fro = Path(f'/Users/dev3s/Desktop/2month/homework4/files/{file}')
    if fro.is_file():
        fro.unlink()
        print("File was deleted!")
    else:
        print("File not found!")



