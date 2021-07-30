import subprocess
import sys
import os
print('----------Welcome to "Setup Project" applycation create by thanhdauxuan--------')
con = input('Exit: 0\nContinue:1\n')
con = int(con)
if con == 0:
    sys.exit("See you later")
num = input("Project type?\n--0:C++||1:Java||2:JavaS||3:Python||4:Other---\nEnter:")
num = int(num)
condition = num!=0 and num != 1 and num != 2 and num !=3 and num != 4
while condition:
    num = input("Not exist projecttype!\nPlease enter again: ")
    num = int(num)
    condition = num!=0 and num != 1 and num != 2 and num !=3 and num != 4
direc = 'D:\COMPSCI_STU\PL'
filename = input("Enter the filename: ")
if num == 0:
    direc += '\Cpp'
    num_ = input('-----Type?(0:Exercise||1:Other)------\n') 
    if num_ == "0":
        direc += '\ex'
    elif num_ == "1":
        direc += '\Temp'
    else :
        sys.exit("Wrong!")
elif num == 1:
    direc +='\Java'
elif num == 2:
    direc += '\JavaS'
elif num == 3:
    direc += '\Python'
elif num == 4:
    direc += '\Other'
    print('Creat new folder?(yes/no)')
    log = input()
    if log == 'yes' :
        folder = input("Namefolder: ")
        os.chdir(direc)
        os.mkdir(folder)
        cwd = os.getcwd()
        os.chdir(cwd + chr(92) + folder)
        with open(filename, "a") as file:
            if num == 0:
                file.write("#include <iostream>\nint main() {\n\n\n    return 0;\n}")
        subprocess.run('code .', shell=True)
        sys.exit("See you later")
os.chdir(direc)
with open(filename, "a") as file:
    if num == 0:
        file.write("#include <iostream>\nint main() {\n\n\n    return 0;\n}")
subprocess.run('code .',shell=True)
sys.exit("See you later")


