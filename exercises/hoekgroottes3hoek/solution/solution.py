hoek1 = int(input('Geef de grootte van de eerste hoek: '))
hoek2 = int(input('Geef de grootte van de tweede hoek: '))

hoek3 = 180 - hoek1 - hoek2

if hoek3 < 90:
    print ('De derde hoek is een scherpe hoek van', hoek3, 'graden.')
elif hoek3 == 90:
    print ('De derde hoek is een rechte hoek.')
else:
    print ('De derde hoek is een stompe hoek van', hoek3, 'graden.')
