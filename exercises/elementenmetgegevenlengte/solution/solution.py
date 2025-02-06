getallenlijst=['een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen', 'tien', 'elf', 'twaalf', 'dertien', 'veertien', 'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien', 'twintig']

lengte = int(input('Hoe lang moet het getal zijn: '))

for element in getallenlijst:
    if len(element) == lengte:
        print (element, end= ' ')

        