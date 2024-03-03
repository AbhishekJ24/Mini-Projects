import datetime
def getDate():
    return datetime.datetime.now()
print("\n\n~~~~~~~~~~~~~~ ABHISHEK'S HEALTH MANAGEMENT SYSTEM WELCOMES YOU ~~~~~~~~~~~~~~\n")
repeater=1
while(repeater):
    f1=open('USER1Food.txt','a')
    f2=open('USER2Food.txt','a')
    f3=open('USER3Food.txt','a')
    f4=open('USER1Exercise.txt','a')
    f5=open('USER2Exercise.txt','a')
    f6=open('USER3Exercise.txt','a')
    menuoption=int(input("DO YOU WANT TO INPUT LOGS OR PRINT LOGS FOR THE THREE CLIENTS\n1 FOR INPUTTING\n2 FOR PRINTING\n3 FOR EXIT\n"))
    if menuoption==1:
        choice=int(input("\nEnter your choice of client:\n1 for USER 1\n2 for USER 2\n3 for USER 3\n"))
        ch=int(input("\nEnter your choice, whether you want to log food or exercise:\n1 for FOOD\n2 FOR EXERCISE\n"))
        if choice==1:
            if ch==1:
                times=int(input("\nEnter the number of foods you want to log: "))
                print("Enter the food name:\n")
                for i in range(0,times):
                    food=input()
                    st=str(getDate())+"\t"+food.upper()+"\n"
                    f1.write(st)
            elif ch==2:
                times=int(input("\nEnter the number of exercises you want to log: "))
                print("Enter the exercise name:")
                for i in range(0,times):
                    exercise=input()
                    st=str(getDate())+"\t"+exercise.upper()+"\n"
                    f4.write(st)
        if choice==2:
            if ch==1:
                times=int(input("\nEnter the number of foods you want to log: "))
                print("Enter the food name:\n")
                for i in range(0,times):
                    food=input()
                    st=str(getDate())+"\t"+food.upper()+"\n"
                    f2.write(st)
            elif ch==2:
                times=int(input("\nEnter the number of exercises you want to log: "))
                print("Enter the exercise name:")
                for i in range(0,times):
                    exercise=input()
                    st=str(getDate())+"\t"+exercise.upper()+"\n"
                    f5.write(st)
        if choice==3:
            if ch==1:
                times=int(input("\nEnter the number of foods you want to log: "))
                print("Enter the food name:\n")
                for i in range(0,times):
                    food=input()
                    st=str(getDate())+"\t"+food.upper()+"\n"
                    f3.write(st)
            elif ch==2:
                times=int(input("\nEnter the number of exercises you want to log: "))
                print("Enter the exercise name:")
                for i in range(0,times):
                    exercise=input()
                    st=str(getDate())+"\t"+exercise.upper()+"\n"
                    f6.write(st)
    elif menuoption==2:
        f1=open('USER1Food.txt','r')
        f2=open('USER2Food.txt','r')
        f3=open('USER3Food.txt','r')
        f4=open('USER1Exercise.txt','r')
        f5=open('USER2Exercise.txt','r')
        f6=open('USER3Exercise.txt','r')
        nch=int(input("\nEnter your choice of client:\n1 for USER 1\n2 for USER 2\n3 for USER 3\n"))
        lch=int(input("\nEnter your choice, whether you want to print food log or exercise log:\n1 for FOOD\n2 FOR EXERCISE\n"))
        if nch==1:
            if lch==1:
                print(f1.read())
            elif lch==2:
                print(f4.read())
            else:
                pass
        elif nch==2:
            if lch==1:
                print(f2.read())
            elif lch==2:
                print(f5.read())
            else:
                pass
        elif nch==3:
            if lch==1:
                print(f3.read())
            elif lch==2:
                print(f6.read())
            else:
                pass
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()
    elif menuoption==3:
        print("\nTHANK YOU FOR VISITING US")
        repeater=0
    else:
        print("INVALID CHOICE ENTERED")
        repeater=0
    print("\n-----------------------------------------------------------\n")