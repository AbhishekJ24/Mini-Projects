# ABHISHEK JOSHI
# SNAKE WATER GAME - CODE WITH HARRY
import random
print("\n\n~~~~~~~~~~~~~~~ ABHISHEK'S SNAKE WATER GUN GAME WELCOMES YOU ~~~~~~~~~~~~~~~\n")
options=["SNAKE","WATER","GUN"]
counter=10
user_count=0
comp_count=0
while(counter!=0):
    choice=input("Enter your choice\n1. SNAKE\n2. WATER\n3. GUN\n").upper()
    comp_choice=random.choice(options)
    if choice == comp_choice:
        print("TIE\nUSER: {}\nCOMPUTER: {}\n{}\n---------------------------------------\n".format(user_count,comp_count,comp_choice))
    else:
        if choice == "SNAKE" and comp_choice == "WATER":
            user_count=user_count+1
            print("WIN\nUSER: {}\nCOMPUTER: {}\n{}\n---------------------------------------\n".format(user_count,comp_count,comp_choice))
        elif choice == "WATER" and comp_choice == "SNAKE":
            comp_count=comp_count+1
            print("LOSE\nUSER: {}\nCOMPUTER: {}\n{}\n---------------------------------------\n".format(user_count,comp_count,comp_choice))
        elif choice == "GUN" and comp_choice == "SNAKE":
            user_count=user_count+1
            print("WIN\nUSER: {}\nCOMPUTER: {}\n{}\n---------------------------------------\n".format(user_count,comp_count,comp_choice))
        elif choice == "SNAKE" and comp_choice == "GUN":
            comp_count=comp_count+1
            print("LOSE\nUSER: {}\nCOMPUTER: {}\n{}\n---------------------------------------\n".format(user_count,comp_count,comp_choice))
        elif choice == "WATER" and comp_choice == "GUN":
            user_count=user_count+1
            print("WIN\nUSER: {}\nCOMPUTER: {}\n{}\n---------------------------------------\n".format(user_count,comp_count,comp_choice))
        elif choice == "GUN" and comp_choice =="WATER":
            comp_count=comp_count+1
            print("LOSE\nUSER: {}\nCOMPUTER: {}\n{}\n---------------------------------------\n".format(user_count,comp_count,comp_choice))
        else:
            print("INVALID INPUT")
            exit
    counter=counter-1
if comp_count>user_count:
    print("YOU LOSE THE GAME\nBETTER LUCK NEXT TIME!!!")
elif comp_count<user_count:
    print("YOU WON THE GAME\nCONGRATULATIONS!!!")
else:
    print("YOU TIED THE GAME\nSMOOTH!!!")