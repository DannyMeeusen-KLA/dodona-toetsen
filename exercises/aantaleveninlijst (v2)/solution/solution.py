# inlezen lijst getallen, gescheiden door spaties
zin = input('Geef de getallen in, gescheiden door spaties:')

# omvormen tot stringlijst
strlijst = zin.split(' ')

# aantal elementen in de lijst ophalen (wordt gebruikt in de range)
aantalinlijst = len(strlijst)

# teller aantal even getallen op zijn beginwaarde zetten
aantaleven = 0

# door de lijst lopen (van index 0 tot aantalinlijst-1)
for tel in range(0, aantalinlijst, 1):
    # elk element uit de lijst (van type string) omzetten naar type int
    intgetal = int(strlijst[tel])
    # als het getal even is: teller aantal even getallen met één verhogen
    if intgetal % 2 == 0:
        aantaleven = aantaleven + 1

# aantal even getallen afdrukken
print(aantaleven)
