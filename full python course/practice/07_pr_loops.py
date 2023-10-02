# Q1 write a prog. to print a multiplication table enter by user using for loop
# t = int(input("Enter a value jiski table print krani hai "))


# for i in range(1,11):
#     print(i*t)
    





# Q2 write a program to find first letter of name in list using for loop
# list  = ["chirag","rahul","rajesh","ramniwas"]

# for name in list :
#     if name.startswith("r"):
#         print("hello! "+ name)







# Q3 attempt first question using while loop
# num = int(input("Enter the value: "))
# i = 1
# while i<=10:
#     print(str(num) + "x" + str(i) + "=" + str(num*i))
#     i = i+1






# Q4 write a program to find a number prime or not

# num = int(input("Enter the value: "))
# prime = True
# for i in range(2,num):
#     if num%i == 0:
#         prime = False
#         break
# if prime:
#     print("Number "+str(num)+" is prime")
# else:
#     print("Number "+str(num)+" is not prime")






# Q5 write a program to find the sum first n natural numbers using while loop

# num = int(input("Enter the number: "))
# sum = 0
# i = 1
# while i <= num:
#     sum = sum + i
#     i = i+ 1
# print(sum)






# Q6 write a program to find the factorial first n natural numbers 
# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1,(num+1)):
#     factorial = factorial*i

# print(f"The factorial of {num} is {factorial}")



'''Q7 write the folloing pattern 
n = 3   *
        **
        ***  '''


# n = int(input("Ente the value jitne star chahiye: "))
# for i in range(1,(n+1)):
#     print(i*"*")



'''Q8 write the folloing pattern 
n = 3   *
       ***
      *****  '''
# n = int(input("Enter the value of printing the star: "))
# for i in range(n):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i +1),  end="")
#     print(" "*(n-i-1))



# Q9 write a program to print the reverse table 
t = int(input("Enter a value jiski table reverse print krani hai "))

i = [10,9,8,7,6,5,4,3,2,1]
for a in range(10):
    print(i[a]*t)