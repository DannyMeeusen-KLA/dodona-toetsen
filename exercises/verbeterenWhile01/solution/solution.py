onder = int(input('Geef de ondergrens: '))
boven = int(input('Geef de ondergrens: '))

while onder <= boven:
    if onder % 4 == 0:
        print (onder, end=' ')
    onder = onder + 1
