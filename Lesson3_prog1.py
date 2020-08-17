god_list = [2,3,4,5,6,7,8,9,0,10,12,14,6231,123,54,76,21,77]
a_list = []
b_list = []
c_list = []
#for a in god_list:
#    if a % 2 == 0:
#        a_list.append(a)
#for b in god_list:
#    if b % 3 == 0:
#        b_list.append(b)
#for c in god_list:
#    if c % 2 !=0 and c % 3 !=0:
#        c_list.append(c)
#print(a_list)
#print(b_list)
#print(c_list)

#for a in god_list:
#    if a % 2 == 0:
#        a_list.append(a)
#        continue
#    if a % 3 == 0:
#        b_list.append(a)
#        continue
#    if a % 2 !=0 and a % 3 !=0:
#        c_list.append(a)
#        continue
#print(a_list)
#print(b_list)
#print(c_list)

for a in god_list:
    if a % 2 == 0:
        a_list.append(a)
        continue
    elif a % 3 == 0:
        b_list.append(a)
        continue
    else:
        c_list.append(a)
print(a_list)
print(b_list)
print(c_list)