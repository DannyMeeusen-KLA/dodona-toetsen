# vragen hoeveel er in de spaarpotten zit
spaarpot1 = int(input('Hoeveel zit er in de eerste spaarpot: '))
spaarpot2 = int(input('Hoeveel zit er in de tweede spaarpot: '))

# het saldo berekenen: is er geld teveel of te weinig?
saldo = spaarpot1 + spaarpot2 - 99

# antwoordzin afdrukken op basis van het feit of het saldo negatief of positief is
if saldo == 0:
    print ('De kinderen hebben net genoeg geld.')
elif saldo > 0:
    print ('De kinderen hebben', saldo, 'euro over.')
else:
    saldo = abs(saldo)
    print ('De kinderen hebben', saldo, 'euro tekort.')
