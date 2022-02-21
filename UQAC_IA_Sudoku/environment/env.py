import logging

import environment.env
from environment.box import box


class grid:
    grid = None

    def __init__(self):
        environment.env.grid = [[box() for i in range(9)] for j in range(9)]

    def getGrid(self):
       return self.grid

    def setGrid(self, grid):
        self.grid = grid

    def checkColumn(self, column):
        availableNumbers = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if availableNumbers[grid[column][i] - 1] != 0:  #tkt ça marche frero
                availableNumbers[grid[column][i] - 1] = 0
            else:
                return False # Element already modified
        return True

    def checkRow(self, row):
        availableNumbers = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if availableNumbers[grid[i][row] - 1] != 0:  #tkt ça marche frero
                availableNumbers[grid[i][row] - 1] = 0
            else:
                return False # Element already modified
        return True

    def checkSubgrid(self, SubgridRowNumber, SubgridColumnNumber):
        availableNumbers = [1,2,3,4,5,6,7,8,9]
        for i in range(3):
            for j in range 3:
                if availableNumbers[grid[i + 3*SubgridColumnNumber][j +3*SubgridRowNumber] - 1] != 0:  #tkt ça marche frero
                    availableNumbers[grid[i + 3*SubgridColumnNumber][j +3*SubgridRowNumber] - 1] = 0
                else:
                    return False # Element already modified
        return True

