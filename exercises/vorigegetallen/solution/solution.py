begin = int(input('Geef het begingetal: '))
aantal = int(input('Geef het aantal getallen: '))

for tel in range (begin, begin-aantal, -1):
    print (tel, end=' ')
