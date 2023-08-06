import os
import time

#[PATH SELECT]:
path=""
flag=0

while True:
    #[DEFAULT PATH]:
    print("------------------------------------")
    print(r"SUGGESTION : C:\Users\junil\Desktop\Python\Projects\Project 1 - TO DO Application")
    print("------------------------------------")
    path=input("ENTER THE PATH WHERE YOUR TO-DO.py FILE IS PRECENT : ")
    try:
        while True:
            os.chdir(path)
            print("------------------------------------")
            if os.path.isfile("TO-DO.py"):
                print("------------------------------------")
                print("FILE FOUND SUCCESSFULLY!")
                print("------------------------------------")
                flag=1
                break
            else:
                print("------------------------------------")
                print("FILE NOT FOUND IN THIS DIRECTORY!")
                print("------------------------------------")
                path=input("RE ENTER THE PATH WHERE YOUR TO-DO.py FILE IS PRESENT : ")
                continue
        if flag==1:
            break
    except:
        print("------------------------------------")
        print("YOU ENTERED INVALID DIRECTORY PATH!")
        print("------------------------------------")

print()
print()
print("OPENING TO-DO.py: [ ",end="")

print("|",end=" ")
time.sleep(1)

print("|",end=" ")
time.sleep(1)

print("|",end=" ")
time.sleep(1)

print("|",end=" ")
time.sleep(1)

print("|",end=" ")
time.sleep(1)

print("|",end=" ")
time.sleep(1)

print(" ]")
print()
print()

os.system('python '+path+'/TO-DO.py')