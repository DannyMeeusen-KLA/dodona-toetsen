while True:
    getal = int(input('Geef een natuurlijk getal in uit het interval [10, 99]: '))
    if getal >= 10 and getal <= 99:
        break

eenheid = getal % 10
tiental = getal //10

if eenheid % 2 == 0 and tiental % 2 == 0:
    print ('BEIDEN EVEN')
elif eenheid % 2 == 1 and tiental % 2 == 1:
    print ('BEIDEN ONEVEN')
else:
    print ('EVEN EN ONEVEN')
