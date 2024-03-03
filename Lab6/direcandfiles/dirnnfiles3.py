import os

def checkPath(path):
    if not os.path.exists:
        print(f"The path '{path}' does not exist.")
        return
    
    directory, filename = os.path.split(path)
    print(f"The path '{path}' exists.")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")

checkPath("pp2\Labs\lab6\Directories_and_Files/dirnfiles3.py") 