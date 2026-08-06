dagenMeer25 = 0
dagenMeer30 = 0
for tel in range (5):
    temp = int(input('Geef de temperatuur van dag '+str(tel+1)+': '))
    if temp >= 25:
        dagenMeer25 = dagenMeer25 + 1
    if temp >= 30:
        dagenMeer30 = dagenMeer30 + 1


if dagenMeer25 == 5 and dagenMeer30 >= 3:
    print ('Er was een hittegolf tijdens deze vijfdaagse.')
else:
    print ('Er was geen hittegolf tijdens deze vijfdaagse.')
