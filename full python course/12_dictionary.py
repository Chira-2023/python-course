from msilib import PID_TITLE


dic = {
    "chirag":"he is a coder",
    "rajesh":"he is a teacher",
    "xyz":[54,555,343,3545],
    "nextDic":{
        "rahul":"he is a youtuber",
        "uma" : "he is a student"
    },
    1:3

}
# print(dic["chirag"])
# print(dic["nextDic"]["uma"])


# dictionary method
# print(dic.keys()) # printing the key of dictionary 
# print(type(dic.keys()))
# print(dic.values())

update_dic = {
    "chirag arya": "he is a iitan",
    "uma bharti" : "he is a gclican"
}
dic.update(update_dic)
print(dic)

print(dic.get("chirag")) # it is output is key of chirag
print(dic["chirag arya"])    # it is output is key of chirag

# diffrence b/w get and [] is given blew
# print(dic.get("chirag1"))   # this is show NONE
# print(dic["chirag1"])     # this is show error