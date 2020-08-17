a_list = [1,"2", {"123":123}, [1,2,3,4]]
a_dict = {"list" : " " , "dict" : "", "int" : "", "str" : ""}
for a in a_list:
    if type(a) == list:
        a_dict.update({"list" : a})
    elif type(a) == dict:
        a_dict.update({"dict": a})
    elif type(a) == int:
        a_dict.update({"int" : a})
    elif type(a) == str:
        a_dict.update({"str" : a})

print(a_dict)
