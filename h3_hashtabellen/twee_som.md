# Implementatie van de twee som puzzel

Gegeven een rij van gehele getallen en een doelgetal, eveneens geheel. Maak de methode `two_sum` die de indices retourneert in een tupel van de twee getallen die samen als som het doelgetal hebben.  
- Ga ervan uit dat er maar één oplossing mogelijk is.
- Je mag een element niet twee keer gebruiken.  
- Geef de indices van de twee getallen in stijgende volgorde. Geef `None` terug als er geen paar wordt gevonden.  

### Vragen

- Wat zou de tijdscomplexiteit zijn van dit algoritme?  
- Kan je ook een versie maken van dit algoritme met een betere tijdscomplexiteit? Een tip: gebruik hiervoor hashtabellen. Geef deze methode de naam `two_sum_hash`.
- Wat is de tijdscomplexiteit nu?  

### Een voorbeeld

Als `doel = 10` en `getallen = [1, 4, 5, 7, 8, 9]` dan geeft zowel `two_sum(getallen, doel)` als `two_sum_hash(getallen, doel)` het tupel `(0, 5)` als resultaat.