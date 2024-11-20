zin = input ('Geef een rij getallen, gescheiden door spaties: ')

strlijst = zin.split()

kleinste = None
aantalinlijst = len(strlijst)

for tel in range(0, aantalinlijst, 1):
    getal = int(strlijst[tel])
    if kleinste == None:
        kleinste = getal
    elif getal < kleinste:
        kleinste = getal

if kleinste == None:
    print ('Er is geen getal in de lijst.')
else:
    print (kleinste)
