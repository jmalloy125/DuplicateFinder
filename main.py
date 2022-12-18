import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from Data.generate_sha256 import generate_sha256, find_duplicates
import time

if __name__ == '__main__':
    Tk().withdraw()
    directory = askdirectory()
    ts = time.perf_counter()
    hashes = generate_sha256(directory)
    tf = time.perf_counter()
    print(f"{tf - ts} || {os.cpu_count()}")
    duplicates = find_duplicates(hashes)
    print(f"Found {len(duplicates)} duplicate files")
    for file in duplicates:
        if os.path.exists(file):
            os.remove(file)
        else:
            print("Did not exist")
