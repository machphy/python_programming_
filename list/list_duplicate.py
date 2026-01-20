list=[2,5,7,6,2,3,4,6,5,7,9,1,2,4,11,10,12]
list2=[]
for x in list:
    if x not in list2 :
        list2.append(x)

print(list2) 