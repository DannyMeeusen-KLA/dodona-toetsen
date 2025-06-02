uitvoer = ""

invoer = input('Geef een drieletterafkorting: ')
while invoer != "":
    if len(invoer) == 3:
        uitvoer = uitvoer + invoer + " "
    invoer = input('Geef een drieletterafkorting: ')

print (uitvoer)
