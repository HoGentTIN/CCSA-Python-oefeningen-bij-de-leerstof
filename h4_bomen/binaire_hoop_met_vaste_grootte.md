# Implementatie van een binaire hoop

Schrijf een klasse `BinaryHeap` die een binaire hoop implementeert op de manier
zoals besproken in de cursustekst.
In het bijzonder moet je klasse over de volgende methoden beschikken.
* `BinaryHeap`: de constructor, die ook aangeeft wat het maximale aantal elementen in de binaire hoop is
* `is_empty`: geeft aan of de hoop leeg is.
* `get_min_elem`: retourneert het kleinste element (wanneer de binaire hoop niet leeg is)
* `insert_elem`: voegt een nieuw element toe aan de binaire hoop
* `remove_min_elem`: verwijdert en retourneert het kleinste element van de binaire hoop (wanneer die niet leeg is)
* `__str__`: deze methode retourneert de array-voorstelling van de binaire hoop

Het vergelijken van elementen gebeurt op basis van de `<`-operator.

Een mogelijk gebruik van deze klasse is als volgt:
```
>>> b = BinaryHeap()
>>> b.is_empty()
True
>>> b.insert_elem(3)
>>> b.is_empty()
False
>>> b.insert_elem(1)
>>> b.insert_elem(2)
>>> print(b)
[1, 3, 2]
>>> b.remove_min_elem()
1
>>> print(b)
[2, 3]
>>> b.remove_min_elem()
2
>>> b.remove_min_elem()
3
>>> print(b)
[]
>>> b.is_empty()
True
```

