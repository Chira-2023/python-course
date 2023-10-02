# # Q1. input = name but output is = good morning name
 
# name = input("Enter your name : ")
# print("good morning",name)

# ''' Q2. letter templet for example
#       letter = dear <|name|>
#                you are slected in jee with this rank
#                rank <|rank|>
# '''
# name = input("name:\n")
# rank = input("rank:\n")
# rank = int(rank)
# print("dear",name,
#         "\nyou are slected in jee with",rank, "rank" )


# # Q3. write a program to detect double speace in your string
# name = "my name is chirag arya and my  father  name is  rajesh arya"
# print(name.count("  "))


# # Q4. replace the double space in problem no. 3 by single space
# print(name.replace("  "," "))

# ''' Q5. write the program the folloing letter to creat the escape sequence
#        paragraph : dear chirag, you are slected in jee. Thank you!
# '''
# letter = '''dear chirag, \nyou are slected in jee. \n\nThank you! '''
# print(letter)