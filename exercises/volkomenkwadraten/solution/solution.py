ondergrens = int(input('Geef het laagste grondtal:'))
bovengrens = int(input('Geef het hoogste grondtal:'))

vklist = []
for grond in range(ondergrens, bovengrens+1):
    vklist.append(grond**2)

print(vklist)
