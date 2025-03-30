Uit de postcode van een Belgische gemeente of stad kan je de provincie afleiden waarin de gemeente of stad ligt.  
We beperken ons in deze oefening tot de postcodes van Vlaamse steden en gemeenten. Hieronder vind je voor elke provincie het interval waarin de postcodes liggen:  

- provincie **Antwerpen**: [2000, 2999]  
- provincie **Vlaams-Brabant**: [1500, 1999] en [3000, 3499]  
- provincie **Limburg**: [3500, 3999]
- provincie **West-Vlaanderen**: [8000, 8999]  
- provincie **Oost-Vlaanderen**: [9000, 9999]  
  
Schrijf een functie `postcode` die als invoerparameter een postcode krijgt (als string), en de naam van de provincie teruggeeft.  
Je mag er van uitgaan dat de invoerparameter numeriek is, maar het kan wel zijn dat de postcode in geen enkel van bovenstaande intervals ligt. In dat geval geeft de functie de waarde **ongeldig** terug.  
  

## Voorbeelden

```console?lang=python&prompt=>>>
>>> postcode("2018")
Antwerpen
>>> postcode("1200")
ongeldig
>>> postcode("3500")
Limburg
>>> postcode("8500")
West-Vlaanderen
```
