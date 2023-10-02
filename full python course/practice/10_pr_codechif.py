from cgi import print_directory
from traceback import print_tb
from wsgiref.validate import InputWrapper


t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if x>y:
        print(x-y)
    else:
        print(0)