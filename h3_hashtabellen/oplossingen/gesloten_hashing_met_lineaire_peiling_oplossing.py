class HashSet:

    def __init__(self, max_size=10):

        ## data == None and deleted == False --> lege plaats
        ## data != None and deleted == False --> ingenomen door een item
        ## data == None and deleted == True --> verwijderd item. Kan ingenomen worden
        ## data != None and deleted == True --> mag niet voorkomen
        
        self._data = [None] * max_size
        self._deleted = [False] * max_size
        
        self._max_size = max_size
        self._num_items = 0

    def add(self, item):        
        if self._num_items == self._max_size:
            raise ValueError("Add on a full set")        
        
        # do not add duplicates
        if self.index_of(item) != -1:
            return -1

        self._num_items += 1
        index = hash(item) % self._max_size      
        while self._data[index] is not None:
            print(index)
            index += 1
            if index == self._max_size:
                index = 0

        self._data[index] = item
        self._deleted[index] = False # Moet altijd False worden, wat het ook was

        return index


    def index_of(self, item):
        index = hash(item) % self._max_size
        num_tries = 0
        while (num_tries < self._max_size 
            and (self._data[index] is not None or self._deleted[index])
            and self._data[index] != item):
            print(index)
            index += 1
            if index == self._max_size:
                index = 0
            num_tries += 1
        
        return index if self._data[index] == item else -1

    def delete(self, item):
        index = self.index_of(item)
        if index == -1:
            return False
        self._data[index] = None
        self._deleted[index] = True
        self._num_items -= 1
        return True

if __name__ == "__main__":
    hash_set = HashSet(max_size=10)
    print("Toevoegen 10: ",hash_set.add(10))
    print("Toevoegen 15: ",hash_set.add(15))
    print("Toevoegen 29: ",hash_set.add(29))
    print("Toevoegen 100: ",hash_set.add(100))
    print("Toevoegen 115: ",hash_set.add(115))
    print("Toevoegen 129: ",hash_set.add(129))

    print("Zoeken naar 10", hash_set.index_of(10))
    print("Zoeken naar 129", hash_set.index_of(129))

    print("Verwijderen 129", hash_set.delete(129))

    print("Zoeken naar 129", hash_set.index_of(129))

    print("Toevoegen 129: ",hash_set.add(129))

    # Verwijder 100
    print("Verwijderen 100", hash_set.delete(100))
    print("Verwijderen 100", hash_set.delete(100))

    # Zoek naar 129
    print("Zoeken naar 129", hash_set.index_of(129))

    print("Toevoegen 120: ",hash_set.add(120))

    ## Vullen van de tabel
    print("Toevoegen 3: ",hash_set.add(3))
    print("Toevoegen 4: ",hash_set.add(4))
    print("Toevoegen 77: ",hash_set.add(77))
    print("Toevoegen 88: ",hash_set.add(88))

    ## Nog een vullen als de tabel vol is
    print("Toevoegen 99: ",hash_set.add(99))