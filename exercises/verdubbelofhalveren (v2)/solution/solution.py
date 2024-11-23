# inlezen lijst getallen, gescheiden door spaties
zin = input('Geef de getallen in, gescheiden door spaties:')

# omvormen tot stringlijst
strlijst = zin.split(' ')

# bepalen aantal elementen in de lijst
aantalinlijst = len (strlijst)

# lege lijst aanmaken
lijst = []

# door de lijst lopen voor index = 0 tot en met index = aantalinlijst - 1
for tel in range(0, aantalinlijst, 1):
    # het element in de lijst (type = string) omzetten naar type int
    intgetal = int(strlijst[tel])
    # nakijken of het bekomen getal even of oneven is, de correcte bewerking erop uitvoeren en toevoegen aan de uitvoerlijst
    if intgetal % 2 == 0:
        lijst.append (intgetal // 2)
    else:
        lijst.append (intgetal * 2)

# de uitvoerlijst afdrukken
print(lijst)