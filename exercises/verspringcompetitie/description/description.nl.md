We zoeken de verste en de minst verre sprong in een verspringcompetitie.  
De gebruiker geeft eerst in hoeveel atleten deelnemen. Elke atleet krijgt 3 sprongen.  
Vervolgens moet, lijn per lijn, naar de gesprongen afstand gevraagd worden. Als een atleet een ongeldige sprong aflevert, dan wordt de afstand *-1* (min 1) ingegeven.  
Je mag er van uitgaan dat er minstens één geldige sprong wordt afgeleverd in de hele competitie.  
  
Het programma drukt de verste en de minst verre (geldige) sprong af in twee volzinnen als volgt:  
*De verste sprong bedroeg xxx cm.*  
*De minst verre sprong bedroeg yyy cm.*  
(waarbij xxx en yyy de afstanden in kwestie zijn).  
  

### Voorbeeld 1
```console?lang=python&prompt=>>>
>>> 1
>>> -1
>>> 456
>>> 485
De verste sprong bedroeg 485 cm.  
De minst verre sprong bedroeg 456 cm. 
```

### Voorbeeld 2
```console?lang=python&prompt=>>>
>>> 2
>>> 584
>>> 583
>>> -1
>>> -1
>>> 574
>>> 521
De verste sprong bedroeg 584 cm.  
De minst verre sprong bedroeg 521 cm. 
```

### Voorbeeld 3
```console?lang=python&prompt=>>>
>>> 4
>>> 684
>>> 583
>>> -1
>>> -1
>>> 714
>>> -1
>>> 245
>>> 365
>>> -1
>>> 259
>>> 574
>>> 243
De verste sprong bedroeg 714 cm.  
De minst verre sprong bedroeg 243 cm. 
```

