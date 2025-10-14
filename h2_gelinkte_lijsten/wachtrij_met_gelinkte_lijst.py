class QueueList:

    class Knoop:

        def __init__(self,data=None,volgende=None) -> None:
            self.data = data
            self.volgende = volgende

    def __init__(self) -> None:
        self.kop = None
        self.staart = None

    def is_empty(self):
        return self.kop is None

    def enqueue(self,data):
        pass
       

    def front(self):
        pass

    def dequeue(self):
        pass
    
    def invert(self):
        pass
