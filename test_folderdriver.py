import os
import subprocess

def open_folder(path):
    print(path)
    with subprocess.Popen(path) as folder:
        print(folder)
