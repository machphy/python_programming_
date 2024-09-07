n=int(input('Enter a number '))
factorial=1
for count in range (1,n+1):
    factorial=factorial*count

print('factorial of',n,'is',factorial)