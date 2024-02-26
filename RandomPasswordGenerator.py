import random

passlist=[]
def passGenerator():
    digits = random.randrange(8,13)
    genPass = ""
    for i in range(digits):
        alpha=random.randrange(97,123)
        num=random.randrange(10)
        digoralpha=random.randrange(2)
        if digoralpha==1:
            genPass=genPass+chr(alpha)
        else:
            genPass=genPass+str(num)
    return genPass

genPass=passGenerator()
if (genPass not in passlist):
    passlist.append(genPass)
    print("Password Created Successfully!!\n",genPass,sep="")
else:
    print('Try something else')
    passGenerator()
