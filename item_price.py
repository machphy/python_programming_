item=input('enter the item name :-')
price=input('enter the price :-')

total_len=len(item)+len(price)

print(total_len)

dots='.'*(20-total_len)
print(item+dots+price)
