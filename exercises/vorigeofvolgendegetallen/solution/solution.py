begin = int(input('Geef het begingetal: '))
richting = input('Geef een + of een - in: ')

if richting == '+':
    for tel in range (begin, begin+10, 1):
        print (tel, end=' ')
else:
    for tel in range (begin, begin-10, -1):
        print (tel, end=' ')

