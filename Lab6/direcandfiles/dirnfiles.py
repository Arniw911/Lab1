#Ex 1
import os

def listdir(path):
    print("Directories:")
    listofdir = []
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            listofdir.append(entry)
    return listofdir
    
def listfiles(path):
    print("Files:")
    listoffiles = []
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            listoffiles.append(entry)
    return listoffiles
    
def listdirfiles(path):
    print("Directories and Files:")
    listofdirfiles = []
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)) or os.path.isdir(os.path.join(path, entry)):
            listofdirfiles.append(entry)
    return listofdirfiles

print(listdir("C:/Users/user/Desktop/English"))
print(listfiles("C:/Users/user/Desktop/English"))
print(listdirfiles("C:/Users/user/Desktop/English"))



#Ex 2 
import os

def check(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    if os.access(path, os.R_OK):
        print(f"You can read the path '{path}'.")
    else:
        print(f"You cannot read the path '{path}'.")

    if os.access(path, os.W_OK):
        print(f"You can write to the path '{path}'.")
    else:
        print(f"You cannot write to the path '{path}'.")

    if os.path.isfile(path):
        if os.access(path, os.X_OK):
            print(f"The file '{path}' can be executed.")
        else:
            print(f"The file '{path}' cannot be executed.")
    else:
        print(f"The path '{path}' is a directory, so we don't check for executability.")

check("dirnfiles.py")



#Ex 3
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



#Ex 4
def countl(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

filename = 'here input path'
line_count = countl(filename)
print(f"The number of lines in the file '{filename}' is {line_count}.")    



#Ex 5
def writelist(list_items, filename):
    with open(filename, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")

my_list = ['apple', 'banana', 'cherry']
filename = 'my_list.txt'

writelist(my_list, filename)
print(f"The list has been written to the file '{filename}'.")



#Ex 6
import string

def generatefiles():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {letter}.txt")

generatefiles()
print("26 text files have been generated.")



#Ex 7
f = open("theFile.txt")
content = f.read()
f.close()

duplicate = open("duplicate.txt","w")
duplicate.write(content)
duplicate.close()



#Ex8
import os

def deleteFile(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist")
        return

    if os.path.isfile(path):
        if os.access(path,os.X_OK):
            os.remove(path)
            print(f"The file '{path}' has been removed.")
        else:
            print(f"The file '{path}' is not executable.")
    else:
        print(f"The path '{path}' is a directory, so we don't check for executability.")


deleteFile("this_file_will_be_removed.txt")
