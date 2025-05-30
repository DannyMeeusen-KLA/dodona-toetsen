uitvoer = ""

invoer = input('Geef een letter: ')
while invoer != "":
    if len(invoer) == 1:
        uitvoer = uitvoer + invoer
    invoer = input('Geef een letter: ')

print (uitvoer)
