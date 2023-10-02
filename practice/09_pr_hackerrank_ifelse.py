n = int(input("Enter your value"))
f = n%2
if f == 1:
    print("weird")
elif f == 0:
    if n >2 and n<5:
        print("Not weird")
    elif n < 20 and n > 6:
        print("weird")
    else:
        print("Not weird")