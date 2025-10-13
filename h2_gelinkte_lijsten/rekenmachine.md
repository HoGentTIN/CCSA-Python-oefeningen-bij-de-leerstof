# Een (eenvoudige) rekenmachine

In deze oefening implementeren we een eenvoudige rekenmachine.
```
rekenmachine("3 + 5 * 2 - 4")
```
zal als returnwaarde `9` geven.

We weten reeds dat het voor een computer eenvoudig is om een expressie in postfix notatie te evalueren. Verder is er een gekend algoritme om een expressie in infix notatie om te zetten in postfix notatie. Tenslotte moet de infix-notatie nog "geparsed" worden in tokens en hierbij nemen we (voor de eenvoud) aan dat de verschillende tokens van elkaar gescheiden worden door een spatie).

Onze rekenmachine maakt enkel gebruik van de volgende binaire operatoren:
```
+ - * /
```

*Opmerking* je kan en mag meer functies definiëren (bv. om code gemakkelijk te kunnen hergebruiken of om je code meer leesbaar te maken) dan diegene die hieronder gevraagd worden. 

## Evalueren van expressie in postfix notatie

Schrijf een methode `evalueer_postfix(e)` waaraan een sequentie van tokens `e` wordt meegegeven. Elk token is ofwel een getal ofwel één van vier operatoren. Deze methode retourneert de waarde van de expressie.
Je mag er van uitgaan dat het een correcte expressie in postfix notatie betreft.
```
>>> evalueer_postfix(["3", "5", "*"])
15.0
>>> evalueer_postfix(["3", "5", "-"])
-2.0
>>> evalueer_postfix(["3", "5", "*", "2", "-"])
13.0
```

## Omzetten van infix naar postfix

Schrijf een methode `infix_naar_postfix(infix)` waaraan een sequentie van tokens `infix` wordt meegegeven.
Deze sequentie van tokens stelt een geldige infix expressie voor, gebruikmakend van getallen, de vier gegeven operatoren en haakjes. De return-waarde van deze methode is een sequentie van tokens die 
samen de postfix uitdrukking van gegeven infix expressie vormt. 
```
>>> infix_naar_postfix(["3", "*", "5"])
['3', '5', '*']
>>> infix_naar_postfix(["3", "-", "5"])
['3', '5', '-']
>>> infix_naar_postfix(["(", "3", "*", "5", ")", "-", "2"])
['3', '5', '*', '2', '-']
```

## Een eenvoudige rekenmachine

Gebruik nu de voorgaande methoden om een eenvoudige methode `rekenmachine(infix_string)` te implementeren die 
een `string` als invoer krijgt die een geldige infix-expressie voorstelt en die de waarde
van deze expressie als return-waarde heeft. Het eerste wat je zal moeten doen is de gegeven
`string` omzetten naar een sequentie van `string` die de tokens voorstellen. Voor de eenvoud nemen we aan dat de tokens van elkaar gescheiden worden door een spatie. In dit geval kan je de volgende lijn code gebruiken:
```
infix_tokens = infix_string.split()
```
De werking van de methode `rekenmachine` is als volgt:
```
>>> rekenmachine("3 + 5")
8.0
>>> rekenmachine("3 + 5 * 2")
13.0
>>> rekenmachine("( 3 + 5 ) * 2")
16.0
```