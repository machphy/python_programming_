s1=input('enter a string')
s2=input('enter sec string')

if len(s1)!=len(s2):
    print('not eq')
else:
    for x in s1:
        if x not in s2:
            print('not anagram')
            break ;
    else :
        print('algram')