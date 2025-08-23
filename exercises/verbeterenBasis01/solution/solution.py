# In dit programma zitten veel fouten. 
# Wij tellen al zeker 8 nodige aanpassingen die er moeten gebeuren vooraleer het perfect werkt.

getal1 = int(input("Geef een geheel getal in: "))              # int toegevoegd
getal2 = int(input("Geef een geheel getal in: "))              # int toegevoegd
getal3 = float(input("Geef een decimaal getal in: "))          # float toegevoegd

# Druk het eerste getal af
print (getal1)                                              # print aan kantlijn gezet en getal1 met kleine letter

# Bereken de som van getal1 en getal2 en druk af
som = getal1 + getal2                                       # toekenning is van rechts naar links
print (som)

# Druk het derde getal af
print (getal3)                                              # aanhalingstekens verwijderen

# Bereken het product van de som en getal3, rond af tot op 1 cijfer na de komma en druk af
product = som * getal3
product = round(product, 1)                                 # 'product =' toevoegen aan linkerkant (toekenning)
print (product)
