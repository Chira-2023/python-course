import random
from re import S
from tkinter import W


def gamewin(comp,you):
    if comp == you: 
        return None
    elif comp == "s":
        if you == "w":
            return False 
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False 
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False 
        elif you == "w":
            return True

comp = print("comp turn: snake(s) gun(g) water(w) ")
randno  = random.randint(1,3)
if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
else:
    comp = "g"
    
you = input("you turn: snake(s) gun(g) water(w): ")
print(f"comp choise {comp}")
print(f"your choise {you}")
result = gamewin(comp,you)
if result == True:
    print("you win")
elif result == False:
    print("you lose")
else:
    print("match tied")
