# inlezen hoeveel getallen er zullen worden ingegeven
aantal = int(input('Hoeveel getallen wil je ingeven:'))

# teller aantal even getallen op zijn beginwaarde zetten
aantaleven = 0

for tel in range(1, aantal+1, 1):
    getal = int(input('Geef het getal: '))
    if getal % 2 == 0:
        aantaleven = aantaleven + 1

print(aantaleven)
