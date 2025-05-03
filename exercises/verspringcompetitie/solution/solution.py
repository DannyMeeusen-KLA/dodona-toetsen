aantal = int(input('Aantal atleten dat deelneemt: '))

maxsprong = -1
minsprong = 9999
for tel in range (aantal*3):
    sprong = int(input('Afstand van de sprong'))
    if sprong > maxsprong:
        maxsprong = sprong
    if sprong > -1 and sprong < minsprong:
        minsprong = sprong
        
print ('De verste sprong bedroeg', maxsprong, 'cm.')        
print ('De minst verre sprong bedroeg', minsprong, 'cm.')        

    