maximum = int(input('Op hoeveel punten stond de toets? '))

aantalonv = 0
for tel in range(10):
    punten = int(input('Geef de punten van leerling'+str(tel)+': '))
    if punten < maximum/2:
        aantalonv = aantalonv + 1
        
print(aantalonv)
