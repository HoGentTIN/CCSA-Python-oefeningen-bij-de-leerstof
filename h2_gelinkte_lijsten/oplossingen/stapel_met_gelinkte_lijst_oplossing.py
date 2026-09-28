class StackList:


    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende


    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        nieuwe_top = StackList.Knoop(data, self.top)
        self.top = nieuwe_top

    def peek(self):
        if self.is_empty():
            raise ValueError("Peek op lege stapel")
        return self.top.data

    def pop(self):
        if self.is_empty():
            raise ValueError("Pop op lege stapel")
        data = self.top.data
        self.top = self.top.volgende
        return data