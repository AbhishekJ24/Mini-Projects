import pygame

# A CLASS ACCOUNT THAT CAN HAVE INSTANCES FOR N NUMBER OF USERS, IT HAS A CONSTRUCTOR, A METHOD FOR CREDIT, DEBIT AND DISPLAYING BALANCE
class Account:
    def __init__(self):
        self.amount=0
        print("\n--------------------------------------------------------\n")
        print("\nACCOUNT CREATED AT PYTHON BANK SUCCESSFULLY")
    
    def credit(self,creditamt):
        self.amount+=creditamt
        print("CREDITED",creditamt,"SUCCESSFULLY!!")
    
    def debit(self,debitamt):
        self.amount-=debitamt
        print("DEBITED",debitamt,"SUCCESSFULLY!!")

    def displayBalance(self):
        print("CURRENT BALANCE:",self.amount)

# USING PYGAME TO LOAD A MUSIC FILE THAT PLAYS SIMULTANEOUSLY WHILE THE USER USES THE FUNCTIONALITY OF THE SCRIPT
pygame.init()
pygame.mixer.music.load('/Users/gamingspectrum24/Documents/PRG/Projects/Mini Projects/AccountSimulator/music.mp3')
pygame.mixer.music.play()

# CREATING AN OBJECT FOR USER 1 OF CLASS ACCOUNT
user1=Account()

# A MENU DRIVEN APPROACH TO SIMULATE AN ATM MACHINE THAT ENABLES THE USER TO CREDIT AND DEBIT MONEY AND DISPLAY THE BALANCE AND TERMINATE IF NOT REQUIRED

while True:
    choice=int(input("\nEnter your choice?\n1 for CREDIT\n2 for DEBIT\n3 for BALANCE DISPLAY\n4 for EXIT\n"))
    if choice==1:
        cre = int(input("AMOUNT: "))
        user1.credit(cre)
    elif choice==2:
        deb = int(input("AMOUNT: "))
        user1.debit(deb)
    elif choice==3:
        user1.displayBalance()
    elif choice==4:
        break
