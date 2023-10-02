from ast import operator
from operator import truediv


a = 4
b = 2.0

# aurthmtical operators
print("The value of 4 + 2.0", a + b)
print("The value of 4 - 2.0", a - b)
print("The value of 4 * 2.0", a * b)
print("The value of 4 / 2.0", a / b)

#assigment operators
b += 1.5
b -= 2
b *= 2
b /= 5
print(b)

# comperision operators
# c = (5>4)
# c = (5<4)
# c = (5>=4)
# c = (5<=4)
# c = (5==4)
c = (5!=4)
print(c)

# logical operator
bool1 = True
bool2 = False
print("The value of bool1 and bool2 ",(bool1 and bool2))
print("The value of bool1 or bool2 ",(bool1 or bool2))
print("The value of not bool2 ",(not bool2))