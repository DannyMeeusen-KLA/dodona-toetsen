# de lijstvariabele met de kleuren van de regenboog
regenboog = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'indigo', 'violet']

for kleur in regenboog:
    print (kleur)

volgnummer = int(input('Geef het volgnummer van de gewenste kleur: '))
if volgnummer < 1 or volgnummer > 7:
    print ('Met dit volgnummer komt geen kleur overeen.')
else:
    print ('Met volgnummer', volgnummer, 'komt de kleur', regenboog[volgnummer-1],'overeen.')