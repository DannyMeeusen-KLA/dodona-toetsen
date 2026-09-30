naam = input('Geef de naam van de leerling: ')
aantal = int(input('Geef het aantal sponsors: '))
bedrag = float(input('Geef het bedrag per sponsor: '))

totaal = round(aantal*bedrag, 1)
print ('Het aantal euros dat', naam, 'inzamelde, bedraagt', str(totaal)+'.')