deeltal = int(input('Geef deeltal: '))
deler = int(input('Geef deler: ')) 

deeltal = deeltal + 1

while deeltal % deler != 0 or deeltal % 7 != 0:
    deeltal = deeltal + 1

print (deeltal)
