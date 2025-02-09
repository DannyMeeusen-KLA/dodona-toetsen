kwadraat = int(input('Geef een getal als kwadraat: '))

grondtal = 1
while (grondtal+1)**2 < kwadraat:
    grondtal = grondtal + 1

print ('Tussen', grondtal, 'en', grondtal+1)
