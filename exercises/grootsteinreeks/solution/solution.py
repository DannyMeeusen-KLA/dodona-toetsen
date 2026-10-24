kleinste = int(input('Geef het eerste getal: '))
grootste = kleinste

getal = int(input('Geef het tweede getal: '))
if getal < kleinste:
    kleinste = getal
elif getal > grootste:
    grootste = getal

getal = int(input('Geef het derde getal: '))
if getal < kleinste:
    kleinste = getal
elif getal > grootste:
    grootste = getal

getal = int(input('Geef het vierde getal: '))
if getal < kleinste:
    kleinste = getal
elif getal > grootste:
    grootste = getal

getal = int(input('Geef het vijfde getal: '))
if getal < kleinste:
    kleinste = getal
elif getal > grootste:
    grootste = getal

print ('Het kleinste getal is ' + str(kleinste) + ', het grootste getal is ' + str(grootste) + '.')