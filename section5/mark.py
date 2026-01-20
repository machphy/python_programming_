mark = int(input('Enter the subject mark: '))

if 0 <= mark <= 100:
    if mark >= 90:
        print('A++ mark')
    elif mark >= 80:
        print('A+ mark')
    elif mark >= 70:
        print('A mark')
    elif mark >= 60:
        print('B mark')
    elif mark >= 50:
        print('C mark')
    elif mark >= 40:
        print('D mark')
    elif mark >= 30:
        print('E mark')
    elif mark >= 20:
        print('F mark')
    elif mark >= 10:
        print('G mark')
    elif mark >= 0:
        print('H mark')
else:
    print('Invalid mark')
