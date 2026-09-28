class QueueList:


    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende


    def __init__(self):
        self.kop    = None
        self.staart = None

    def is_empty(self):
        return self.staart is None

    def enqueue(self, data):
        nieuwe_staart = QueueList.Knoop(data)
        if self.is_empty():
            self.kop = nieuwe_staart
            self.staart = nieuwe_staart
        else:            
            self.staart.volgende = nieuwe_staart
            self.staart = nieuwe_staart

    def front(self):
        if self.is_empty():
            raise ValueError("Frond op lege wachtrij")
        return self.kop.data

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Dequeue op lege wachtrij")
        data = self.kop.data
        self.kop = self.kop.volgende
        if self.kop is None:
            self.staart = None
        return data


    def invert(self):       
        vorige = None
        huidige = self.kop        
        while not huidige is None:
            volgende = huidige.volgende 
            huidige.volgende = vorige           
            vorige = huidige
            huidige = volgende            
        self.kop, self.staart = self.staart, self.kop


    def __str__(self):        
        ref = self.kop
        elems = []
        while not ref is None:
            elems.append(ref.data)
            ref = ref.volgende
        return "[" + ",".join(str(x) for x in elems) + "]"