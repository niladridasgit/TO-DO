from datetime import datetime
from playsound import playsound
import time
import os

#[PATH SELECT]:
path=""
while True:
    #[DEFAULT PATH]:
    print("------------------------------------")
    print(r"SUGGESTION : C:\Users\junil\Desktop\Python\Projects\Project 1 - TO DO Application")
    print("------------------------------------")
    path=input("ENTER THE PATH OF MUSIC DIRECTORY : ")
    try:
        os.chdir(path)
        print("------------------------------------")
        print("DIRECTORY CHANGED SUCCESSFULLY.")
        print("------------------------------------")
        break
    except:
        print("------------------------------------")
        print("YOU ENTERED INVALID DIRECTORY PATH!")
        print("------------------------------------")

#[MUSIC SELECT]:
music=""
while True:
    #[DEFAULT MUSIC]:
    print("------------------------------------")
    print("SUGGESTION : Baarish")
    print("------------------------------------")
    music=input("ENTER THE NAME OF THE MUSIC [mp3] FILE : WITHOUT EXTENSION : ")
    if os.path.isfile(music+".mp3"):
        print("------------------------------------")
        print("MUSIC FOUND SUCCESSFULLY!")
        print("------------------------------------")
        break
    else:
        print("------------------------------------")
        print("YOU ENTERED INVALID MUSIC PATH!")
        print("------------------------------------")

#[TO DO LIST]:
TO_DO_LIST={}

print("------------------------------------")
print("THE TIME FORMAT IS : 24 HOURS\nSTART TIME : 00:00:00\nEND TIME : 23:59:59")
print("------------------------------------")

#[TO DO FUNCTION]:
def TO_DO(destination_goal,destination_hour,destination_minute):
    print("------------------------------------")
    print("YOUR NEXT GOAL IS : ["+destination_goal+"] AT : "+str(destination_hour)+":"+str(destination_minute))
    
    now=datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    print("------------------------------------")
    print("CURRENT TIME IS : ",current_time)
    print("------------------------------------")

    current_hour = int(now.strftime("%H"))
    current_minute = int(now.strftime("%M"))
    
    while True:
        now=datetime.now()

        if destination_hour<int(now.strftime("%H")):
            print("------------------------------------")
            print("TIME PASSED!\nYOU ENTERED EITHER YESTERDAY'S TIME OR TOMORROW'S TIME!\nPLEASE ENTER TODAY'S TIME.")
            print("------------------------------------")
            break
        #else:
        if destination_hour>=int(now.strftime("%H")):
            if destination_minute<int(now.strftime("%M")) and destination_hour==int(now.strftime("%H")):
                print("------------------------------------")
                print("IT'S NOT TODAY!\nYOU ENTERED EITHER YESTERDAY'S TIME OR TOMORROW'S TIME!\nPLEASE ENTER TODAY'S TIME.")
                print("------------------------------------")
                break

            goal=destination_goal
            
            #IF THE DESTINATION HOUR IS SAME AS THE CURRENT HOUR:
            if destination_hour==current_hour:
                time_to_reach=destination_minute-current_minute
            #IF THE DESTINATION HOUR IS SAME AS THE CURRENT HOUR+1: 
            elif destination_hour==current_hour+1:
                time_to_reach=(60-current_minute)+destination_minute
            #IF THE DESTINATION TIME IS MORE THAN THE CURRENT HPUR+1:
            else:
                time_to_reach=(destination_hour-current_hour-1)*60+(60-current_minute)+destination_minute
            
            #COUNTDOWN: 
            print("------------------------------------")
            print("COUNTDOWN : ")
            print("------------------------------------")
            if time_to_reach<=10:
                for i in range(time_to_reach,0,-1):
                    print("{} MINUTES TO REACH THE GOAL [{}]".format(i,goal))
                    time.sleep(60)
            else:
                for i in range(time_to_reach,0,-10):
                    if i<=10:
                        for j in range(i,0,-1):
                            print("{} MINUTES TO REACH THE GOAL [{}]".format(j,goal))
                            time.sleep(60)
                    else:
                        print("{} MINUTES TO REACH THE GOAL [{}]".format(i,goal))
                        time.sleep(60*10)
            
            now=datetime.now()
            if destination_minute==int(now.strftime("%M")):
                if destination_goal.upper()=="SHUTDOWN":
                    print("------------------------------------")
                    print("DESTINATION TIME IS REACHED : ",now.strftime("%H:%M:%S"))
                    for i in range(0,10,1):
                        time.sleep(2)
                        print(".")
                    print("")
                    time.sleep(40)
                    print("------------------------------------")
                    os.system("shutdown /s /t 1")
                print("------------------------------------")
                print("DESTINATION TIME IS REACHED : ",now.strftime("%H:%M:%S"))
                #ACCESS THE SONG HERE: 
                playsound(music+'.mp3')
                print("------------------------------------")
                break
    print("------------------------------------")

#[MENU DRIVEN FUNCTIONS]:
def menu():
    print("------------------------------------")
    print("\nPRESS : [delete]\nPRESS : [add]\nPRESS : [start]\nPRESS : [display]\nPRESS : [edit]\n")
    print("------------------------------------")
    command=input("PRESS : ")
    print("------------------------------------")
    return command

def add():
    keyCount=0
    print("------------------------------------")
    task=input("ENTER THE TASK NAME : ")
    print("------------------------------------")
    while True:
        hour,minute=input("ENTER THE TIME : \n[hour] : "),input("[minute] : ")
        if int(hour)<0 or int(hour)>=24:
            print("------------------------------------")
            print("INVALID ENTRY OF HOUR!\nYOU ENTERED HOUR<0 AND HOUR>24")
            print("------------------------------------")
        else:
            if int(minute)<0 or int(minute)>=60:
                print("------------------------------------")
                print("INVALID ENTRY OF MINUTE!\nYOU ENTERED MINUTE<0 AND MINUTE>24")
                print("------------------------------------")
            else:
                break
    print("------------------------------------")
    flag=0
    location=""
    if len(TO_DO_LIST)==0:
        pass
    else:
        for key in TO_DO_LIST:
            if TO_DO_LIST[key][0]==hour:
                if TO_DO_LIST[key][1]==minute:
                    flag=1
                    location=TO_DO_LIST[key][2]
                    break
    if flag==0:
        keyCount+=len(TO_DO_LIST)
        TO_DO_LIST[keyCount]=[hour,minute,task]
        print("TASK IS ADDED INTO THE TASK LIST.")
        print("------------------------------------")
    if flag==1:
        print(location+" IS POINTED TO THE SAME TIME YOU ENTERED ON THE TASK LIST : "+str(hour)+":"+str(minute))
        print("SO, WE CAN NOT ADD THIS TASK.")
        print("------------------------------------")

def display():
    print("------------------------------------")
    print("TASK LIST OF TODAY : ")
    print("------------------------------------")
    if len(TO_DO_LIST)==0:
        print("TILL NOW NO ELEMENT IN THE LIST.")
        print("------------------------------------")
        pass
    else:
        i=0
        for key in TO_DO_LIST:
            print("[TASK {}] : {:>50} | {:>10}:{} ".format(key,TO_DO_LIST[key][2].upper(),TO_DO_LIST[key][0],TO_DO_LIST[key][1]))
            i+=1
    print("------------------------------------")

def delete():
    print("------------------------------------")
    task=input("ENTER THE TASK NAME : ")
    print("------------------------------------")
    if len(TO_DO_LIST)==0:
        print("NO ELEMENT IN THE LIST.")
        print("------------------------------------")
        pass
    else:
        flag=0
        location=0
        for key in TO_DO_LIST:
            if task.upper()==TO_DO_LIST[key][2].upper():
                flag=1
                location=key
                break
        if flag==1:
            del TO_DO_LIST[location]
        else:
            print("------------------------------------")
            print("TASK IS NOT PRESENT IN THE LIST.")
            print("------------------------------------")

def edit():
    print("------------------------------------")
    task=input("ENTER THE TASK NAME [WHICH TASK YOU WANT TO EDIT] : ")
    print("------------------------------------")
    if len(TO_DO_LIST)==0:
        print("NO ELEMENT IN THE LIST.")
        print("------------------------------------")
        pass
    else:
        flag=0
        location=0
        for key in TO_DO_LIST:
            if task.upper()==TO_DO_LIST[key][2].upper():
                flag=1
                location=key
                break
        if flag==1:
            print("------------------------------------")
            choose=input("EDIT THE TASK [NAME/TIME] : \nCHOOSE : ")
            print("------------------------------------")
            if choose.upper()=="NAME":
                print("------------------------------------")
                print("TASK OLD NAME : ",TO_DO_LIST[location][2])
                name=input("ENTER TASK NEW NAME : ")
                TO_DO_LIST[location][2]=name
                print("------------------------------------")
            else:
                print("TASK OLD TIME : {}:{}".format(TO_DO_LIST[location][0],TO_DO_LIST[location][1]))
                while True:
                    hour,minute=input("ENTER TASk NEW TIME :\n[hour] : "),input("[minute] : ")
                    if int(hour)<0 or int(hour)>=24:
                        print("------------------------------------")
                        print("INVALID ENTRY OF HOUR!\nYOU ENTERED HOUR<0 AND HOUR>24")
                        print("------------------------------------")
                    else:
                        if int(minute)<0 or int(minute)>=60:
                            print("------------------------------------")
                            print("INVALID ENTRY OF MINUTE!\nYOU ENTERED MINUTE<0 AND MINUTE>24")
                            print("------------------------------------")
                        else:
                            break
                TO_DO_LIST[location][0]=hour
                TO_DO_LIST[location][1]=minute
            print("------------------------------------")
        else:
            print("------------------------------------")
            print("TASK IS NOT PRESENT IN THE LIST.")
            print("------------------------------------")

#[MENU DRIVEN]:
command=menu()

while command.lower()!="start":
    print("------------------------------------")
    print("THE NUMBER OF ELEMENTS IN THE TASK LIST IS : ",len(TO_DO_LIST))
    print("------------------------------------")
    #ADD A TASK: 
    if command.lower()=="add":
        add()
    #DISPLAY THE TASK(S):
    if command.lower()=="display":
        display()
    
    #DELETE A TASK:
    if command.lower()=="delete":
        delete()
    
    #EDIT A TASK:
    if command.lower()=="edit":
        edit()

    command=menu()

#[SORTING TIME]:
print("------------------------------------")
print("THE NUMBER OF ELEMENTS IN THE TASK LIST IS : ",len(TO_DO_LIST))
display()
print("------------------------------------")

print("------------------------------------")
print("SORT THE LIST ACCORDING TO THE TIME : ")
print("------------------------------------")
for key1 in TO_DO_LIST:
    for key2 in TO_DO_LIST:
        if key1==key2:
            break
        else:
            if int(TO_DO_LIST[key1][0])*100+int(TO_DO_LIST[key1][1])<=int(TO_DO_LIST[key2][0])*100+int(TO_DO_LIST[key2][1]):
                TO_DO_LIST[key1],TO_DO_LIST[key2]=TO_DO_LIST[key2],TO_DO_LIST[key1]
            else:
                continue

#[DISPLAY THE TASK WHEN START]:
print("------------------------------------")
display()
print("------------------------------------")

#[SHUTDOWN TIME SETTING]:
sdH=0
sdM=0
print("------------------------------------")
while True:
    print("------------------------------------")
    choose=input("YOU WANT TO SET THE SHUTDOWN TIMER : [yes/no]\nCHOOSE :")
    print("------------------------------------")
    if choose.upper()=="NO":
        break
    sdH,sdM=input("WHEN YOW WANT TO SHUT DOWN YOUR PC : \n[hour] : "),input("[minute] : ")
    if int(sdH)<0 or int(sdH)>=24:
        print("------------------------------------")
        print("INVALID ENTRY OF HOUR!\nYOU ENTERED HOUR<0 AND HOUR>24")
        print("------------------------------------")
    else:
        if int(sdM)<0 or int(sdM)>=60:
            print("------------------------------------")
            print("INVALID ENTRY OF MINUTE!\nYOU ENTERED MINUTE<0 AND MINUTE>24")
            print("------------------------------------")
        else:
            break
print("------------------------------------")

#[START FOLLOWING THE LIST]: 
for key in TO_DO_LIST:
    TO_DO(TO_DO_LIST[key][2].upper(),int(TO_DO_LIST[key][0]),int(TO_DO_LIST[key][1]))
TO_DO("SHUTDOWN",int(sdH),int(sdM))