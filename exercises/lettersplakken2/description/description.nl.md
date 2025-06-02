In dit programma blijft de gebruiker letters of woorden invoeren tot hij een lege string invoert (= op Enter duwen zonder eerst iets te hebben ingegeven).  
Als de gebruiker een woord van drie letters invoert, wordt dit woord aan de uitvoerstring "geplakt", gevolgd door een spatie.  
Als de invoer één, twee, vier of meer karakters lang is, dan wordt deze invoer NIET aan de uitvoerstring toegevoegd.  
  
Om de lengte van de invoer te bekijken, kan je de functie *len()* gebruiken.  
Zo is *len("abc")* gelijk aan 3.  
*len("a")* is dan weer gelijk aan 1.  
Gebruik een while die stopt als de lengte van de invoer gelijk is aan 0.  
  
Bekijk de voorbeelden.  
    

### Voorbeeld 1
```console?lang=python&prompt=>>>
>>> KLA
>>> Koninklijk Lyceum Antwerpen
>>> btw
>>> belasting op de toegevoegde waarde
>>> PSG
>>> Paris Saint-Germain
>>> 
KLA btw PSG 
```
In dit voorbeeld wordt enkel de eerste, derde en vijfde invoerlijn behouden. Daar is de lengte immers gelijk aan 3.  
De invoerlijnen 2, 4 en 6 worden niet aan de uitvoer toegevoegd want hun lengte is verschillend van 3.  

### Voorbeeld 2
```console?lang=python&prompt=>>>
>>> 01
>>> NCZ
>>> KGD
>>> wiskunde
>>> chemie
>>> ISL
>>> fysica
>>> 
NCZ KGD ISL 
```
In dit voorbeeld worden enkel de afkortingen van de levensbeschouwelijke vakken behouden omdat ze op een afzonderlijke lijn werden ingebracht, telkens met lengte 3.  
De andere invoerlijnen hebben allemaal een lengte verschillend van 3 en werden dus niet behouden in de uitvoer.
