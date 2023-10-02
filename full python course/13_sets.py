a = {34,4,"hello",25}
a2 = {"hello", 33,34,45,223,2}
# print(type(a))
# print(a)
print(a.intersection(a2)) # intersection method in sets
# # Empty sets
# b = {} # this is a empty dictionary 
# c = set() # this is a empty set
# print(type(b))
# print(type(c))

# method in sets 
d = set()
d.add(4)
d.add(566)
d.add(6)
# d.add([4,5,3,"chirag arya"]) ## set me list and dictionary element nhi add kr skte hai kyoki inko hum change bhi kr sakte hai
d.add((5,6,"chirag arya")) # set me tuples ko add kr sakte hai
# print(d)

# print(len(d)) ## printing the length of sets

# # d.remove(5) ## throws an error becouse this 5 is not present in the set
# d.remove(4) ## this is remove becouse this 4 present in the set 
# print(d)

## POP method
print(d)
print(d.pop())
