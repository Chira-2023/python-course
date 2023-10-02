# name = ["chirag","rahul","uma","neha"]
# def hi():
#     return "hi "
# for i in range(len(name)):
#     print(hi() + name[i])


# default name in function
def greet(name = "stranger"):
    print("good day "+name)

greet("chirag")  # good day chirag print hoga 
greet()   # good day stranger print hoga