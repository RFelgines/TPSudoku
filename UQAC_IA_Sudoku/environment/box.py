class box:
    number = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'value':
                self.number = int(value)
        if self.number is None:
            self.number = 'X'

    def empty(self):
        self.number = None

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number
