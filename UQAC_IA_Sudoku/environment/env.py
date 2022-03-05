import math
from random import sample

from UQAC_IA_Sudoku.environment.box import box


class env:
    grid = None
    base = 3
    side = base * base

    def __init__(self):
        self.grid = [[box() for i in range(9)] for j in range(9)]

    def getGrid(self):
        return self.grid

    def getRow(self, pos):  # Return the row concerned by the pos
        return [self.grid[pos[0]][i].getNumber() for i in range(9)]

    def getColumn(self, pos):  # Return the column concerned by the pos
        return [self.grid[i][pos[1]].getNumber() for i in range(9)]

    def closestMiddle(self, pos):  # Return the middle of the closest square from the pos
        middles = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
        dist = [math.dist(elem, pos) for elem in middles]
        return middles[dist.index(min(dist))]

    def getSquare(self, pos):  # Return the square concerned by the pos
        closest = self.closestMiddle(pos)
        ret = [[self.grid[i][j].getNumber() for i in range(closest[0] - 1, closest[0] + 2)]
               for j in range(closest[1] - 1, closest[1] + 2)]
        return ret[0] + ret[1] + ret[2]

    def availableNumbers(self, pos):  # Checks what numbers can be placed at a certain position
        return [i for i in range(9) if
                i not in self.getRow(pos) and i not in self.getColumn(pos) and i not in self.getSquare(pos)]

    def generateSudoku(self):
        rBase = range(self.base)
        rows = [g*self.base + r for g in self.generateSudoku_shuffle(rBase) for r in self.generateSudoku_shuffle(rBase)]
        cols = [g*self.base + c for g in self.generateSudoku_shuffle(rBase) for c in self.generateSudoku_shuffle(rBase)]
        nums = self.generateSudoku_shuffle(range(1, self.base*self.base+1))

        board = [[nums[self.generateSudoku_patern(r, c)] for c in cols] for r in rows]

        for i in range(9):
            for j in range(9):
                self.grid[i][j].setNumber(board[i][j])

    def generateSudoku_patern(self, r, c):
        return (self.base*(r%self.base)+r//self.base+c)%self.side

    def generateSudoku_shuffle(self, s):
        return sample(s, len(s))

    """
    def LCR(self):
        ConstraintsValue = numpy.zeros(9, 9)
        LCR = 0
        posLCR = 0, 0
        for i in range(9):
            for j in range(9):
                ConstraintsValue[i][j] = len(self.availableNumbers(i, j))
                if ConstraintsValue[i][j] >= LCR:
                    posLCR = ConstraintsValue[i][j]
        return posLCR

    def MRV(self):
        ConstraintsValue = numpy.zeros(9, 9)
        LCR = 0
        posLCR = 0, 0
        for i in range(9):
            for j in range(9):
                ConstraintsValue[i][j] = len(self.availableNumbers(i, j))
                if ConstraintsValue[i][j] >= LCR:
                    posLCR = ConstraintsValue[i][j]
        return posLCR
    """

    def checkPlacement(self, pos, number):  # Check if placement is correct
        return number not in self.getRow(pos) and number not in self.getColumn(pos) \
               and number not in self.getSquare(pos)
        # True = Number can be placed here
        # False = Number cannot be placed here

    def placeElement(self, pos, number):  # Place number at the pos if possible
        if self.checkPlacement(pos, number):
            self.grid[pos[0]][pos[1]].setNumber(number)
            return True
        else:
            return False
        # True = Placement success
        # False = Placement failure
