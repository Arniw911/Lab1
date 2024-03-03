#Ex 1
import os

def dir(path, list_all): 

    for dir_name in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_name)):
            print(dir_name)
            if list_all:
                dir(os.path.join(path, dir_name))

def files(path,list_all):
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            print(file_name)
        if list_all and os.path.isdir(os.path.join(path, file_name)):
            files(os.path.join(path, file_name), True)


files("../", True)



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

check("2.py")



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
counter = 0

f = open("example.txt","w") 
for i in range(1,10+1):
        f.write(str(i)+"\n")
f.close()        

f = open("example.txt","r")
for i in f:
    counter+=1
    
print(counter)        



#Ex 5
def listToStr(lst):
    mystr = "["
    for i in lst:
        mystr+=i+", "
    if len(lst)>0:    
        mystr = mystr[:-2]
    mystr+="]"
    return mystr    

lst = [x for x in "RANDOM STRING"]

with open("list.txt","w") as f:
    f.write(listToStr(lst))



#Ex 6
for j in [chr(i) for i in range(65,91)]:
    f = open(f"{j}.txt", "w")
    f.close()



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
            print(f"The file '{path}' was removed.")
        else:
            print(f"The file '{path}' is not executable.")
    else:
        print(f"The path '{path}' is a directory, so executability is not applicable.")


deleteFile("this_file_will_be_removed.txt")
