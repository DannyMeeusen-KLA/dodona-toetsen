In dit programma blijft de gebruiker letters of woorden invoeren tot hij een lege string invoert (= op Enter duwen zonder eerst iets te hebben ingegeven).  
Als de gebruiker één letter invoert, wordt deze letter aan de uitvoerstring "geplakt".  
Als de invoer meer dan één karakter lang is, dan wordt deze invoer NIET aan de uitvoerstring toegevoegd.  
  
Om de lengte van de invoer te bekijken, kan je de functie *len()* gebruiken.  
Zo is *len("a")* gelijk aan 1.  
*len("abc")* is dan weer gelijk aan 3.  
Gebruik een while die stopt als de lengte van de invoer gelijk is aan 0.  
  
Bekijk de voorbeelden.  
    

### Voorbeeld 1
```console?lang=python&prompt=>>>
>>> K
>>> oninklijk
>>> L
>>> yceum
>>> A
>>> ntwerpen
>>> 
KLA
```
In dit voorbeeld wordt enkel de eerste, derde en vijfde invoerlijn behouden. Daar is de lengte immers gelijk aan 1.  
De invoerlijnen 2, 4 en 6 worden niet aan de uitvoer toegevoegd want hun lengte is verschillend van 1.  

### Voorbeeld 2
```console?lang=python&prompt=>>>
>>> 0123456789
>>> a
>>> bcd
>>> e
>>> fgh
>>> i
>>> jklmn
>>> o
>>> pqrst
>>> u
>>> vwxyz
>>> 
aeiou
```
In dit voorbeeld worden enkel de klinkers behouden omdat ze op een afzonderlijke lijn werden ingebracht, telkens met lengte 1.  
De invoerlijnen waar de cijfers en de medeklinkers werden ingebracht hebben allemaal een lengte groter dan 1 en werden dus niet behouden in de uitvoer.
