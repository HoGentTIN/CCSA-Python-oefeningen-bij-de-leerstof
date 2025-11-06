# De 8-puzzel oplossen met A*-algoritme

## Implementatie van de 8-puzzel

Schrijf een klasse `AchtPuzzel` die een instantie van een 8-puzzel voorstelt.
Deze klasse `AchtPuzzel` heeft de volgende methoden:
 
- `__init__(self, bord)`: de constructor. Hieraan geef je optioneel een string mee van lengte 9 bestaande uit de cijfers 0 t.e.m. 8. Deze string stelt een 8-puzzel voor, waarbij 0 staat voor het lege vakje.  Wanneer je geen argumenten meegeeft dan wordt een "standaard" doelbord opgebouwd, met alle cijfers in oplopende volgorde en het lege vakje rechtsonderaan.
- `opvolgers(self)`: Deze methode geeft een `set` terug van paren. Elk paar `(a, s)` staat voor een actie `a` en een nieuwe `AchtPuzzel` `s`. Zoals uitgelegd in de cursus beschouwen we de acties in termen  van de beweging van het lege vakje.  We gebruiken de letters `B`(oven), `O`(nder), `L`(inks) en `R`(rechts). Je kan deze `dict` gebruiken om deze methode vlotter te implementeren:
```
 BUREN = {0 : {("R", 1),("O", 3)},       1 : {("L", 0),("R", 2),("O", 4)},        2 : {("L",1),("O",5)},
          3 : {("B",0),("R",4),("O",6)}, 4 : {("B",1),("L", 3),("R", 5),("O",7)}, 5 : {("B",2),("L", 4),("O",8)},
          6 : {("B",3),("R",7)},         7 : {("B",4),("L",6),("R",8)},          8 : {("B",5),("L",7)} 
            }
```
De betekenis hiervan is als volgt. Voor het vakje linksbovenaan (met index 0) kan je de actie `R`(echts) uitvoeren en dan belandt het lege vakje op positie 1. Je kan eveneens de actie `O`(nder) uitvoeren en dan belandt het lege vakje op het linkse vakje van de middelste rij. Dit vakje heeft index 3. Vandaar dus de afbeelding `0 : {("R", 1),("O", 3)}`.
 
- `aantal_verkeerd(self, andere_puzzel)`. Deze methode telt op hoeveel posities *verschillend van het lege vakje* de twee puzzels verschillen.
- `manhattan_heuristiek(self, andere_puzzel)`. Deze methode telt de Manhattan afstand van elk vakje *uitgezonderd het lege vakje* naar zijn doelpositie zoals gegeven door `andere_puzzel`.

## Implementatie van een Plan

Schrijf een klasse `Plan`. Deze klasse houdt een aantal attributen bij:

- `toestand`: de omschrijving van de huidige toestand
- `actie`: de actie uitgevoerd om deze toestand te bereiken
- `voorganger`: een ander plan. Het uitvoeren van de actie in het huidig plan op de toestand in de voorganger levert de toestand van dit plan op.
- `kost`: de totale kost om hier te geraken
- `h_waarde`: de waarde van de heuristiek voor de huidige toestand

Bij de implementatie van het A*-algoritme zijn het deze plannen die zullen opgeslaan worden
in de prioriteitswachtrij, waarbij plannen met een lagere `kost + h_waarde` een hogere prioriteit
hebben. Daarom schrijven we een methode `__lt__(self, ander_plan)` om twee `Plan`nen te vergelijken.
Deze methode moet `True` teruggeven als en slechts als `self < ander_plan`. In alle andere gevallen moet `False` teruggegeven worden.

Aan de hand van een `Plan` kan men alle acties terugvinden die werden uitgevoerd om dit plan 
te bekomen. Schrijf een methode `geef_actie_sequentie` die de acties die werden uitgevoerd
om tot de toestand in dit plan te komen *in de juiste volgorde* teruggeeft.


## Implementatie van het A*-algoritme

Schrijf een methode `a_ster_zoeken` die het A*-algoritme implementeert in zijn graafgebaseerde variant, d.w.z. dat er een gesloten lijst wordt bijgehouden van toestanden die reeds zijn geëxpandeerd.
Deze methode  heeft de volgende parameters:

- `start_toestand`. De toestand van waaruit het zoekproces vertrekt (hier dus de AchtPuzzel waarmee je start).
- `is_doel`. Een functie die van een toestand kan zeggen of het doel bereikt werd of niet.
- `heuristiek`. Een functie die een toestand afbeeldt op zijn heuristische waarde
- `kost`. Een functie met twee argumenten: een toestand en een actie. Deze functie geeft 
aan wat de kost is van het uitvoeren van de actie in de gegeven toestand. Een default-implementatie
zou als volgt kunnen zijn: `kost = lambda s, a : 1`, wat aangeeft dat het uitvoeren van om het even welke actie een kost heeft van 1.

De methode `a_ster_zoeken` retourneert een tupel `(actie_sequentie, kost)` wanneer een oplossing
werd gevonden of `None` wanneer er geen oplossing werd gevonden. 

Tips: 

- Maak (uiteraard) gebruik van de klasse `Plan` voor het implementeren van deze methode.
- Om dezelfde oplossing te verkrijgen als in de testen roep je `sorted` aan op de returnwaarde van `opvolgers`. Op die manier worden de acties steeds in dezelfde volgorde geprobeerd.
- Om de prioriteitswachtrij te implementeren kan je gebruik maken van de ingebouwde module `heapq`. Hier een kort voorbeeld van het gebruik:
```
import heapq
wachtrij = []
heapq.heappush(wachtrij, 5)
heapq.heappush(wachtrij, 1)
heapq.heappush(wachtrij, 3)
print(heapq.heappop(wachtrij)) # dit print de waarde 1
print(heapq.heappop(wachtrij)) # dit print de waarde 3
```
