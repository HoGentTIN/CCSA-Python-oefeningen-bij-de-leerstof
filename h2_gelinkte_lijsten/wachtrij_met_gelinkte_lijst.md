# Wachtrij met gelinkte lijst

Een wachtrij is een FIFO-datastructuur. Het element dat het eerst op de wachtrij werd geplaatst is ook het eerste dat wordt verwijderd. Een wachtrij heeft m.a.w. twee uiteinden: een kop en een staart. Elementen worden toegevoegd aan de kant van de staart en verwijderd aan de kant van de kop. Een wachtrij kan geïmplementeerd worden m.b.v. een gelinkte lijst. Hierbij worden twee `Knoop`-referenties bijgehouden: één naar de kop en één naar de staart.

Schrijf een klasse `QueueList` die een wachtrij implementeert m.b.v. een gelinkte lijst. 
De klasse `QueueList` moet over de volgende methoden beschikken.
* `QueueList`: de constructor, maakt een lege wachtrij met een `kop` en een `staart`. We gebruiken in dit geval geen ankercomponenten.
* `is_empty`: controleert of de wachtrij leeg is
* `enqueue`: voegt een gegeven element toe aan de staart van de wachtrij
* `front`: retourneert het voorste element, m.a.w. de kop, van de wachtrij, zonder het te verwijderen
* `dequeue`: retourneert en verwijdert het voorste element van de wachtrij

Een mogelijk gebruik van deze wachtrij is als volgt:

```
>>> q = QueueList()
>>> q.is_empty()
True
>>> q.enqueue("One")
>>> q.is_empty()
False
>>> q.front()
'One'
>>> q.enqueue("Two")
>>> q.enqueue("Three")
>>> q.front()
'One'
>>> q.dequeue()
'One'
>>> q.dequeue()
'Two'
>>> q.front()
'Three'
>>> q.is_empty()
False
>>> q.enqueue("Four")
>>> q.dequeue()
'Three'
>>> q.dequeue()
'Four'
>>> q.is_empty()
True
```

Breid de wachtrij vervolgens uit met een methode `invert`. Deze methode plaatst
de elementen van een bestaande wachtrij in omgekeerde volgorde. Er wordt geen nieuwe wachtrij
gegenereerd. Je mag geen `data` velden wijzigen en geen nieuwe knopen alloceren. Je mag enkel de referenties 
van de gelinkte lijst manipuleren. Een mogelijk gebruik van de methode `invert` is als volgt:
```
>>> q = QueueList()
>>> for x in range(1,5):
...     q.enqueue(x)
...
>>> q.front()
1
>>> q.invert()
>>> q.front()
4
>>> q.dequeue()
4
>>> q.front()
3
>>> q.invert()
>>> q.front()
1
>>> q.dequeue()
1
>>> q.dequeue()
2
>>> q.front()
3
>>> q.invert()
>>> q.front()
3
>>> q.dequeue()
3
>>> q.invert()
>>> q.is_empty()
True
>>> q.enqueue(10)
>>> q.front()
10
```


