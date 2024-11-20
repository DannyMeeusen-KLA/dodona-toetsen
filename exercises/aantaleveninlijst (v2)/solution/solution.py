# inlezen lijst getallen, gescheiden door spaties
zin = input('Geef de getallen in, gescheiden door spaties:')

# omvormen tot stringlijst
strlijst = zin.split(' ')

# teller aantal even getallen op zijn beginwaarde zetten
aantaleven = 0

for strgetal in strlijst:
    intgetal = int(strgetal)
    if intgetal % 2 == 0:
        aantaleven = aantaleven + 1

print(aantaleven)
