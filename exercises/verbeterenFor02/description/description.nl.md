Je krijgt een oplossing van onderstaande opgave, jammer genoeg met syntax- en/of logische fouten.  
Test het programma in de sandbox, corrigeer de fouten en dien je gecorrigeerde oplossing in.  

De gebruiker geeft op één lijn 5 gehele getallen in, gescheiden door een spatie.  
Het programma splitst de lijn en steekt de gehele getallen in een lijst (als string).  
Het programma doorloopt de lijst met strings en steekt de elementen in een nieuwe lijst (als integer).  
Het programma doorloopt de lijst met integers en vergelijkt elk getal met zijn voorganger. Afhankelijk van het resultaat van
deze vergelijking, wordt één van deze teksten afgedrukt:  
*xxx is groter dan zijn voorganger.*  
*xxx is gelijk aan zijn voorganger.*  
*xxx is kleiner dan zijn voorganger.*  

De voorgestelde oplossing maakt gebruik van een *for* om de tabellen te vullen, en van een *while* om de getallen te vergelijking met de voorganger. Let op: deze vergelijking begint pas vanaf het tweede getal!  

Bekijk de voorbeelden!  

### Voorbeelden

```console?lang=python&prompt=>>>
>>> 5 7 1 9 12
7 is groter dan zijn voorganger.
1 is kleiner dan zijn voorganger.
9 is groter dan zijn voorganger.
12 is groter dan zijn voorganger.

>>> 8 8 6 6 9
8 is gelijk aan zijn voorganger.
6 is kleiner dan zijn voorganger.
6 is gelijk aan zijn voorganger.
9 is groter dan zijn voorganger.

```
