bedrag = int(input('Het gestorte bedrag: '))
if bedrag <= 1000:
    rente = bedrag * 0.1
else:
    rente = 100 + (bedrag-1000) * 0.2

print ('Marc krijgt', rente, 'euro aan rente.')