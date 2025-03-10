tekst = input ('Geef 5 getallen gescheiden door een spatie: ')

# 5 getallen opslaan in strlijst
strlijst = tekst.split()

# lege intlijst aanmaken en 5 getallen als int toevoegen
intlijst = []
for strgetal in strlijst:
    intlijst.append(int(strgetal))
    
index = 1 
while index < len(intlijst) :
    if intlijst[index] < intlijst[index-1]:
        print(intlijst[index], 'is kleiner dan zijn voorganger.')
    elif intlijst[index] == intlijst[index-1]:
        print(intlijst[index], 'is gelijk aan zijn voorganger.')
    else:
        print(intlijst[index], 'is groter dan zijn voorganger.')
    index = index + 1
        