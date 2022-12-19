import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno, showinfo
from Data.generate_sha256 import generate_sha256, find_duplicates
import time
import shutil

if __name__ == '__main__':
    Tk().withdraw()
    directory = askdirectory(title="Select Folder To Scan For Duplicates")
    if os.path.exists(directory):
        ts = time.perf_counter()
        hashes = generate_sha256(directory)
        tf = time.perf_counter()
        print(f"{tf - ts} || {os.cpu_count()}")
        duplicates = find_duplicates(hashes)
        duplicates_length = len(duplicates)
        print(f"Found {duplicates_length} duplicate files")
        if duplicates_length > 0:
            move_files = askyesno(title="Delete Duplicates", message=f"Found {duplicates_length} duplicates,"
                                                                   f" would you like to move them to a /Duplicates "
                                                                   f"folder?")
        else:
            showinfo(title="Finished", message="No duplicates found.")
        if not os.path.exists(f"{directory}/Duplicates"):
            os.mkdir(f"{directory}/Duplicates")
        if move_files:
            for file in duplicates:
                if os.path.exists(file):
                    shutil.move(file, f"{directory}/Duplicates")
            showinfo(title="Files Removed", message=f"{len(duplicates)} files have been moved.")
