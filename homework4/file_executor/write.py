import os
from pathlib import Path


def write(file, body):
    fro = Path(f'/Users/dev3s/Desktop/2month/homework4/files/{file}')
    if fro.exists():
        open(f'/Users/dev3s/Desktop/2month/homework4/files/{file}', 'a').write(body)
        print("Update!")
    else:
        print("File not found!")







