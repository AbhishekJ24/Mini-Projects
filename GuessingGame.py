# GUESS THE NUMBER GAME - CODE WITH HARRY
import random
target=random.randint(0,100)
flag=0
print("\n\nGUESSING GAME\n--------------------------\nNOTE: YOU WILL HAVE 5 ATTEMPTS TO GUESS THE NUMBER\n")
for i in range (4,-1,-1):
    guess=int(input("Enter a number (from 0 to 100):\t\t\t({}CHANCES LEFT)\n".format(i+1)))
    if guess==target:
        print("BULLS EYE")
        flag=1
        break
    elif guess>target:
        print("GO FOR A LOWER NUMBER\n")
        continue
    elif guess<target:
        print("GO FOR A HIGHER NUMBER\n")
        continue
if flag==0:
    print("THE NUMBER WAS",target,".\nTRY AGAIN NEXT TIME")
else:
    pass