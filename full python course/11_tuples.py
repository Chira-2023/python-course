# creating a tuples using ()
from queue import Empty


t = (1,2,3,4,5,6)
# t1 = () ## Empty tuple
# print(t)
# # print(t1)

# t1 = (1) ## wrong way to decleared the tuples with one element
# print(t1) ## it is trieat a number
# t1 = (1,)  ## tuples with one element
# print(t1)  ## it is trieat a tuple

# cannot update the value of a tuple
# t(0) = 44  ## this is show error

print(t.count(1))
print(t.index(5))