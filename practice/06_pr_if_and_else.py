## Q1 write a program to find gretest no. of 4 no. input by user
# from turtle import pen


# a = int(input("Enter 1 no."))
# b = int(input("Enter 2 no."))
# c = int(input("Enter 3 no."))
# d = int(input("Enter 4 no."))
# if a>d:
#     f1 = a
# else :
#     f1 = d    

# if b>c:
#     f2 = b    
# else:
#     f2 = c    

# if f1>f2:
#     print(f1, "is grestes")
# else:
#     print(f2 , "is grestes")    






## Q2 write a program to declre the persentage of student on school based 
# from ast import If


# p = int(input("Enter your physics marks out of 100 :"))
# c = int(input("Enter your chemistry marks out of 100 :"))
# m = int(input("Enter your math marks out of 100 :"))

# per = (p+c+m)/3
# print(per)
# if p<33 or c<33 or m<33:
#     print("you are fail because you have less 33% marks in one of the sub.")
# elif per>33.33 and per<48:
#     print("you are pass by grace")    
# elif per>48 and per <85:
#     print("congratulation! you are pass by B grade")    
# else:
#     print("congratulation! you are pass with A grade")    







## Q3 write a program to detect a spam

# text = input("Enter the text\n")

# if "video call on what'app" in text:
#     spam = True
# elif "send your OTP " in text:
#     spam = True    
# elif "buy this" in text :
#     spam = True    
# else:
#     spam = False    

# if spam:
#     print("this is a spam")    
# else:
#     print("this is not a spam")






## Q4 write a program to find length of the text input by user 
# name = input("Enter your name \n")
# print("your name character is ",len(name))
# if (len(name))<10:
#     print("your name length is less then 10")
# else:
#     print("your name length is greter then 10") 






## Q5 write a program to find out the name is present on list or not 
NameList = ["chirag arya", "Rahul arya", "Uma bharti","Neha arya"]
c = "Rahul arya"
if c in NameList:
    print("this name in the list")
else:
    print("this name is not in list ")    






## Q6 write a prorgram to the gradeing system on in school
m = int(input("Enter your maths marks \n"))
s = int(input("Enter your science marks \n"))
ss = int(input("Enter your ss marks \n"))
sa = int(input("Enter your sanskart marks \n"))
h = int(input("Enter your hindi marks \n"))
e = int(input("Enter your english marks \n"))

tot = (m+s+ss+sa+h+e)/6
print("your persentage is " , tot)
if m>33 and s>33 and ss>33 and sa>33 and h>33 and e>33:
    if tot<100 and tot>95:
        print("congratulation! you pass with A+ grade")
    elif tot<95 and tot>85:
        print("congratulation! you are pass with A grade")
    elif tot<85 and tot>70:
        print("congratulation! you are pass with B grade")
    elif tot<70 and tot>55:
        print("congratulation! you are pass with C grade")    
    elif tot<55 and tot>50:
        print("congratulation! you are pass with D grade")
    elif tot<50 and tot>35:
        print(" you are pass with grace")
    else:
        print("you are fail because you persentage is less than 35")
else :
    print("you are fail because you less than 33 marks in one of the subject")