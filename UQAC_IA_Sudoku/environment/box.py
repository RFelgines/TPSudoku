class box:
    number = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'value':
                self.number = int(value)
        if self.number is None:
            self.number = 0

    def setNumber(self, number):
        self.number = int(number)

    def getNumber(self):
        return int(self.number)
