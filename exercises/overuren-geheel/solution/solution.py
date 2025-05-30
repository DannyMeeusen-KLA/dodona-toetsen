uren = int(input('Aantal gewerkte uren: '))
if uren <= 8:
    loon = uren * 11
else:
    loon = 88 + (uren-8)*16

print ('Simona verdiende vandaag', loon, 'euro.')