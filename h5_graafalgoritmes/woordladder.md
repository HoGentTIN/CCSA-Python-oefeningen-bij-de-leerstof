# Woordladder

In deze oefening ga je een kinderspelletje implementeren, nl. het maken van 
een woordladder. Je begint met een startwoord, je kan telkens één letter wijzigen, en de bedoeling is om uit te komen bij een doelwoord. Bij wijze van voorbeeld een woordladder om het woord "hiel" om te zetten in "voet" (en omgekeerd):
```
hiel -> viel -> voel -> voet
```

We zullen dit probleem modelleren als een kortste pad probleem in een ongewogen graaf. De knopen van de graaf stellen de woorden voor en twee 
knopen zijn verbonden als en slechts als hun woorden op precies één plaats 
verschillen.

## Bepalen of twee woorden op precies één plaats verschillen

Schrijf een methode om te bepalen of twee woorden even lang zijn en op precies één plaats verschillen. Noem deze methode `precies_een_verschillend`. Deze methode kan als volgt 
worden gebruikt:
```
>>> precies_een_verschillend("span", "spat")
True
>>> precies_een_verschillend("test", "tast")
True
>>> precies_een_verschillend("test", "testje")
False
>>> precies_een_verschillend("test", "test")
False
>>> precies_een_verschillend("testje", "test")
False
>>> precies_een_verschillend("TEST", "test")
False
```

## Opbouwen van een graaf

We zullen de graaf voorstellen aan de hand van een "dictionary" of "map" (i.e. een `dict` in Python). De sleutels van deze `dict` zijn de verschillende woorden, de waarden zijn verzamelingen (`set`) van woorden. Schrijf een methode `maak_graaf` die een lijst van woorden meekrijgt als invoerparameter. De returnwaarde van deze methode is een `dict` die de ongerichte en ongewogen graaf voorstelt. Deze methode kan als volgt worden gebruikt:
```
>>> words = ["aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd", "da", "db", "dc", "dd"]
>>> graaf = maak_graaf(words)
>>> graaf
{'aa': {'ca', 'ac', 'ba', 'ad', 'da', 'ab'}, 'ab': {'cb', 'aa', 'ac', 'bb', 'db', 'ad'}, 'ac': {'aa', 'cc', 'bc', 'dc', 'ad', 'ab'}, 'ad': {'aa', 'ac', 'cd', 'dd', 'bd', 'ab'}, 'ba': {'aa', 'ca', 'bc', 'bb', 'bd', 'da'}, 'bb': {'cb', 'ba', 'bc', 'bd', 'db', 'ab'}, 'bc': {'ac', 'ba', 'cc', 'bb', 'bd', 'dc'}, 'bd': {'cd', 'ba', 'dd', 'bc', 'bb', 'ad'}, 'ca': {'cb', 'aa', 'cd', 'ba', 'cc', 'da'}, 'cb': {'ca', 'cd', 'cc', 'bb', 'db', 'ab'}, 'cc': {'cb', 'ca', 'ac', 'cd', 'bc', 'dc'}, 'cd': {'cb', 'ca', 'cc', 'dd', 'bd', 'ad'}, 'da': {'aa', 'ca', 'ba', 'dd', 'dc', 'db'}, 'db': {'cb', 'dd', 'bb', 'dc', 'da', 'ab'}, 'dc': {'ac', 'cc', 'dd', 'bc', 'db', 'da'}, 'dd': {'cd', 'bd', 'dc', 'db', 'ad', 'da'}}
>>> graaf['aa']
{'ca', 'ac', 'ba', 'ad', 'da', 'ab'}
```

## Impliciet berekenen van kortste paden

Schrijf een methode `kortste_pad` met een graaf `g` en een woord `w` als invoer  die een `dict` teruggeeft die `string`s afbeeldt op `string`s. De betekenis van deze dictionary is de volgende. 
- Als woord `w1` afgebeeld wordt op `None` wil dit zeggen dat er geen pad bestaat van `w` naar `w1`.
- Als woord `w1` afgebeeld wordt op woord `w2` dan is woord `w2` de directe voorganger van `w1` op het gevonden 
kortste pad van woord `w` naar `w1`. M.a.w. het pad van `w` naar `w1` heeft als laatste boog `(w2,w1)`. 

Deze methode kan je als volgt gebruiken:
```
>>> words = ["aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd", "da", "db", "dc", "dd"]
>>> graaf = maak_graaf(words)
>>> kortste_pad(graaf, "aa")
{'aa': 'aa', 'ab': 'aa', 'ac': 'aa', 'ad': 'aa', 'ba': 'aa', 'bb': 'ab', 'bc': 'ac', 'bd': 'ad', 'ca': 'aa', 'cb': 'ab', 'cc': 'ac', 'cd': 'ad', 'da': 'aa', 'db': 'ab', 'dc': 'ac', 'dd': 'ad'}
```

*Belangrijke opmerking*. Bij het implementeren van deze methode zal je de buren van een knoop moeten 
overlopen. Doe dit als volgt:
```
for w in sorted(graaf[v]):
```
Door het gebruik van `sorted` worden de woorden steeds in alfabetische volgorde overlopen. Dit zorgt
ervoor dat de uitvoer van de methode uniek bepaald wordt. (Dat is nodig voor het automatisch testen van de code.)

## Expliciet bepalen van een pad

Met behulp van de dictionary berekend door `kortste_pad` kunnen nu de kortste paden expliciet worden 
berekend. Schrijf een methode `geef_pad` met als invoer de dictionary berekend door `kortste_pad` en
een woord. Deze methode geeft een lijst van woorden terug die start met het woord `w` dat werd gebruikt
en eindigt bij het meegegeven woord.  Wanneer zo'n pad niet bestaat dan wordt `None` teruggegeven.  Merk op dat het woord `w` uniek bepaald kan worden uit de meegegeven dictionary, het is namelijk het enige woord dat zijn eigen voorganger is.

```
>>> words = ["aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd", "da", "db", "dc", "dd"]
>>> graaf = maak_graaf(words)
>>> pred = kortste_pad(graaf, "aa")
>>> geef_pad(pred, "dd")
['aa', 'ad', 'dd']
>>> geef_pad(pred, "aa")
['aa']
>>> geef_pad(pred, "ba")
['aa', 'ba']
```