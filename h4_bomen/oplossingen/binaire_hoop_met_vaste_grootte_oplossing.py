class BinaryHeap:

    def __init__(self, max_size=10):
        self._num_elem = 0
        self._data = [None] * max_size

    def empty(self):
        """Controleert of de binaire hoop leeg is.
        """
        return self._num_elem == 0

    def _swap(self, i1, i2):
        """Wisselt twee elementen om in de binaire hoop. 
           De posities van de om te wisselen elementen worden aangeven door de
           indices <code>i1</code> en <code>i2</code>.
        """
        self._data[i1], self._data[i2] = self._data[i2], self._data[i1]

    def get_min_elem(self):
        """Retourneert het kleinste element van de binaire hoop indien niet leeg.
        """
        if self.empty():
            raise ValueError("get_min_elem on empty heap")
        return self._data[0]

    @staticmethod
    def _parent(child_index):
        """Geeft de index van de ouder terug.
        """
        return (child_index - 1) // 2

    @staticmethod
    def _children(parent_index):
        """Geeft de indices van de kinderen terug. Controleert niet of deze indices geldig zijn.
        """
        return 2*parent_index + 1, 2*parent_index + 2

    def _is_leaf(self, index):
        """Controleert of een positie een blad is.
        """
        child1, _ = BinaryHeap._children(index)
        return child1 >= self._num_elem

    def insert_elem(self, elem):
        """Voegt een element toe aan de binaire hoop. Controleert niet of er nog plaats is.
        """
        index = self._num_elem
        self._data[index] = elem
        while index != 0 and elem < self._data[BinaryHeap._parent(index)]:
            self._swap(index, BinaryHeap._parent(index))
            index = BinaryHeap._parent(index)

        self._num_elem += 1

    def remove_min_elem(self):
        """Verwijdert en retourneert het kleinste element uit de binaire hoop.
        """
        min_elem = self.get_min_elem()
        self._num_elem -= 1

        self._data[0] = self._data[self._num_elem]
        self._data[self._num_elem] = None

        # Bubble down
        index = 0
        elem = self._data[0]
        
        while (not self._is_leaf(index) and 
            elem > self._data[self._index_min_child(index)]):
            child_index = self._index_min_child(index)
            self._swap(index, child_index)
            index = child_index


        return min_elem

    def _index_min_child(self, index):
        """Geef index van het kind waar het kleinste element staat.
        """
        child1, child2 = BinaryHeap._children(index)

        ## Beide kinderen geldig
        if child2 < self._num_elem:
            return child1 if self._data[child1] < self._data[child2] else child2
        return child1 if child1 < self._num_elem else None
        
        
    def __str__(self):
        """Geef een stringrepresentatie van de binaire hoop.
        """
        return str(self._data[:self._num_elem])


if __name__ == '__main__':
    b = BinaryHeap()
    print("heap is empty: ", b.empty())
    b.insert_elem(3)
    b.insert_elem(1)
    b.insert_elem(2)
    print(b)
    min_elem = b.remove_min_elem()
    print("Min element is ", min_elem)
    print(b)

    b2 = BinaryHeap(max_size=20)
    for elem in [11, 13, 1, 15, 6, 5, 9, 16, 3, 10, 7, 4, 12, 14, 2]:
        b2.insert_elem(elem)        
    print(b2)

    b3 = BinaryHeap(max_size=20)
    for elem in [1,2,3,6,4,8,10,17,13,19,24,23,9,12,31,30,18,15]:
        b3.insert_elem(elem)
    print(b3)
    min_elem = b3.remove_min_elem()
    print("Kleinste element:", min_elem)
    print(b3)
    min_elem = b3.remove_min_elem()
    print("Kleinste element:", min_elem)
    print(b3)
    min_elem = b3.remove_min_elem()
    print("Kleinste element:", min_elem)
    print(b3)

    import random
    b4 = BinaryHeap(max_size=10000)
    elems = list(range(10000))
    random.shuffle(elems)
    for elem in elems:
        b4.insert_elem(elem)
    min_elem = b4.get_min_elem()
    print(f"Kleinste element: {min_elem}")
    b4.remove_min_elem()
    min_elem = b4.get_min_elem()
    print(f"Kleinste element: {min_elem}")
    for _ in range(9998):
        b4.remove_min_elem()
    print(b4.get_min_elem())