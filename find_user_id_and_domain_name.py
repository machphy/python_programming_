emailid=input('enter emial id :- ')
atrate= emailid.find('@')
print(atrate)

print('user id :', emailid[:atrate])
print('domain name :', emailid[atrate+1:])
