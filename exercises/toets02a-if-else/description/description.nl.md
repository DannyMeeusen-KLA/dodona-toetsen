Het programma vraagt aan de gebruiker om, één voor één, de temperaturen van 5 opeenvolgende dagen in te geven, telkens op een verschillende lijn.  
Het getal wordt ingegeven zonder het graden-Celsius-teken (°).  

Het programma gaat dan bepalen of er een hittegolf was in die vijfdaagse periode.   
Om te spreken van een hittegolf moet aan volgende voorwaarden voldaan zijn:  
- het moet elke dag minstens 25 graden warm zijn, én  
- minstens drie van die 5 dagen moet het 30 graden of meer zijn (de zogenaamde '<i>tropische dagen</i>').  
  
Als er een hittegolf is, dan wordt afgedrukt: *Er was een hittegolf tijdens deze vijfdaagse.*   
Als er geen hittegolf is, dan wordt afgedrukt: *Er was geen hittegolf tijdens deze vijfdaagse.* 
      

### Voorbeelden

```console?lang=python&prompt=>>>
>>> 28
>>> 30
>>> 35
>>> 29
>>> 32
Er was een hittegolf tijdens deze vijfdaagse.

>>> 28
>>> 30
>>> 27
>>> 29
>>> 32
Er was geen hittegolf tijdens deze vijfdaagse.

>>> 31
>>> 30
>>> 33
>>> 22
>>> 32
Er was geen hittegolf tijdens deze vijfdaagse.

```