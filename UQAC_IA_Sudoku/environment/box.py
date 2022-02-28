class box:
    number = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'value':
                self.number = int(value)

    def empty(self):
        self.number = None

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number
