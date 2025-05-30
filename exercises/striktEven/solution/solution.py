bovengrens = int(input('Geef de bovengrens: '))

if bovengrens < 2:
    print ('De bovengrens is te laag.')
else:
    for tel in range(2, bovengrens+1, 2):
        print (tel)