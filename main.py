import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno, showinfo
from Data.generate_sha256 import generate_sha256, find_duplicates
import time

if __name__ == '__main__':
    Tk().withdraw()
    directory = askdirectory(title="Select Folder To Scan For Duplicates")
    if os.path.exists(directory):
        ts = time.perf_counter()
        hashes = generate_sha256(directory)
        tf = time.perf_counter()
        print(f"{tf - ts} || {os.cpu_count()}")
        duplicates = find_duplicates(hashes)
        print(f"Found {len(duplicates)} duplicate files")
        delete_files = askyesno(title="Delete Duplicates", message=f"Found {len(duplicates)} duplicates, would you like to delete them?")
        if delete_files:
            for file in duplicates:
                if os.path.exists(file):
                    os.remove(file)
            showinfo(title="Files Removed", message=f"{len(duplicates)} files have been deleted.")
