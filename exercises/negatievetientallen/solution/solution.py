bovengrens = int(input('Geef de ondergrens: '))

if bovengrens > 0:
    print ('De ondergrens is te hoog.')
else:
    for tel in range(ondergrens, 1, 10):
        print (tel)