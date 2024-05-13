import math


a=int(input('enter a : '))
b=int(input('enter b : '))
c=int(input('enter c : '))
root1=(-b+ math.sqrt(b**2-4*a*c))/(2*a)
root2=(-b- math.sqrt(b**2-4*a*c))/(2*a)
print('root are:',root1,root2)
