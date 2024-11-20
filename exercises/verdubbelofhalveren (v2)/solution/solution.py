# inlezen lijst getallen, gescheiden door spaties
zin = input('Geef de getallen in, gescheiden door spaties:')

# omvormen tot stringlijst
strlijst = zin.split(' ')

# lege lijst aanmaken
lijst = []

for strgetal in strlijst:
    intgetal = int(strgetal)
    if intgetal % 2 == 0:
        lijst.append (intgetal // 2)
    else:
        lijst.append (intgetal * 2)

print(lijst)