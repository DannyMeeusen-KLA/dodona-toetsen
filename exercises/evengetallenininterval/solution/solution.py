onder = int(input('Geef de ondergrens: '))
boven = int(input('Geef de bovengrens: '))

for tel in range (onder, boven+1, 1):
    if tel%2 == 0:
        print (tel)

print ()