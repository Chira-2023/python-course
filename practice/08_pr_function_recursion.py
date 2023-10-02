# Q1 write a function to find the greatest of 3 number
# def great_num(a,b,c):
#     if a>b and a>c:
#         print(a," is greates no. out of three ")
#     elif b>a and b>c:
#         print(b," is greates no. out of three ")
#     else:
#         print(c," is greates no. out of three ")

# a = int(input("Enter the first number: "))
# b = int(input("Enter the secound number: "))
# c = int(input("Enter the thired number: "))
# great_num(a,b,c)








# Q2 write a function to convert in celsius to fahrenheit
# def temp_conv(c):
#     f = (9/5)*c +32
#     return f

# c = int(input("Enter the value in °C to convert in °F: "))
# cov = temp_conv(c)
# print(c,"°C conver in to " , cov,"°F")







# Q3 how to work end function

# print("hello" , end = " ") # is me (end = " ") ka matlab hai ki print end ho jaye 1 space se or iski by defualt value (\n) hoti hai
# print("how" , end = " ")
# print("are" , end = " ")
# print("you?" , end = " ")









# # Q4 write a recursion function to sum first n natural number
# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)

# num = int(input("Enter the number: "))
# sum = sum(num)
# print("The sum first "+ str(num)+" natural no. is "+str(sum))






''' Q5 write a function to print the following pattern
    n = 3
    ***
    **
    *
'''

# def star_print(n):
#     print("*"*n)
    
#     if n == 1:
#         return "*"
#     star_print(n-1)

# num = int(input("Enter the no. jithne star print krne hai: "))
# star_print(num)





# Q6 convert inch to cm 
# def in_to_cm(n):
#     return n *2.54
# cm = in_to_cm(4)
# print(cm)




# Q7 remove a word from a string and print the string

# def remov_word(string,word):
#     f = string.replace(word,"")
#     return f.strip()
# this = "hello chirag how are you ?"
# r = remov_word(this,"chirag")
# print(r)




# Q8 write a python function to print the multiplication of no. which is enterd by the user
def mult_tabl(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
num = int(input("Enter a number: "))
mult_tabl(num)