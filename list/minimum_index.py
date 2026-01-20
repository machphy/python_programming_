fri1 = ['mango', 'apple', 'burger', 'juice', 'banana', 'samosa']

fri2 = ['apple', 'juice', 'samosa', 'mango', 'burger', 'banana']

fri3 = ['samosa', 'banana', 'juice', 'burger', 'apple', 'mango']

index1=10
index2=10
index3=10

for i in range (len(fri1)):
    index=fri2.index(fri1[i])

    if i+ index< index1+index2+index3:
        index1=i
        index2=index
        index3=index
print(fri1[index1],index1+index2+index3)
    