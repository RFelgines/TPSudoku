import logging

import environment.env
from environment.box import box


class grid:
    grid = None

    def __init__(self):
        environment.env.grid = [[box() for i in range(9)] for j in range(9)]

    def fillGrid(self, difficulty):
        if difficulty == 1: # easy
            startNumbers = 25

        elif difficulty == 2: # medium
            startNumbers = 20

        elif difficulty == 3: # hard
            starNumbers = 15

        else:
            logging.INFO('Invalid difficulty')
            return False

        NumbersToPlace = startNumbers

    def getGrid(self):
       return self.grid
