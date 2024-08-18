pass1=input('enter password :-')
pass2=input('conf password :-')

if pass1==pass2:
    print('yes they are matched')
else:
    if pass1.casefold()==pass2.casefold():
        print('plz enter the currect pasword or check the case ')
    else :
        print('no they are not match try again')
