zin = input ('Geef een rij getallen, gescheiden door spaties: ')

strlijst = zin.split()

kleinste = int(strlijst[0])
aantalinlijst = len(strlijst)

for tel in range(1, aantalinlijst-1, 1):
    getal = int(strlijst[tel])
    if getal < kleinste:
        kleinste = getal

print (kleinste)
