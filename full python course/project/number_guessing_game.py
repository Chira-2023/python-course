import random

num = int(input("guess your no. between 1 to 100\n"))
compnum = random.randint(1,100)
def guess(comp,num):
    if compnum<num:
        num = int(input("guess lover no.\n"))
        guess(comp,num) 
    elif compnum>num:
        num = int(input("guess higher no.\n"))
        guess(comp,num)
    elif compnum == num:
        num1 = num
        print(f"guess no. {compnum} and your no.{num1} is same")
        

guess(compnum,num)

