grondtal = int(input('Grondtal: '))

kwadraat1 = grondtal**2
kwadraat2 = (grondtal+1)**2

for tel in range (kwadraat1+1, kwadraat2):
    print (tel, end=' ')
