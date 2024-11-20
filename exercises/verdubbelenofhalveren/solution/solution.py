# inlezen hoeveel getallen er zullen worden ingegeven
aantal = int(input('Hoeveel getallen wil je ingeven:'))

# uitvoerlijst leeg aanmaken
lijst = []

for tel in range(1, aantal+1, 1):
    getal = int(input('Geef het getal: '))
    if getal % 2 == 0:
        lijst.append (getal//2)
    else:
        lijst.append (getal*2)

print(lijst)
